# print_packet.py
from scapy.all import *
import io
from contextlib import redirect_stdout

l3 = IP()
l4 = TCP()
packet = l3/l4

p80211 = Dot11() / Dot11Beacon() / Dot11Elt("SSID", "test")


f = io.StringIO()
with redirect_stdout(f):
    print("TCP/IP:")
    ls(packet)
    print("\n802.11:")
    ls(p80211)
    # print("\nall layers:")
    # ls()
out = f.getvalue()

out_file = "packet_listing.txt"
with open(out_file, 'w') as f:
    f.write(out)

print("Packet Listing:", out, sep="\n\n")


