# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version May  2 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.aui

###########################################################################
## Class GenCascadersFrame
###########################################################################

class GenCascadersFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cascaders", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer6 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.AddGrowableRow( 1 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_status = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_status.SetMaxSize( wx.Size( -1,50 ) )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.m_status, wx.ID_ANY, u"Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.mStatus = wx.StaticText( self.m_status, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mStatus.Wrap( -1 )
		bSizer2.Add( self.mStatus, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer2.AddSpacer( ( 50, 0), 0, 0, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_status, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.mUserName = wx.StaticText( self.m_status, wx.ID_ANY, u"s1040340", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.mUserName.Wrap( -1 )
		bSizer2.Add( self.mUserName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button1 = wx.Button( self.m_status, wx.ID_ANY, u"Connect/Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.Enable( False )
		
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_status.SetSizer( bSizer2 )
		self.m_status.Layout()
		bSizer2.Fit( self.m_status )
		fgSizer6.Add( self.m_status, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_users = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_users, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Filter Cascaders:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer11.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bFilters = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bFilters.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		mFilterSubjectChoices = [ u"All" ]
		self.mFilterSubject = wx.Choice( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mFilterSubjectChoices, 0 )
		self.mFilterSubject.SetSelection( 0 )
		bFilters.Add( self.mFilterSubject, 0, wx.ALL, 5 )
		
		
		bFilters.AddSpacer( ( 50, 0), 0, 0, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Lab:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bFilters.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		mFilterLabChoices = [ u"All" ]
		self.mFilterLab = wx.Choice( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mFilterLabChoices, 0 )
		self.mFilterLab.SetSelection( 0 )
		bFilters.Add( self.mFilterLab, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panel6.SetSizer( bFilters )
		self.m_panel6.Layout()
		bFilters.Fit( self.m_panel6 )
		bSizer11.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		fgSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		fgCascaders = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgCascaders.AddGrowableCol( 0 )
		fgCascaders.AddGrowableRow( 0 )
		fgCascaders.SetFlexibleDirection( wx.BOTH )
		fgCascaders.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel9 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgCascaders.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		bCascaderList = wx.BoxSizer( wx.VERTICAL )
		
		bCascaderList.SetMinSize( wx.Size( 150,-1 ) ) 
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Cascaders:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bCascaderList.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		mFilteredCascaderListChoices = []
		self.mFilteredCascaderList = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mFilteredCascaderListChoices, 0 )
		bCascaderList.Add( self.mFilteredCascaderList, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgCascaders.Add( bCascaderList, 1, wx.EXPAND, 5 )
		
		fgSizer1.Add( fgCascaders, 1, wx.EXPAND, 5 )
		
		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		self.m_users.AddPage( self.m_panel1, u"Find Cascader", True )
		self.m_panel2 = wx.Panel( self.m_users, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer7.AddGrowableCol( 0 )
		fgSizer7.AddGrowableRow( 2 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.mCascadeStartStop = wx.Button( self.m_panel2, wx.ID_ANY, u"Start Cascading", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.mCascadeStartStop, 0, wx.ALL, 5 )
		
		bAddSubject = wx.BoxSizer( wx.HORIZONTAL )
		
		mCascadeSubjectChoices = []
		self.mCascadeSubject = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mCascadeSubjectChoices, 0 )
		self.mCascadeSubject.SetSelection( 0 )
		bAddSubject.Add( self.mCascadeSubject, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.mCascadeAddSub = wx.Button( self.m_panel2, wx.ID_ANY, u"Add Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		bAddSubject.Add( self.mCascadeAddSub, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.mCascadeRemoveSub = wx.Button( self.m_panel2, wx.ID_ANY, u"Remove Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		bAddSubject.Add( self.mCascadeRemoveSub, 0, wx.ALL, 5 )
		
		fgSizer7.Add( bAddSubject, 1, wx.EXPAND, 5 )
		
		mCascadeSubjectListChoices = []
		self.mCascadeSubjectList = wx.ListBox( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mCascadeSubjectListChoices, 0 )
		fgSizer7.Add( self.mCascadeSubjectList, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel2.SetSizer( fgSizer7 )
		self.m_panel2.Layout()
		fgSizer7.Fit( self.m_panel2 )
		self.m_users.AddPage( self.m_panel2, u"Cascade", False )
		
		fgSizer6.Add( self.m_users, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.SetSizer( fgSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.onConnectDisconnect )
		self.mFilterSubject.Bind( wx.EVT_CHOICE, self.onSubjectSelect )
		self.mFilterLab.Bind( wx.EVT_CHOICE, self.onLabSelect )
		self.mFilteredCascaderList.Bind( wx.EVT_LISTBOX, self.onCascaderClick )
		self.mFilteredCascaderList.Bind( wx.EVT_LISTBOX_DCLICK, self.onCascaderDClick )
		self.mCascadeStartStop.Bind( wx.EVT_BUTTON, self.onStartStopCascading )
		self.mCascadeAddSub.Bind( wx.EVT_BUTTON, self.onAddSubject )
		self.mCascadeRemoveSub.Bind( wx.EVT_BUTTON, self.onRemoveSubject )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onConnectDisconnect( self, event ):
		event.Skip()
	
	def onSubjectSelect( self, event ):
		event.Skip()
	
	def onLabSelect( self, event ):
		event.Skip()
	
	def onCascaderClick( self, event ):
		event.Skip()
	
	def onCascaderDClick( self, event ):
		event.Skip()
	
	def onStartStopCascading( self, event ):
		event.Skip()
	
	def onAddSubject( self, event ):
		event.Skip()
	
	def onRemoveSubject( self, event ):
		event.Skip()
	

###########################################################################
## Class GenMessagingDialog
###########################################################################

class GenMessagingDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 450,400 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.mConversations = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_CLOSE_ON_ALL_TABS|wx.aui.AUI_NB_DEFAULT_STYLE|wx.aui.AUI_NB_TAB_MOVE|wx.aui.AUI_NB_WINDOWLIST_BUTTON )
		
		bSizer14.Add( self.mConversations, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class GenMessagePanel
###########################################################################

class GenMessagePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		fgSizer10 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer10.AddGrowableCol( 0 )
		fgSizer10.AddGrowableCol( 1 )
		fgSizer10.AddGrowableRow( 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer10.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer17.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Send", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer10.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer10 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class GenAskForHelp
###########################################################################

class GenAskForHelp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ask For Help", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		
		fgSizer6 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer6.AddGrowableCol( 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Ask a cascader for help:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer6.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Subjects", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer9.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		mSubjectChoices = []
		self.mSubject = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mSubjectChoices, 0 )
		self.mSubject.SetSelection( 0 )
		bSizer9.Add( self.mSubject, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		fgSizer6.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Brief Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer10.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.mDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.mDescription.SetMinSize( wx.Size( 256,-1 ) )
		
		bSizer10.Add( self.mDescription, 1, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button6, 0, wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button7, 0, wx.ALL, 5 )
		
		fgSizer6.Add( bSizer11, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer6 )
		self.Layout()
		fgSizer6.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button6.Bind( wx.EVT_BUTTON, self.onOk )
		self.m_button7.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onOk( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

