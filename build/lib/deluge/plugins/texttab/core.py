#
# -*- coding: utf-8 -*-#

# Copyright (C) 2016 haydent <www.httech.com.au>
#
# Basic plugin template created by:
# Copyright (C) 2008 Martijn Voncken <mvoncken@gmail.com>
# Copyright (C) 2007-2009 Andrew Resch <andrewresch@gmail.com>
# Copyright (C) 2009 Damien Churchill <damoxc@gmail.com>
# Copyright (C) 2010 Pedro Algarvio <pedro@algarvio.me>
#
# This file is part of textTab and is licensed under GNU General Public License 3.0, or later, with
# the additional special exception to link portions of this program with the OpenSSL library.
# See LICENSE for more details.
#

import logging
import os
from deluge.plugins.pluginbase import CorePluginBase
import deluge.component as component
import deluge.configmanager
from deluge.core.rpcserver import export
#from twisted.internet.task import LoopingCall

DEFAULT_PREFS = {
    "path1":""
}

log = logging.getLogger(__name__)

class Core(CorePluginBase):
    def enable(self):
        self.config = deluge.configmanager.ConfigManager("texttab.conf", DEFAULT_PREFS)
        #self.update_status_timer = LoopingCall(self.update_stats)
        #self.update_status_timer.start(5)

    def disable(self):
        #self.update_status_timer.stop()
        pass

    def update(self):
        pass
        
    @export
    def get_text(self):
        self.path = self.config["path1"]
        
        if os.path.isfile(self.path):
            log.info("textTab, opening file: %s" % self.path)
            f = open(self.path, "r")            
            str = f.read();
            #log.info("textTab, file contents: \n%s" % str)
            f.close()
            return str
        else:
            log.info("textTab, file not found: %s" % self.path)        
        


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
