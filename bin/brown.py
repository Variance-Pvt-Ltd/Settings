#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# written by @monees007 on Tue Jul 27 09:08:07 2021
#

import wx
import json

# import main

# load dependencies
with open('../json/credentials.json') as credentials_j:
    cj = dict(json.load(credentials_j))
with open('../json/settings.json') as settings_j:
    sj = dict(json.load(settings_j))
    wj = dict(sj['watchlist'])
sjtemp={}
for x in sj:
    sjtemp[x]=sj[x]

# end dependencies
class Watchlist_Item():
    def mark(parent, title, base, quote):
        # # begin wxGlade: Watchlist_Item.__init__
        # kwds["style"] = kwds.get("style", 0) | wx.BORDER_NONE | wx.TAB_TRAVERSAL
        # wx.Panel.__init__(self,None, wx.ID_ANY)
        # self = wx.Panel(None, wx.ID_ANY, "")
        self = wx.Panel(parent, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        self.title = title
        title =title
        # self.SetSizeWH(-1, 55)
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.SetForegroundColour(wx.Colour(255, 255, 255))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND | wx.LEFT | wx.TOP, 24)

        label_1 = wx.StaticText(self, wx.ID_ANY, title)
        label_1.SetForegroundColour(wx.Colour(255, 255, 255))
        label_1.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, title))
        sizer_2.Add(label_1, 1, wx.EXPAND | wx.LEFT, 6)

        self.bitmap_button_1 = wx.BitmapButton(self, wx.ID_ANY, wx.Bitmap("../assets/close.png", wx.BITMAP_TYPE_ANY),
                                               style=wx.BORDER_NONE | wx.BU_AUTODRAW | wx.BU_EXACTFIT | wx.BU_NOTEXT)
        self.bitmap_button_1.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.bitmap_button_1.SetSize(self.bitmap_button_1.GetBestSize())
        sizer_2.Add(self.bitmap_button_1, 0, wx.RIGHT, 6)

        grid_sizer_1 = wx.GridSizer(2, 2, 5, 12)
        sizer_1.Add(grid_sizer_1, 6, wx.ALL | wx.EXPAND, 24)

        label_2 = wx.StaticText(self, wx.ID_ANY, "Base Asset")
        label_2.SetForegroundColour(wx.Colour(255, 255, 255))
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, base)
        self.text_ctrl_1.SetMinSize((130, 33))
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALIGN_CENTER, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "Quote Asset")
        label_3.SetForegroundColour(wx.Colour(255, 255, 255))
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_1.Add(label_3, 0, wx.ALIGN_CENTER, 0)

        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, quote)
        self.text_ctrl_2.SetMinSize((130, 33))
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.ALIGN_CENTER, 0)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()

        # self.Bind(wx.EVT_BUTTON, Watchlist_Item.remove_watchlist, self.bitmap_button_1)
        self.bitmap_button_1.Bind(wx.EVT_BUTTON,Watchlist_Item.remove_watchlist)
        return self
        # end wxGlade

    def remove_watchlist(event):  # wxGlade: Watchlist_Item.<event_handler>
        print('trying to remove')
        print(event.GetEventObject())



def delete_r(title):
    print(title)
    # del sjtemp[title]
    with open('../json/settings.json', 'w') as setjson:
        json.dump(sjtemp, setjson)



def load_watchlist(self):
    wl = []
    for title in wj:
        base = wj[title]["base_asset"]
        quote = wj[title]["quote_asset"]
        wl.append(Watchlist_Item.mark(self.watchlist, title, base, quote))
    for x in wl:
        self.sizer_19.Add(x, 1, wx.EXPAND, 0)


class MyFrame(wx.Frame):

    def __init__(self, *args, **kwds):

        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0)
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((974, 1047))
        self.SetTitle("frame")
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.panel_1 = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_SIMPLE)
        self.panel_1.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.panel_1.SetForegroundColour(wx.Colour(255, 255, 255))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        top_pane = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_1.Add(top_pane, 0, wx.EXPAND, 0)

        label_14 = wx.StaticText(self.panel_1, wx.ID_ANY, "Variance Pvt. Ltd.")
        label_14.SetMinSize((180, 32))
        label_14.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        top_pane.Add(label_14, 0, wx.LEFT, 14)

        top_pane.Add((20, 20), 1, wx.EXPAND, 0)

        self.exit_button = wx.Button(self.panel_1, wx.ID_CANCEL, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.exit_button.SetMinSize((32, 32))
        self.exit_button.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.exit_button.SetBitmap(wx.Bitmap('../assets/close.png', wx.BITMAP_TYPE_ANY))
        top_pane.Add(self.exit_button, 0, 0, 0)

        self.backpanel = wx.Notebook(self.panel_1, wx.ID_ANY, style=wx.NB_FIXEDWIDTH)
        self.backpanel.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.backpanel.SetForegroundColour(wx.Colour(255, 255, 255))
        self.backpanel.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_1.Add(self.backpanel, 13, wx.EXPAND, 0)

        self.watchlist = wx.ScrolledWindow(self.backpanel, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.watchlist.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.watchlist.SetForegroundColour(wx.Colour(255, 255, 255))
        self.watchlist.SetScrollRate(10, 10)
        self.backpanel.AddPage(self.watchlist, "     Watchlist     ")

        self.sizer_19 = wx.BoxSizer(wx.VERTICAL)

        self.add_btn = wx.Button(self.watchlist, wx.ID_ADD, "")
        self.sizer_19.Add(self.add_btn, 0, wx.ALIGN_RIGHT | wx.LEFT | wx.RIGHT | wx.TOP, 11)

        # self.watchlist_pnl = wx.Panel(self.watchlist, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        # self.watchlist_pnl.SetScrollRate(10, 10)


        load_watchlist(self)

        self.Settings = wx.ScrolledWindow(self.backpanel, wx.ID_ANY, style=wx.BORDER_NONE | wx.TAB_TRAVERSAL)
        self.Settings.SetScrollRate(7, 7)
        self.backpanel.AddPage(self.Settings, "     Settings     ")

        sizer_3 = wx.BoxSizer(wx.VERTICAL)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.Settings, wx.ID_ANY, "Time Frame")
        label_1.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_1.SetForegroundColour(wx.Colour(255, 255, 255))
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(label_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.choices9 = ["1m", "3m", "5m", "15m", "30m", "1H", "2H", "4H", "6H", "8H", "12H", "1D", "3D", "1W", "1M"]
        self.time_frame = wx.Choice(self.Settings, wx.ID_ANY, choices=self.choices9)
        self.time_frame.SetMinSize((360, 35))
        current_selection = self.choices9.index(sj["timeframe"])
        self.time_frame.SetSelection(current_selection)
        sizer_4.Add(self.time_frame, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_1 = wx.StaticLine(self.Settings, wx.ID_ANY)
        static_line_1.SetBackgroundColour(wx.Colour(51, 51, 51))
        static_line_1.SetForegroundColour(wx.Colour(51, 51, 51))
        sizer_3.Add(static_line_1, 0, wx.ALL | wx.EXPAND, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)

        label_2 = wx.StaticText(self.Settings, wx.ID_ANY, "EMA 1")
        label_2.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_2.SetForegroundColour(wx.Colour(255, 255, 255))
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(label_2, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.ema1 = wx.TextCtrl(self.Settings, wx.ID_ANY, sj["ema1"])
        self.ema1.SetMinSize((222, 33))
        sizer_5.Add(self.ema1, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_2 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_2, 0, wx.EXPAND, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.Settings, wx.ID_ANY, "EMA 2")
        label_3.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_3.SetForegroundColour(wx.Colour(255, 255, 255))
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(label_3, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.ema2 = wx.TextCtrl(self.Settings, wx.ID_ANY, sj["ema2"])
        self.ema2.SetMinSize((222, 33))
        sizer_6.Add(self.ema2, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_3 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_3, 0, wx.EXPAND, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)

        label_4 = wx.StaticText(self.Settings, wx.ID_ANY, "Leverage")
        label_4.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_4.SetForegroundColour(wx.Colour(255, 255, 255))
        label_4.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(label_4, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.leverage = wx.TextCtrl(self.Settings, wx.ID_ANY, str(sj["leverage"]))
        self.leverage.SetMinSize((222, 33))
        sizer_7.Add(self.leverage, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_4 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_4, 0, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_8, 1, wx.EXPAND, 0)

        label_5 = wx.StaticText(self.Settings, wx.ID_ANY, "Profit %")
        label_5.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_5.SetForegroundColour(wx.Colour(255, 255, 255))
        label_5.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(label_5, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.profitcent = wx.TextCtrl(self.Settings, wx.ID_ANY, str(sj["profit_percent"]))
        self.profitcent.SetMinSize((222, 33))
        sizer_8.Add(self.profitcent, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_5 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_5, 0, wx.EXPAND, 0)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_9, 1, wx.EXPAND, 0)

        label_6 = wx.StaticText(self.Settings, wx.ID_ANY, "Margin Type")
        label_6.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_6.SetForegroundColour(wx.Colour(255, 255, 255))
        label_6.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_9.Add(label_6, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)
        self.choices2 = ["ISOLATED", "CROSS"]
        self.margin_type = wx.Choice(self.Settings, wx.ID_ANY, choices=self.choices2)
        self.margin_type.SetMinSize((360, 35))
        current_selection = self.choices2.index(sj["margin_type"])
        self.margin_type.SetSelection(current_selection)
        sizer_9.Add(self.margin_type, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_6 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_6, 0, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_10, 1, wx.EXPAND, 0)

        label_7 = wx.StaticText(self.Settings, wx.ID_ANY, "Exit Switch")
        label_7.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_7.SetForegroundColour(wx.Colour(255, 255, 255))
        label_7.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_10.Add(label_7, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.exit_tgl = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.exit_tgl.SetMinSize((222, 20))
        self.exit_tgl.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.exit_tgl.SetForegroundColour(wx.Colour(0, 0, 0))
        self.exit_tgl.SetBitmap(wx.Bitmap("../assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        self.exit_tgl.SetBitmapPressed(
            wx.Bitmap("../assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        sizer_10.Add(self.exit_tgl, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.SHAPED, 121)
        if sj["exit_switch"] == "t":
            self.exit_tgl.SetValue(True)
        else:
            self.exit_tgl.SetValue(False)
        static_line_7 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_7, 0, wx.EXPAND, 0)

        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_11, 1, wx.EXPAND, 0)

        label_8 = wx.StaticText(self.Settings, wx.ID_ANY, "Long Switch")
        label_8.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_8.SetForegroundColour(wx.Colour(255, 255, 255))
        label_8.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_11.Add(label_8, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.long_tgl = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.long_tgl.SetMinSize((222, 20))
        self.long_tgl.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.long_tgl.SetForegroundColour(wx.Colour(0, 0, 0))
        self.long_tgl.SetBitmap(wx.Bitmap("../assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        self.long_tgl.SetBitmapPressed(wx.Bitmap("../assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        sizer_11.Add(self.long_tgl, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.SHAPED, 121)

        if sj["long_switch"] == "t":
            self.long_tgl.SetValue(True)
        else:
            self.long_tgl.SetValue(False)

        static_line_8 = wx.StaticLine(self.Settings, wx.ID_ANY)
        sizer_3.Add(static_line_8, 0, wx.EXPAND, 0)

        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_12, 1, wx.EXPAND, 0)

        label_9 = wx.StaticText(self.Settings, wx.ID_ANY, "Short Switch")
        label_9.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_9.SetForegroundColour(wx.Colour(255, 255, 255))
        label_9.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_12.Add(label_9, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.short_tgl = wx.ToggleButton(self.Settings, wx.ID_ANY, "")
        self.short_tgl.SetMinSize((222, 20))
        self.short_tgl.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.short_tgl.SetForegroundColour(wx.Colour(0, 0, 0))
        self.short_tgl.SetBitmap(wx.Bitmap("../assets/toggle_btn(0).png", wx.BITMAP_TYPE_ANY))
        self.short_tgl.SetBitmapPressed(
            wx.Bitmap("../assets/toggle_btn(1).png", wx.BITMAP_TYPE_ANY))
        sizer_12.Add(self.short_tgl, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT | wx.SHAPED, 121)

        if sj["short_switch"] == "t":
            self.short_tgl.SetValue(True)
        else:
            self.short_tgl.SetValue(False)

        self.credentials = wx.Panel(self.backpanel, wx.ID_ANY)
        self.credentials.Hide()
        self.backpanel.AddPage(self.credentials, "     Credentials     ")

        sizer_13 = wx.BoxSizer(wx.VERTICAL)

        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)

        label_10 = wx.StaticText(self.credentials, wx.ID_ANY, "Webhook URL")
        label_10.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_10.SetForegroundColour(wx.Colour(255, 255, 255))
        label_10.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_14.Add(label_10, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.webhook_url = wx.TextCtrl(self.credentials, wx.ID_ANY, sj["webhook_url"])
        # self.webhook_url = wx.TextCtrl(self.credentials, wx.ID_ANY, sj["webhook_url"], style=wx.TE_READONLY)

        self.webhook_url.SetMinSize((222, 33))
        sizer_14.Add(self.webhook_url, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_9 = wx.StaticLine(self.credentials, wx.ID_ANY)
        sizer_13.Add(static_line_9, 0, wx.EXPAND, 0)

        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(sizer_15, 1, wx.EXPAND, 0)

        label_11 = wx.StaticText(self.credentials, wx.ID_ANY, "API Key")
        label_11.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_11.SetForegroundColour(wx.Colour(255, 255, 255))
        label_11.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_15.Add(label_11, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.api_key = wx.TextCtrl(self.credentials, wx.ID_ANY, cj["api_key"])
        self.api_key.SetMinSize((222, 33))
        sizer_15.Add(self.api_key, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_10 = wx.StaticLine(self.credentials, wx.ID_ANY)
        sizer_13.Add(static_line_10, 0, wx.EXPAND, 0)

        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(sizer_16, 1, wx.EXPAND, 0)

        label_12 = wx.StaticText(self.credentials, wx.ID_ANY, "API Secret")
        label_12.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_12.SetForegroundColour(wx.Colour(255, 255, 255))
        label_12.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_16.Add(label_12, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.api_secret = wx.TextCtrl(self.credentials, wx.ID_ANY, cj["api_secret"])
        self.api_secret.SetMinSize((222, 33))
        sizer_16.Add(self.api_secret, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        static_line_11 = wx.StaticLine(self.credentials, wx.ID_ANY)
        sizer_13.Add(static_line_11, 0, wx.EXPAND, 0)

        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13.Add(sizer_17, 1, wx.EXPAND, 0)

        label_13 = wx.StaticText(self.credentials, wx.ID_ANY, "TLD")
        label_13.SetBackgroundColour(wx.Colour(0, 0, 0))
        label_13.SetForegroundColour(wx.Colour(255, 255, 255))
        label_13.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_17.Add(label_13, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 117)

        self.tld = wx.TextCtrl(self.credentials, wx.ID_ANY, cj["tld"])
        self.tld.SetMinSize((222, 33))
        sizer_17.Add(self.tld, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 117)

        bottom_pane = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(bottom_pane, 0, wx.EXPAND, 0)

        bottom_pane.Add((20, 25), 4, wx.EXPAND, 0)

        self.start_btn = wx.Button(self.panel_1, wx.ID_ANY, "START", style=wx.BORDER_NONE)
        self.start_btn.SetMinSize((48, 30))
        bottom_pane.Add(self.start_btn, 1, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.RIGHT | wx.TOP, 13)

        self.save_btn = wx.Button(self.panel_1, wx.ID_ANY, "SAVE", style=wx.BORDER_NONE)
        self.save_btn.SetMinSize((48, 30))
        bottom_pane.Add(self.save_btn, 1, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 13)

        self.credentials.SetSizer(sizer_13)

        self.Settings.SetSizer(sizer_3)

        self.watchlist.SetSizer(self.sizer_19)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.exit_btn_clicked, self.exit_button)
        self.Bind(wx.EVT_BUTTON, self.add_btn_pressed, self.add_btn)
        self.Bind(wx.EVT_BUTTON, self.start_button_clicked, self.start_btn)
        self.Bind(wx.EVT_BUTTON, self.save_button_clicked, self.save_btn)
        # end wxGlade

    def exit_btn_clicked(self, event):  # wxGlade: MyFrame.<event_handler>
        self.Close()
        event.Skip()

    def add_btn_pressed(self, event):  # wxGlade: MyFrame.<event_handler>
        frame = MyDialog(None, wx.ID_ANY, "")
        frame.Show()
        # sizer11=wx.BoxSizer(wx.)
        # label_24 = wx.StaticText(self.watchlist_pnl, wx.ID_ANY, "Variance Pvt. Ltd.")
        # self.sizer19.Add(label_24, 0, wx.LEFT, 14)
        event.Skip()

    def start_button_clicked(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.start_btn.GetLabel() == "START":
            ################## starting bot begin###################
            # main.main.main()
            ################## starting bot end ###################
            self.start_btn.SetLabel("STOP")
        else:
            # TODO: implemented to stop bot here.
            self.start_btn.SetLabel("START")
        event.Skip()

    def save_button_clicked(self, event):  # wxGlade: MyFrame.<event_handler>
        with open('../json/settings.json') as settings_j:
            sjtemp = json.load(settings_j)
        with open('../json/credentials.json') as credentials_j:
            cjtemp = json.load(credentials_j)

        sjtemp['timeframe'] = self.choices9[self.time_frame.GetSelection()]
        sjtemp['ema1'] = self.ema1.GetValue()
        sjtemp['ema2'] = self.ema2.GetValue()
        sjtemp['leverage'] = int(self.leverage.GetValue())
        sjtemp['profit_percent'] = int(self.profitcent.GetValue())
        sjtemp['margin_type'] = self.choices2[self.margin_type.GetSelection()]

        # exit switch
        if self.exit_tgl.GetValue():
            sjtemp['exit_switch'] = "t"
        else:
            sjtemp['exit_switch'] = "f"
        # long switch
        if self.long_tgl.GetValue():
            sjtemp['long_switch'] = "t"
        else:
            sjtemp['long_switch'] = "f"
        # short switch
        if self.short_tgl.GetValue():
            sjtemp['short_switch'] = "t"
        else:
            sjtemp['short_switch'] = "f"

        # credentials
        sjtemp['webhook_url'] = self.webhook_url.GetValue()
        cjtemp['api_key'] = self.api_key.GetValue()
        cjtemp['api_secret'] = self.api_secret.GetValue()
        cjtemp['TLD'] = self.tld.GetValue()
        with open('../json/settings.json', 'w') as setjson:
            json.dump(sjtemp, setjson)
        with open('../json/credentials.json', 'w') as credjson:
            json.dump(cjtemp, credjson)

        ################## update_settings ###################
        # main.main.update_settings()
        ################## update_settings end ###############

        self.webhook_url.SetEditable(False)
        self.api_key.SetEditable(False)
        self.api_secret.SetEditable(False)
        self.tld.SetEditable(False)

        # end of class MyFrame

    def add_watchlist_now(self, title, base, quote):
        # add obj to watchlist_pnl
        # app.frame.sizer_19.Add(Watchlist_Item.mark(app.frame.watchlist,title,base,quote), 1, wx.EXPAND, 0)

        sjtemp["watchlist"][title] = {}
        sjtemp["watchlist"][title]["base_asset"] = base
        sjtemp["watchlist"][title]["quote_asset"] = quote
        with open('../json/settings.json', 'w') as setjson:
            json.dump(sjtemp, setjson)





class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((469, 350))
        self.SetTitle("Add to Watchlist")
        self.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.SetForegroundColour(wx.Colour(255, 255, 255))

        back_sizer = wx.BoxSizer(wx.VERTICAL)

        top_pane = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Variance Pvt. Ltd."), wx.HORIZONTAL)
        back_sizer.Add(top_pane, 1, wx.EXPAND, 0)

        label_14 = wx.StaticText(self, wx.ID_ANY, "Add to Watchlist")
        label_14.SetMinSize((180, 32))
        label_14.SetForegroundColour(wx.Colour(255, 255, 255))
        label_14.SetFont(wx.Font(13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        top_pane.Add(label_14, 0, wx.LEFT, 14)

        top_pane.Add((20, 20), 5, wx.EXPAND, 0)

        self.exit_button = wx.Button(self, wx.ID_CANCEL, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.exit_button.SetMinSize((32, 32))
        self.exit_button.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.exit_button.SetBitmap(wx.Bitmap("../assets/close.png", wx.BITMAP_TYPE_ANY))
        top_pane.Add(self.exit_button, 0, 0, 0)

        content_grid = wx.GridSizer(3, 2, 0, 0)
        back_sizer.Add(content_grid, 6, wx.EXPAND, 0)

        label_1 = wx.StaticText(self, wx.ID_ANY, "Title")
        label_1.SetForegroundColour(wx.Colour(255, 255, 255))
        label_1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        content_grid.Add(label_1, 0, wx.ALIGN_CENTER, 0)

        self.title = wx.TextCtrl(self, wx.ID_ANY, "")
        self.title.SetMinSize((133, 33))
        content_grid.Add(self.title, 0, wx.ALIGN_CENTER, 0)

        label_2 = wx.StaticText(self, wx.ID_ANY, "Base Asset")
        label_2.SetForegroundColour(wx.Colour(255, 255, 255))
        label_2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        content_grid.Add(label_2, 0, wx.ALIGN_CENTER, 0)

        self.base_asset = wx.TextCtrl(self, wx.ID_ANY, "")
        self.base_asset.SetMinSize((133, 33))
        content_grid.Add(self.base_asset, 0, wx.ALIGN_CENTER, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "Quote Asset")
        label_3.SetForegroundColour(wx.Colour(255, 255, 255))
        label_3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        content_grid.Add(label_3, 0, wx.ALIGN_CENTER, 0)

        self.quote_asset = wx.TextCtrl(self, wx.ID_ANY, "")
        self.quote_asset.SetMinSize((133, 33))
        content_grid.Add(self.quote_asset, 0, wx.ALIGN_CENTER, 0)

        sizer_2 = wx.StdDialogButtonSizer()
        back_sizer.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 9)

        self.button_OK = wx.Button(self, wx.ID_OK, "", style=wx.BORDER_NONE)
        self.button_OK.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.button_OK.SetForegroundColour(wx.Colour(218, 218, 218))
        self.button_OK.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.button_OK.SetDefault()
        sizer_2.AddButton(self.button_OK)

        sizer_2.Realize()

        self.SetSizer(back_sizer)

        self.SetAffirmativeId(self.button_OK.GetId())
        self.SetEscapeId(self.exit_button.GetId())

        self.Layout()
        self.Centre()
        self.Bind(wx.EVT_BUTTON, self.button_OK_clicked, self.button_OK)
        # end wxGlade

    def button_OK_clicked(self, event):
        MyFrame.add_watchlist_now(self, title=self.title.GetValue(), base=self.base_asset.GetValue(),
                                  quote=self.quote_asset.GetValue())
        event.Skip()


# end of class MyDialog


# end of class Watchlist_Item

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
