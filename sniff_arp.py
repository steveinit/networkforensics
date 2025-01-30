# Sniffs ARPs for 50 lines
import scapy.all as scapy

interface = "interface" # replace interface with hardware (eth0|wlan0|etc)
packets_to_sniff = 1

def print_packet(pkt):
   print(f"Source MAC: {pkt[scapy.Ether].src}")
   print(f"Dest MAC: {pkt[scapy.Ether].dst}")
   print(f"ARP source MAC: {pkt[scapy.ARP].hwsrc}")
   print(f"Operation: {pkt[scapy.ARP].op}")
   print("-" * 50)

interface_traffic = scapy.sniff(
   iface=interface,
   count=packets_to_sniff,
   filter="arp",
   prn=print_packet
)