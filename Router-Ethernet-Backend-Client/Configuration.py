from sys import platform

# Output log Directory
Log_Directory = "Build_Version"

# List of urls to ping
url_list = ["192.168.1.1", "www.google.com", "www.yahoo.com"]

# number of ping packets to ping in windows only for hrping.
ping_packets = "6000"

#iperf command list
iperf_list = ["iperf -s -i 1 -w 512K",
"iperf -s -i 1 -w 512K -p 5002",
"iperf -s -i 1 -w 512K -p 5003",
"iperf -s -i 1 -w 512K -p 5004",
"iperf -u -c 239.1.1.1 -i 5 -t 9999999"]

# Please specifie path to the video.
# Linux File path Syntax file:///path/file
# Windows File path Syntax C:\\sample.mkv
vlc_file_path = "file:////home/venkat/Videos/sample.mkv"

#create a vlc command specific to platform.
if platform == "linux" or platform == "linux2":
    vlc_command = "vlc -vvv --loop " + vlc_file_path + " --sout '#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=rtp{dst=239.0.0.1,port=5004,mux=ts},dst=display}' :sout-all :sout-keep"
elif platform == "win32":
    vlc_command = "vlc -vvv --loop " + vlc_file_path + " --sout #transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=rtp{dst=239.0.0.1,port=5004,mux=ts},dst=display} :sout-all :sout-keep"

# list of youtube urls to open
Youtube_url_list = ["https://www.youtube.com/watch?v=xT2ZOZhn5yQ"]

#Browser code to open a specific browser
# ex: 0 for Chrome
#     1 for Firefox
#     other values open Internet Explorer
browsercode = 1

#Path to the web BBrowser in windows only.
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
mozilla_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
internetexplorer_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
