/*
Script: texttab.js
    The client-side javascript code for the textTab plugin.

Copyright:
    (C) haydent 2016 <www.httech.com.au>

    This file is part of textTab and is licensed under GNU General Public License 3.0, or later, with
    the additional special exception to link portions of this program with the OpenSSL library.
    See LICENSE for more details.
*/

textTabPlugin = Ext.extend(Deluge.Plugin, {
    constructor: function(config) {
        config = Ext.apply({
            name: "textTab"
        }, config);
        textTabPlugin.superclass.constructor.call(this, config);
    },

    onDisable: function() {

    },

    onEnable: function() {

    }
});
new textTabPlugin();
