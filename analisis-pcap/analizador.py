
import warnings
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *




pkts = rdpcap("/workspace/Taller-seguridad/analisis-pcap/rogue_user.pcap")
final_payload: str = ""
for packet in pkts:
    if IP in packet and (packet[IP].src == '192.168.56.101' or packet[IP].dst == '192.168.56.101') and TCP in packet and isinstance(packet[TCP].payload, Raw):
        final_payload += bytes.decode(packet[TCP].payload.load)
        a = packet.show(dump=True)
        print(a)

print(final_payload)
