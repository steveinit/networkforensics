import scapy.all as scapy

# Enter listening interface and count of packets intended to sniff
interface = "interface"
packets_to_sniff = 50


interface_traffic = scapy.sniff(iface=interface, count=packets_to_sniff)
interface_traffic.nsummary()