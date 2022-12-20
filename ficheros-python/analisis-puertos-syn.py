# Importamos los módulos necesarios
import warnings
from cryptography.utils import CryptographyDeprecationWarning
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=CryptographyDeprecationWarning)
    import logging
    logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
    from scapy.all import *

import datetime

# Definimos la dirección IP y el rango de puertos que queremos escanear
ip = "80-pdparla-tallerseguridad-bjrtl2cwwjk.ws-eu79.gitpod.io"
puertos = [80,443]

# Iniciamos el escaneo
for puerto in puertos:
    # SYN Petición
    respuesta = sr1(IP(dst=ip)/TCP(dport=puerto, flags="S"), timeout=1)
    if respuesta != None:
        if respuesta.haslayer(TCP):
           # SYN/ACK?
            if respuesta.getlayer(TCP).flags == 0x12:
                print("Puerto {}: Abierto".format(puerto))
    else:
        print("Puerto {}: Cerrado o filtrado".format(puerto))
