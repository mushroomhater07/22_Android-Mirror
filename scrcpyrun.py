"""
This module includes all consts used in this project

0 -->  "KEYCODE_UNKNOWN" 
1 -->  "KEYCODE_MENU" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"
"""
import tkinter as tk
import webbrowser;import subprocess;import os;import time;import io;import threading
from tkinter import COMMAND, messagebox, filedialog, simpledialog, ttk
import keyboard

currdir = os.getcwd()

def getscrcpylocation() :
    answer = messagebox.askyesno(title='Mirror your phone',message='Did you download scrcpy?')
    if answer:
        print("good")
    else:
        messagebox.showinfo("Download", "Download the file: scrcpy for win32/64 .zip and unzip it")
        webbrowser.open_new('https://github.com/Genymobile/scrcpy/releases')
    filename = filedialog.askopenfilename(title='Locate scrcpy.exe',   initialdir='/',        filetypes=(('scrcpy execute file', 'scrcpy.exe'),('scrcpy execute file', 'scrcpy.exe')))
    if len(filename) > 0:
        write = open("config.txt", "wt")
        write.write(filename)
        write.close()
        return filename
    else:
        getscrcpylocation()

def runscrcpy():
    os.system(f'cmd /c "{adblocation}" devices')
    os.system(f'cmd /c "{scrcpylocation}"')

def switchToWired():
    os.system(f'cmd /c "{adblocation}" usb')
    RunWithController()
def RunWithController():
    selection = messagebox.askyesno("","Start with contoller?")
    if selection:
        worker = threading.Thread(target=runscrcpy)
        worker.start()
        adbcontoller()
    else:
        runscrcpy()
def adbcontoller():
    tk.Tk().withdraw()
    #just copy
    #copy finish
    app = tk.Tk()
    app.geometry("380x180")
    app.title('Scrcpy Controller')
    #app.resizable(0, 0)

    # configure the grid
    app.columnconfigure(5, weight=1)
    app.columnconfigure(5, weight=3)


    a00 = ttk.Button(app, text="TAB", command = TABbutton)
    a00.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)
    a01 = ttk.Button(app, text="left", command = leftbutton)
    a01.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
    a02 = ttk.Button(app, text="Power", command = powerbutton)
    a02.grid(column=0, row=2, sticky=tk.E, padx=5, pady=5)
    a10 = ttk.Button(app, text="Up", command = upbutton)
    a10.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
    a11 = ttk.Button(app, text="Middle", command = midbutton)
    a11.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
    a12 = ttk.Button(app, text="Down", command = downbutton)
    a12.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    a20 = ttk.Button(app, text="Notification", command = notibutton)
    a20.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)
    a21 = ttk.Button(app, text="Right", command = rightbutton)
    a21.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)
    a22 = ttk.Button(app, text="Enter", command = Enterbutton)
    a22.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)
    a03 = ttk.Button(app, text="Home", command = homebutton)
    a03.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)
    a13 = ttk.Button(app, text="menu", command = menubutton)
    a13.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
    a23 = ttk.Button(app, text="Back", command = backbutton)
    a23.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)
    a33 = ttk.Button(app, text="Browser", command = browserbutton)
    a33.grid(column=3, row=3, sticky=tk.E, padx=5, pady=5)
    a30 = ttk.Button(app, text="volup", command = volup)
    a30.grid(column=3, row=0, sticky=tk.E, padx=5, pady=5)
    a31 = ttk.Button(app, text="voldown", command = voldown)
    a31.grid(column=3, row=1, sticky=tk.E, padx=5, pady=5)
    a32 = ttk.Button(app, text="Search", command = searchbutton)
    a32.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)
    a24 = ttk.Button(app, text="Power Option", command = longpress)
    a24.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)
    a34 = ttk.Button(app, text="Install APK", command = installapk)
    a34.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)
    a04 = ttk.Button(app, text="Send string", command = sendmsg)
    a04.grid(column=0, row=4, sticky=tk.E, padx=5, pady=3)
    a14 = ttk.Button(app, text="ADB cmd", command = sendadb)
    a14.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
    app.mainloop()
    #app.after(10, runscrcpy) //start runscrcpy immediately after tkinter app, but lag and no respond cause infinite loop scan

##### Very useless code #######
def powerbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 26')

def longpress():
    os.system(f'cmd /c "{adblocation}" shell input keyevent --longpress KEYCODE_POWER')

def homebutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 3')

def backbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 4')

def volup():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 24')

def voldown():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 25')

def TABbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 61')

def menubutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 82')

def notibutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 83')

def searchbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 84')
def browserbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 64')
def upbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 19')
def downbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 20')
def leftbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 21')
def rightbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 22')
def midbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 23')
def Enterbutton():
    os.system(f'cmd /c "{adblocation}" shell input keyevent 66')
def installapk():
    installfile = filedialog.askopenfilename(title='Locate apk file',   initialdir='/', filetypes=(('android package', '*.apk'),('Whatever', '*.*')))
    if len(installfile) > 0:
        installdetail = os.popen(f'cmd /c ""{adblocation}" install "{installfile}""').read().format()
        messagebox.showinfo("",installdetail)
def sendmsg():
    ask =simpledialog.askstring("Enter String","Press ok to Send")
    if(len(ask) >0):
        os.system(f'cmd /c ""{adblocation}" shell input text "{ask}""')
def sendadb():
    ask =simpledialog.askstring("Enter adb command","(ignore adb/adb.exe) Press ok to send")
    if len(ask) >0:
        os.system(f'cmd /c "{adblocation}" devices')
        print(f'cmd /c ""{adblocation}" {ask}"')
        detail = os.popen(f'cmd /c ""{adblocation}" {ask}"').read().format()
        if len(detail)>0:
            messagebox.showinfo("",detail)
###############################
answer = messagebox.askyesno(title='Mirror your phone',message='Do you want to use previous scrcpy location?')
if answer:
    try:
        read = open("config.txt", "rt")
        scrcpylocation = read.readline()
        read.close()
        
        if len(scrcpylocation.format()) == 0:
            raise Exception
    except:
        messagebox.showwarning("Error", "No previous setting")
        scrcpylocation = getscrcpylocation()
else:
    scrcpylocation = getscrcpylocation()

print(scrcpylocation)
scrcpylocation = scrcpylocation.format()
adblocation = scrcpylocation.replace("scrcpy.exe", "adb.exe")
select = messagebox.askyesno("Connection type","Wireless?")
messagebox.showinfo("","plugin your phone via USB")
os.system(f'cmd /c "{adblocation}" devices')
match select:
    case True:
        while True:
            try:
                os.system(f'cmd /c "{adblocation}" tcpip 5555')
                print("wait 5 second")
                time.sleep(5)   
                
                ipdetail = os.popen(f'cmd /c "{adblocation}" shell ip addr show wlan0').read().format().splitlines()
                ipdetail = str(ipdetail[2])
                break
            except:
                messagebox.showinfo("","plugin your phone via USB")
                os.system(f'cmd /c "{adblocation}" devices')
                pass
        while True:
            try:
                ip = simpledialog.askstring("Wireless Option",f"{ipdetail} \n Enter the ip address: (between inet and /24) ")
                ipcheck = ip.split(".")
                if len(ipcheck) != 4:
                    raise Exception
                elif len(ipcheck)== 4:
                    break
            except:
                messagebox.showwarning("","Invalid ip address")
                pass
        os.system(f'cmd /c "{adblocation}" connect {ip}')
        messagebox.showinfo("","unplug your phone now")
        RunWithController()
    case _:
        os.system(f'cmd /c "{adblocation}" disconnect')
        print("Wired")
        RunWithController()

#pyinstaller --onefile "--windowed" --icon=something.ico yourpython.py
# "--windowed" is optional