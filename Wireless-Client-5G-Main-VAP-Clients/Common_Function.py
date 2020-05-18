import Configuration as conf
import subprocess
import webbrowser
import os
import urllib.request
from sys import platform
from utorrentapi import UTorrentAPI
from utorrentapi import TorrentListInfo

def execution(cmd_list):
    for i in cmd_list:
        print(i)
        p = subprocess.Popen(["start", "cmd", "/k", i], shell=True)
        p_staus = p.wait()
        print(p_staus)
    return(True)

def openBrowser(sitelist, browsercode):
    if browsercode == '0':
        if platform == "linux" or platform == "linux2":
            try:
                c = webbrowser.get('google-chrome')
            except:
                print("Chrome Browser is not installed in your linux machine")
                return(False)
        elif platform == "win32":
            if os.path.isfile(conf.chrome_path):
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(conf.chrome_path))
                c = webbrowser.get('chrome')
            else:
                print("Chrome Browser is not installed in your windows machine or not installed at default location")
                return(False)
    elif browsercode == '1':
        if platform == "linux" or platform == "linux2":
            try:
                c = webbrowser.get('firefox')
            except:
                print("FireFox Browser is not installed in your linux machine")
                return(False)
        elif platform == "win32":
            if(os.path.isfile(conf.mozilla_path)):
                webbrowser.register('mozilla', None, webbrowser.BackgroundBrowser(conf.mozilla_path))
                c = webbrowser.get('mozilla')
            else:
                print("FireFox Browser is not installed in your windows machine or not installed at default location")
                return(False)
    else:
        if platform == "linux" or platform == "linux2":
            print("Invalid Input")
            print("In Linux only Firefox and Chrome available try 0 for chrome or 1 for firefox")
            return(False)
        elif platform == "win32":
            if(os.path.isfile(conf.internetexplorer_path)):
                webbrowser.register('iexplorer', None, webbrowser.BackgroundBrowser(conf.internetexplorer_path))
                c = webbrowser.get('iexplorer')
            else:
                print("internet Explorer is not installed in your windows machine or not installed at default location")
                return(False)

    for site in sitelist:
        try:
            if not c.open_new(site):
                raise webbrowser.Error
            else:
                try:
                    temp = urllib.request.urlopen(site).getcode()
                    print(site+" : ", temp)
                except Exception as e:
                    print(site+" : ", e)
        except webbrowser.Error:
            print(format(site))
    return(True)

def torrentHandler(torrent_lst):
    if(os.path.isfile(conf.utorrent_path)):
        subprocess.Popen([conf.utorrent_path])
    else:
        print("utorrent is not installed on your machine")
        return(False)
    apiclient = UTorrentAPI('http://127.0.0.1:'+conf.torrentPort+'/gui', conf.torrentAdmin, conf.torrentPassword)
    data = apiclient.get_list()
    tor_list = TorrentListInfo(data)
    for i in tor_list.torrents:
        apiclient.removedata(i.hash)
        print('Torrent ' + i.name + ' is removed')
    for item in torrent_lst:
        if(os.path.isfile(item):
            apiclient.add_file(item)
        else:
            print('Torrent file ' + item + ' is not found on your machine')
    return(True)
