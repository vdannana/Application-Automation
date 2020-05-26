import os
from sys import platform

import Common_Function as cf
import Configuration as conf

# Creating a Directory to store Log Files
if not os.path.exists(conf.Log_Directory):
    os.mkdir(conf.Log_Directory)
    print("Directory ", conf.Log_Directory,  " Created ")
else:
    print("Directory ", conf.Log_Directory,  " already exists")

# Creating list of ping commands
lis = []
for addr in conf.url_list:
    File_Name = conf.Log_Directory + "/" + "Log_" + addr + ".txt"
    if platform == "linux" or platform == "linux2":
        ping_cmd = "ping " + addr + "|./Requirements/TimeStamp.sh|tee " + File_Name
    elif platform == "win32":
        ping_cmd = "hrping -n " + conf.ping_packets + " -T -F " + File_Name + " " + addr    
    lis.append(ping_cmd)

# Pinging GW and the websites
cf.command_execution(lis)

# Exexcuting ipref commands
cf.command_execution(conf.iperf_list)

# Opening VLC given VLC in Environ Path
cf.command_execution([conf.vlc_command])

# Opening youtube
cf.openBrowser(conf.Youtube_url_list, conf.browsercode)
