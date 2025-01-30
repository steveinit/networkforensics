# Send in ARP packet - Also in simple_arp.py
send( Ether(dst="destination_mac_address")/ARP(op="who-has", psrc="gateway", pdst="destinationIP"),
      inter=RandNum(10,40), loop=1 )

