#
# gtkui.py
#
# Copyright (C) 2009 haydent <www.httech.com.au>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
#
# Deluge is free software.
#
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
#
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.
#

import gtk

from deluge.log import LOG as log
from deluge.ui.client import client
from deluge.plugins.pluginbase import GtkPluginBase
import deluge.component as component
import deluge.common
from twisted.internet.task import LoopingCall
from deluge.ui.gtkui.torrentdetails import Tab
from common import get_resource

class GtkUI(GtkPluginBase):
    def enable(self):
        self.glade = gtk.glade.XML(get_resource("config.glade"))

        component.get("Preferences").add_page("textTab", self.glade.get_widget("prefs_box"))
        component.get("PluginManager").register_hook("on_apply_prefs", self.on_apply_prefs)
        component.get("PluginManager").register_hook("on_show_prefs", self.on_show_prefs)
        
        self._text_tab = TextTab()
        component.get("TorrentDetails").add_tab(self._text_tab)
        
        self.textTab_timer = LoopingCall(self._text_tab.update_tab)
        
        client.texttab.get_config().addCallback(self.setTimer)
        
    def setTimer(self, config):
        try:
            self.textTab_timer.stop()
        except:
            pass
        self.textTab_timer.start(config["poll"])


    def disable(self):
        component.get("Preferences").remove_page("textTab")
        component.get("TorrentDetails").remove_tab("TextTab")
        component.get("PluginManager").deregister_hook("on_apply_prefs", self.on_apply_prefs)
        component.get("PluginManager").deregister_hook("on_show_prefs", self.on_show_prefs)
        self.textTab_timer.stop()

    def on_apply_prefs(self):
        log.debug("applying prefs for textTab")
        config = {
            "path1":self.glade.get_widget("txt_path1").get_text(),
            "poll":self.glade.get_widget("spin_poll").get_value(),
            "reverse":self.glade.get_widget("check_reverse").get_active()            
        }
        client.texttab.set_config(config)
        self._text_tab.update_tab(True)
        client.texttab.get_config().addCallback(self.setTimer)

    def on_show_prefs(self):
        client.texttab.get_config().addCallback(self.cb_get_config)

    def cb_get_config(self, config):
        "callback for on show_prefs"
        self.glade.get_widget("txt_path1").set_text(config["path1"])
        self.glade.get_widget("spin_poll").set_value(config["poll"])
        self.glade.get_widget("check_reverse").set_active(config["reverse"])


class TextTab(Tab):
    def __init__(self):
        Tab.__init__(self)
        glade_tab = gtk.glade.XML(get_resource("text_tab.glade"))

        self._name = "TextTab"
        self._child_widget = glade_tab.get_widget("text_tab")
        self._tab_label = glade_tab.get_widget("text_tab_label")
        self._tab_label_label = glade_tab.get_widget("text_tab_label_label")  

        self.textview = glade_tab.get_widget("text_tab_textview") 
        self.textview.set_editable(False)
        self.textview.set_cursor_visible(False)

    def update_tab(self, force = False):
        client.texttab.get_text(force).addCallback(self.cb_get_text)
        
    def cb_get_text(self, (result, filename, text)):
        if result == 0:
            log.info("textTab, file not found")
            self.textview.get_buffer().set_text(text)
            self._tab_label_label.set_text(filename)
        elif result == 1:
            log.info("textTab, file contents: \n%s" % text)
            self.textview.get_buffer().set_text(text)
            self._tab_label_label.set_text(filename)
        elif result == 2:
            log.info("textTab, no change")


    def __dest(self, widget, response):        
        widget.destroy()


    def update(self):
        pass
