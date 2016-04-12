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


def get_resource(filename):
    import pkg_resources, os
    return pkg_resources.resource_filename("deluge.plugins.texttab",
                                           os.path.join("data", filename))
