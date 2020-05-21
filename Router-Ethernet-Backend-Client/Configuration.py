Log_Directory = "Build_Version"
url_list = ["192.168.1.1", "www.google.com", "www.yahoo.com"]
ping_packets = "6000"
iperf_list = ["iperf -s -i 1 -w 512K",
"iperf -s -i 1 -w 512K -p 5002",
"iperf -s -i 1 -w 512K -p 5003",
"iperf -s -i 1 -w 512K -p 5004",
"iperf -u -c 239.1.1.1 -i 5 -t 9999999"]
# Please specifie path to the video.
# Linux File path Syntax file:///path/file
# Windows File path Syntax C:\\sample.mkv
vlc_file_path = "file:///home/venkat/Documents/GitHub/sample.mp4"
vlc_command = "vlc -vvv --loop " + vlc_file_path + " --sout '#transcode{vcodec=hevc,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:duplicate{dst=rtp{dst=239.0.0.1,port=5004,mux=ts},dst=display}' :sout-all :sout-keep"
web_url_list = ["https://www.youtube.com/watch?v=xT2ZOZhn5yQ"]
browsercode = 1
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
mozilla_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
internetexplorer_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
