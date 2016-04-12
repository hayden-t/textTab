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
from deluge.ui.client import client
from deluge import component
from deluge.plugins.pluginbase import WebPluginBase

from common import get_resource

log = logging.getLogger(__name__)

class WebUI(WebPluginBase):

    scripts = [get_resource("texttab.js")]

    def enable(self):
        pass

    def disable(self):
        pass
