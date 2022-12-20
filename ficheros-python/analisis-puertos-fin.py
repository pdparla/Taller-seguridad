# Importamos los módulos necesarios
from scapy.all import *
import datetime

# Definimos la dirección IP y el rango de puertos que queremos escanear
ip = "192.168.1.1"
puertos = range(1,100)

# Iniciamos el escaneo
for puerto in puertos:
  respuesta = sr1(IP(dst=ip)/TCP(dport=puerto,flags="F"),timeout=10)
  if respuesta != None:
    if respuesta.haslayer(TCP):
      if respuesta.getlayer(TCP).flags == 0x14:
        print("Puerto {}: Abierto".format(puerto))
  else:
    print("Puerto {}: Cerrado o filtrado".format(puerto))