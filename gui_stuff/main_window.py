import wx

class main_frame(wx.Frame):
    def __init__(self):
        global cl
        self.val_lost="1"
        self.cl = cl
        super().__init__(parent=None, title='Hello main frame')

        # variable gui
        size = self.cl.anzahl+1

        self.SetSize((700, size*40))
        self.SetTitle("oh helloooo")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)



        grid_sizer_1 = wx.GridSizer(size, 4, 0, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Adresse:")
        grid_sizer_1.Add(label_1, 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "Spannung:")
        grid_sizer_1.Add(label_2, 0, 0, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Verlorene Anfragen:")
        grid_sizer_1.Add(label_3, 0, 0, 0)

        label_4 = wx.StaticText(self.panel_1, wx.ID_ANY, "Latenz:")
        grid_sizer_1.Add(label_4, 0, 0, 0)

        for i in range(size-1):
            print("jjjj")
            w = self.cl.ip_val.split(".")
            w[-1] = str(int(w[-1]) + i)
            ip_val = w[0] + "." + w[1] + "." + w[2] + "." + w[3]

            name_1 = wx.StaticText(self.panel_1, wx.ID_ANY, ip_val)
            grid_sizer_1.Add(name_1, 0, 0, 0)

            label_5 = wx.StaticText(self.panel_1, wx.ID_ANY, "variable_spannung")
            grid_sizer_1.Add(label_5, 0, 0, 0)

            #locals()["self.label_verloren_"+str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            self.__dict__["label_verloren_"+str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            grid_sizer_1.Add(self.__dict__["label_verloren_"+str(i)], 0, 0, 0)

            self.__dict__["label_ping_" + str(i)] = wx.StaticText(self.panel_1, wx.ID_ANY, "x")
            grid_sizer_1.Add(self.__dict__["label_ping_" + str(i)], 0, 0, 0)




        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.on_timer()

    def on_timer(self):
        try:
            self.label_ping_0.SetLabel(self.cl.list_latenz[0])
        except:
             print("jo")
        wx.CallLater(1000, self.on_timer)


        # end wxGlade

    def init(self, event):  # wxGlade: config_frame.<event_handler>
        self.val_lost=str(int(self.val_lost)+1)
        print(self.val_lost)
        self.label_6.SetLabel(self.cl.list_latenz[0])

        # end wxGlade

# end of class main_frame

class main_frame_init(wx.App):
    def OnInit(self):
        self.frame = main_frame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


def start_main(cll):
    global cl
    cl=cll
    app = main_frame_init()
    #app.frame.cl=cl
    app.MainLoop()

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
