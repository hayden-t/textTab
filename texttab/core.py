#
# core.py
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

from deluge.log import LOG as log
import os
from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component
import deluge.configmanager
from deluge.core.rpcserver import export
import hashlib

DEFAULT_PREFS = {
    "path1":"",
    "poll": 5
}

class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager("texttab.conf", DEFAULT_PREFS)
        self.hash1 = ""

    def disable(self):
        pass

    def update(self):
        pass
        
    @export
    def get_text(self):
        self.path = self.config["path1"]
        
        fname = os.path.basename(self.path)
        fname = os.path.splitext(fname)[0]
        
        if os.path.isfile(self.path):
            log.info("textTab, opening file: %s" % self.path)
            f = open(self.path, "r")     
            
            ftext = f.read()
            fhash = hashlib.md5(ftext).hexdigest()
            if self.hash1 == fhash:
                return (2, False, False)
            self.hash1 = fhash
            if not ftext:
                ftext = '(empty)'
            #log.info("textTab, file contents: \n%s" % str)
            f.close()
            return (1, fname, ftext)
        else:
            log.info("textTab, file not found: %s" % self.path)
            self.hash1 = ""
            return (0, fname, '(file not found)')

    @export
    def set_config(self, config):
        """Sets the config dictionary"""
        for key in config.keys():
            self.config[key] = config[key]
        self.config.save()

    @export
    def get_config(self):
        """Returns the config dictionary"""
        return self.config.config
