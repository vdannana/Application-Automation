# Application-Automation<br>
## 1. Router Ethernet Backend Client
  - Ping sessions to GW and Internet (www.google.com, www.yahoo.com).
  - 4 iperf server sessions and one iperf multicast session as below:
      - iperf -s -i 1 -w 512K
      - iperf -s -i 1 -w 512K -p 5002
      - iperf -s -i 1 -w 512K -p 5003
      - iperf -s -i 1 -w 512K -p 5004
      - iperf -u -c 239.1.1.1 -i 5 -t 9999999
  - VLC multicast streaming server.
  - Open YouTube session using browser.
  - All the logs generated should be saved in a single folder with name as Build version.

## 2. Satellite Ethernet Backend Client
  - Ping sessions to GW, Router ETH backend IP, and Internet (www.google.com, www.yahoo.com).
  - iperf server sessions as below:
      - iperf -s -i 1 -w 512K.
      - iperf -c  <Router eth client IP> -i 1 -w 512K -p <one port number per satellite> -P 3 -t 9999999.
      - iperf -u -s -B 239.1.1.1 -I 5.
  - VLC multicast client to receive stream from router eth client.
  - Open YouTube session using browser
  - All the logs generated should be saved in a single folder with name as Build version.

## 3. Wireless Client 5G Main VAP Clients:
  - Ping sessions to GW, Router ETH backend IP, Connected node Ethernet backend ip, and Internet (www.google.com, www.yahoo.com).
  - iperf server sessions as below:
      - iperf -c  <Eth backend client IP> -i 1 -w 512K -P 3 -t 9999999
      - iperf -u -s -B 239.1.1.1 -I 5  (if supports)
  - VLC multicast client to receive stream from router eth client
  - Open YouTube session using browser
  - Need to run torrent client with already downloaded torrent files.
  - All the logs generated should be saved in a single folder with name as Build version.

## 4. Wireless Client 5G Guest VAP Clients:
  - Ping sessions to Internet (www.google.com, www.yahoo.com).
  - Open 2 YouTube sessions using browser
  - Need to run torrent client with already downloaded torrent files.
  - All the logs generated should be saved in a single folder with name as Build version.

## 5.Wireless Client 2.4G Main/Guest VAP Clients:
  - Ping sessions to Internet (www.google.com, www.yahoo.com).
  - Open 2 YouTube sessions using browser
  - Need to run torrent client with already downloaded torrent files.
  - All the logs generated should be saved in a single folder with name as Build version.
