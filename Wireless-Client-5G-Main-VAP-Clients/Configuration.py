
# Output log Directory
Log_Directory = "Build_Version"

# List of urls to ping
url_list = ["192.168.0.1", "192.168.0.100", "192.168.0.110", "www.google.com", "www.yahoo.com"]

# number of ping packets to ping in windows only for hrping.
ping_packets = "6000"

# iperf command list
iperf_list = ["iperf -c 192.168.0.110 -i 1 -w 512K -P 3 -t 9999999",
"iperf -u -s -B 239.1.1.1 -i 5"]

# vlc_url open a multicast stream
vlc_url = "rtp://@239.0.0.1:5004"

# vlc command to open the vlc playrer
vlc_command = "vlc -vvv " + vlc_url

# list of youtube urls to open
Youtube_url_list = ["https://www.youtube.com/watch?v=xT2ZOZhn5yQ"]

#Browser code to open a specific browser
# ex: 0 for Chrome
#     1 for Firefox
#     other values open Internet Explorer
browsercode = '0'

#Path to the web Browser in windows only.
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
mozilla_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
internetexplorer_path = "C:\\Program Files\\Internet Explorer\\iexplore.exe"

# List of torrent file paths to download.
torrentFiles = ["C:\\Users\\dvenk\\Downloads\\Minions (2015) [1080p] [BluRay] [YTS.MX].torrent"]

# Torrent Web UI UserName and Password and Port.
torrentAdmin = "admin"
torrentPassword = "admin"
torrentPort = "8048"

# utorrent path in windows.
utorrent_path = "C:\\Users\\dvenk\\AppData\\Roaming\\uTorrent\\uTorrent.exe"
