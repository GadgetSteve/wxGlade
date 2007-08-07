#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# generated by wxGlade 0.3.5 on Wed Oct 27 15:47:24 2004

#from wxPython.wx import *
import wx

class wxGladePreferencesUI(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: wxGladePreferencesUI.__init__
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.sizer_6_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, _("Local widget path"))
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.use_menu_icons = wx.CheckBox(self.notebook_1_pane_1, -1, _("Use icons in menu items"))
        self.frame_tool_win = wx.CheckBox(self.notebook_1_pane_1, -1, _("Show properties and tree windows as small frames (Win32 only)"))
        self.show_progress = wx.CheckBox(self.notebook_1_pane_1, -1, _("Show progress dialog when loading wxg files"))
        self.remember_geometry = wx.CheckBox(self.notebook_1_pane_1, -1, _("Remember position and size of wxGlade windows"))
        self.show_sizer_handle = wx.CheckBox(self.notebook_1_pane_1, -1, _("Show \"handles\" of sizers"))
        self.use_kde_dialogs = wx.CheckBox(self.notebook_1_pane_1, -1, _("Use native file dialogs on KDE"))
        self.open_save_path = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.codegen_path = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.number_history = wx.SpinCtrl(self.notebook_1_pane_1, -1, "4", min=0, max=100)
        self.buttons_per_row = wx.SpinCtrl(self.notebook_1_pane_1, -1, "5", min=1, max=100)
        self.use_dialog_units = wx.CheckBox(self.notebook_1_pane_2, -1, _("Use dialog units by default for size properties"))
        self.wxg_backup = wx.CheckBox(self.notebook_1_pane_2, -1, _("Create backup wxg files"))
        self.codegen_backup = wx.CheckBox(self.notebook_1_pane_2, -1, _("Create backup files for generated source"))
        self.allow_duplicate_names = wx.CheckBox(self.notebook_1_pane_2, -1, _("Allow duplicate widget names"))
        self.default_border = wx.CheckBox(self.notebook_1_pane_2, -1, _("Default border width for widgets"))
        self.default_border_size = wx.SpinCtrl(self.notebook_1_pane_2, -1, "", min=0, max=20)
        self.autosave = wx.CheckBox(self.notebook_1_pane_2, -1, _("Auto save wxg files every "))
        self.autosave_delay = wx.SpinCtrl(self.notebook_1_pane_2, -1, "120", min=30, max=300)
        self.backup_suffix = wx.RadioBox(self.notebook_1_pane_2, -1, _("Backup options"), choices=[_("append ~ to filename"), _("append .bak to filename")], majorDimension=2, style=wx.RA_SPECIFY_COLS)
        self.local_widget_path = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.choose_widget_path = wx.Button(self.notebook_1_pane_2, -1, "...", style=wx.BU_EXACTFIT)
        self.ok = wx.Button(self, wx.ID_OK, "")
        self.cancel = wx.Button(self, wx.ID_CANCEL, "")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: wxGladePreferencesUI.__set_properties
        self.SetTitle(_("wxGlade: preferences"))
        self.use_menu_icons.SetValue(1)
        self.frame_tool_win.SetValue(1)
        self.show_progress.SetValue(1)
        self.remember_geometry.SetValue(1)
        self.show_sizer_handle.SetValue(1)
        self.use_kde_dialogs.SetValue(1)
        self.open_save_path.SetSize((196, -1))
        self.codegen_path.SetSize((196, -1))
        self.number_history.SetSize((196, -1))
        self.buttons_per_row.SetSize((196, -1))
        self.wxg_backup.SetValue(1)
        self.codegen_backup.SetValue(1)
        self.allow_duplicate_names.Hide()
        self.default_border_size.SetSize((45, 22))
        self.autosave_delay.SetSize((45, 22))
        self.backup_suffix.SetSelection(0)
        self.ok.SetDefault()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: wxGladePreferencesUI.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        sizer_7_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.FlexGridSizer(4, 2, 0, 0)
        sizer_3.Add(self.use_menu_icons, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.frame_tool_win, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.show_progress, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.remember_geometry, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.show_sizer_handle, 0, wx.ALL|wx.EXPAND, 5)
        sizer_3.Add(self.use_kde_dialogs, 0, wx.ALL|wx.EXPAND, 5)
        label_1 = wx.StaticText(self.notebook_1_pane_1, -1, _("Initial path for \nfile opening/saving dialogs:"))
        sizer_4.Add(label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.open_save_path, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5)
        label_2_copy = wx.StaticText(self.notebook_1_pane_1, -1, _("Initial path for \ncode generation file dialogs:"))
        sizer_4.Add(label_2_copy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.codegen_path, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5)
        #label_2 = wx.StaticText(self.notebook_1_pane_1, -1, "Number of items in file history\n(wxPython >= 2.3.3)")
        label_2 = wx.StaticText(self.notebook_1_pane_1, -1, _("Number of items in file history"))
        sizer_4.Add(label_2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.number_history, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5)
        label_2_copy_1 = wx.StaticText(self.notebook_1_pane_1, -1, _("Number of buttons per row\nin the main palette"))
        sizer_4.Add(label_2_copy_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.buttons_per_row, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5)
        sizer_4.AddGrowableCol(1)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 3)
        self.notebook_1_pane_1.SetAutoLayout(True)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        sizer_3.Fit(self.notebook_1_pane_1)
        sizer_3.SetSizeHints(self.notebook_1_pane_1)
        sizer_5.Add(self.use_dialog_units, 0, wx.ALL|wx.EXPAND, 5)
        sizer_5.Add(self.wxg_backup, 0, wx.ALL|wx.EXPAND, 5)
        sizer_5.Add(self.codegen_backup, 0, wx.ALL|wx.EXPAND, 5)
        sizer_5.Add(self.allow_duplicate_names, 0, wx.ALL|wx.EXPAND, 5)
        sizer_7.Add(self.default_border, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_7.Add(self.default_border_size, 0, wx.ALL|wx.FIXED_MINSIZE, 5)
        sizer_5.Add(sizer_7, 0, wx.EXPAND, 0)
        sizer_7_copy.Add(self.autosave, 0, wx.LEFT|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_7_copy.Add(self.autosave_delay, 0, wx.TOP|wx.BOTTOM|wx.FIXED_MINSIZE, 5)
        label_3 = wx.StaticText(self.notebook_1_pane_2, -1, " seconds")
        sizer_7_copy.Add(label_3, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL|wx.FIXED_MINSIZE, 5)
        sizer_5.Add(sizer_7_copy, 0, wx.EXPAND, 0)
        sizer_5.Add(self.backup_suffix, 0, wx.ALL|wx.EXPAND, 5)
        sizer_6.Add(self.local_widget_path, 1, wx.ALL, 3)
        sizer_6.Add(self.choose_widget_path, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_5.Add(sizer_6, 0, wx.ALL|wx.EXPAND, 5)
        self.notebook_1_pane_2.SetAutoLayout(True)
        self.notebook_1_pane_2.SetSizer(sizer_5)
        sizer_5.Fit(self.notebook_1_pane_2)
        sizer_5.SetSizeHints(self.notebook_1_pane_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, _("Interface"))
        self.notebook_1.AddPage(self.notebook_1_pane_2, _("Other"))
        #sizer_1.Add(wx.NotebookSizer(self.notebook_1), 1, wx.ALL|wx.EXPAND, 5)
        sizer_1.Add(self.notebook_1, 1, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(self.ok, 0, 0, 0)
        sizer_2.Add(self.cancel, 0, wx.LEFT, 10)
        sizer_1.Add(sizer_2, 0, wx.ALL|wx.ALIGN_RIGHT, 10)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class wxGladePreferencesUI


