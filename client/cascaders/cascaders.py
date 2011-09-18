#!/usr/bin/python -O

'''
Startup file, responsible for setting up the application and starting the gui
'''

import logging
from optparse import OptionParser
import dbus.mainloop.glib

import gtk

import mainframe
import dbusutil


class RaiseableService(dbusutil.DbusService):
    '''Service provides a method of raising the window to dbus'''
    def __init__(self, interface, path, app):
        super(RaiseableService, self).__init__(interface, path)
        self.app = app

    @dbusutil.method('com.compsoc')
    def showWindow(self):
        self.app.window.present()

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    parser = OptionParser()
    parser.add_option('-n', '--noshow', action='store_false',
                      help='don\'t show the main window on startup')
    parser.add_option('-d', '--debug', action='store_false',
                      help='start with debug mode on. This is a lot slower')

    (options, args) = parser.parse_args()
    showWindow = options.noshow is None
    debugEnabled = options.debug is not None

    if debugEnabled:
        logging.basicConfig(level=logging.DEBUG)

    #we use dbus to ensure that there is only one running instance of the
    #program. When in debug mode there can be more than one instance
    interface = 'com.compsoc'
    path = '/com/compsoc/cascaders'
    if not dbusutil.isOwner(interface) and not debugEnabled:
        logging.debug('Cascaders app already running, pulling up interface')
        client = dbusutil.DbusClient(interface, path)
        client.showWindow()
    else:
        win = mainframe.CascadersFrame(debugEnabled, show=showWindow)
        obj = RaiseableService(interface, path, win)
        gtk.main()
