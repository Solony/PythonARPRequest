from scapy.all import *
from datetime import datetime

print("Scnning...")

start_time = datetime.now()
answered, unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="hostIP"), timeout=2, verbose=0)

print("\n\tMAC\t\nIP\n")
for snd, rcv in answered:
  print(rcv.sprintf("%Ether.src% - %ARP.psrc%"))

stop_time = datetime.now()
total_time = stop_time - start_time
print("\nScan completed")
print("\nDuration: %s" %(total_time))
