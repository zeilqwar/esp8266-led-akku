import time
import requests
from threading import *
from gui_stuff.init_gui import start
from gui_stuff.main_window import start_main
import os

class storage():
    anzahl=20
    ip_val="192.168.178.152"
    list_latenz=["x","x"]

def threading_main_gui():
    # Call work function
    t1 = Thread(target=start_main,args=(storage, ))  #
    t1.start()

def get_ping(ip_val,number,cl):
    w=ip_val.split(".")
    w[-1]=str(int(w[-1])+number)
    ip_val=w[0]+"."+w[1]+"."+w[2]+"."+w[3]
    #re=os.system("ping "+ip_val)
    import subprocess
    a=subprocess.run("ping "+ip_val+" -n 1",capture_output=True,shell=True)
    print(a)
    if("Zielhost nicht erreichbar" in str(a) or "Verloren = 1" in str(a)):
        cl.list_latenz[number]="-"
    else:
        for i in str(a).split(" "):
            if("Zeit=" in i):
                cl.list_latenz[number]=i.replace("Zeit=","").replace("ms","")





# print("start")
# start(storage)
#
# print(storage.anzahl)


# start_main(storage)

threading_main_gui()
for i in range(1000):
    time.sleep(3)
    get_ping("192.168.178.152",0,storage)
