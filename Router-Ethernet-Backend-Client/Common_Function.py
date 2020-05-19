import Configuration as conf
import subprocess
import webbrowser
import os
import urllib.request
from sys import platform

'''
command_exection funtion execute windows commands in a new command prompt window
or a unix commands in a new tab of the terminal.
input arugumenet cmd_list is list of command to be executed.
'''
def command_execution(cmd_list):
    for i in cmd_list:
        if platform == "linux" or platform == "linux2":
            p = subprocess.Popen(["start", "cmd", "/k", i], shell=True)
        elif platform == "win32":
            p = subprocess.Popen(["start", "cmd", "/k", i], shell=True)   
        p_staus = p.wait()
        print(p_staus)


'''
    openBrowser function open web sites in a browser
    The argumntes
    sitelist takes list of site urls
    browsercode takes a integer which represents a specific browser
        ex: 0 for Chrome
            1 for Firefox
            other values open Internet Explorer 
'''
def openBrowser(sitelist, browsercode):
    if browsercode == 0:
        if platform == "linux" or platform == "linux2":
            try:
                c = webbrowser.get('google-chrome')
            except:
                print("Chrome Browser is not installed in your linux machine")
                return(-1)
        elif platform == "win32":
            if os.path.isfile(conf.chrome_path):
                webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(conf.chrome_path))
                c = webbrowser.get('chrome')
            else:
                print("Chrome Browser is not installed in your windows machine or not installed at default location")
                return(-1)
    elif browsercode ==1:
        if platform == "linux" or platform == "linux2":
            try:
                c = webbrowser.get('firefox')
            except:
                print("FireFox Browser is not installed in your linux machine")
                return(-1)
        elif platform == "win32":
            if(os.path.isfile(conf.mozilla_path)):
                webbrowser.register('mozilla', None,webbrowser.BackgroundBrowser(conf.mozilla_path))
                c= webbrowser.get('mozilla')
            else:
                print("FireFox Browser is not installed in your windows machine or not installed at default location")
                return(-1)
    else:
        if platform == "linux" or platform == "linux2":
            print("Invalid Input")
            print("In Linux oly Firefox and Chrome available try 0 for chrome or 1 for firefox")
            return(-1)
        elif platform == "win32":
            if(os.path.isfile(conf.internetexplorer_path)):
                webbrowser.register('iexplorer', None,webbrowser.BackgroundBrowser(conf.internetexplorer_path))
                c= webbrowser.get('iexplorer')
            else:
                print("internet Explorer is not installed in your windows machine or not installed at default location")
                return(-1)

    for site in sitelist:
        try:
            if not c.open_new(site):
                raise webbrowser.Error
            else:
                try:
                    temp = urllib.request.urlopen(site).getcode()
                    print(site+" : ",temp)
                except Exception as e:
                    print(site+" : ",e)
        except webbrowser.Error:
            print(format(site))
