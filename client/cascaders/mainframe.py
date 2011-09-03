'''
This is the gui class for the main application frame and it handles most of the
core functionality that the user uses while using the application.

It doesn't handle any functionality outside the frame such as messaging
'''
from logging import debug, error
import os
import socket

import wx

import generatedgui
import client

class CascadersFrame(generatedgui.GenCascadersFrame):
    def __init__(self):
        generatedgui.GenCascadersFrame.__init__(self, None)
        self.client = None

        self.subjects  = []
        self.cascaders = []
        self.cascading = False

        self.connect()

    #--------------------------------------------------------------------------
    # Connection stuff
    def isConnected(self):
        return self.client is not None

    def connect(self):
        ''' also does the setup post connect '''

        debug('Connecting...')

        try:
            logname = os.environ['LOGNAME']
        except KeyError:
            msg = ('Couldn\'t get LOGNAME from the enviroment,'
                   ' this only runs on Linux')
            error(msg)
            #FIXME dialog box has ok cancel
            wx.MessageDialog(self,
                             msg,
                             'Error getting user name').ShowModal()

        try:
            self.client = client.RpcClient('localhost',
                                           5010,
                                           logname,
                                           socket.gethostname())
            client.getSubjects(lambda s: None)
            client.getCascaders(lambda c: None)
        except socket.error:
            msg = 'Failed to connect to server'
            error(msg)
            wx.MessageDialog(self,
                             msg,
                             'error connecting').ShowModal()
            self.Close()

    #--------------------------------------------------------------------------
    def updateCascaderLists(self):
        pass

    #--------------------------------------------------------------------------
    def onStartStopCascading(self, event):
        if self.cascading:
            self.client.stopCascading()
        else:
            self.client.startCascading()
    
    def onAddSubject(self, event):
        #self.client.addSubjects(
        pass
    
    def onRemoveSubject(self, event):
        #self.client.removeSubjects(
        pass

    # Filter Stuff
    def onSubjectSelect(self, event):
        self.updateCascaderLists()
    
    def onLabSelect(self, event):
        self.updateCascaderLists()
    #-- -----------------------------------------------------------------------
