import Configuration as conf
import commonfunction as cf
import os

# Creating a Directory to store Log Files
if not os.path.exists(conf.Log_Directory):
    os.mkdir(conf.Log_Directory)
    print("Directory ", conf.Log_Directory,  " Created ")
else:
    print("Directory ", conf.Log_Directory,  " already exists")

# Creating list of ping commands
lis = []
for addr in conf.url_list:
    File_Name = conf.Log_Directory + "\\" + "Log_" + addr + ".txt"
    ping_cmd = "hrping -n " + conf.ping_packets + " -T -F " + File_Name + " " + addr
    lis.append(ping_cmd)

# Pinging GW and the websites
cf.execution(lis)

# Exexcuting ipref commands
cf.execution(conf.iperf_list)

# Opening VLC given VLC in Environ Path
cf.execution([conf.vlc_command])

# Opening youtube
cf.openBrowser(conf.web_url_list, conf.browsercode)
