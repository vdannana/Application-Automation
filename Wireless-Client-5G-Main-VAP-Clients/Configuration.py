Log_Directory = "Build_Version"
url_list = ["192.168.0.1", "192.168.0.100", "192.168.0.110", "www.google.com", "www.yahoo.com"]
ping_packets = "6000"
iperf_list = ["iperf -c 192.168.0.110 -i 1 -w 512K -P 3 -t 9999999",
"iperf -u -s -B 239.1.1.1 -i 5"]
vlc_url = "rtp://@239.0.0.1:5004"
vlc_command = "vlc -vvv " + vlc_url
web_url_list = ["https://www.youtube.com/watch?v=xT2ZOZhn5yQ"]
browsercode = '0'
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
mozilla_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
internetexplorer_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"
torrentFiles = ["C:\\Users\\dvenk\\Downloads\\Minions (2015) [1080p] [BluRay] [YTS.MX].torrent"]
torrentAdmin = "admin"
torrentPassword = "admin"
torrentPort = "8048"
utorrent_path = "C:\\Users\\dvenk\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
