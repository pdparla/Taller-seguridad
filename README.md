# Taller de seguridad 

## [OWASP](https://owasp.org/)

El Open Web Application Security Project® (OWASP) es una fundación sin ánimo de lucro que trabaja para mejorar la seguridad del software. 
Tienen multiples [proyectos](https://owasp.org/projects/), aunque hoy vamos a hablar de dos.

### [OWASP Top 10](https://owasp.org/www-project-top-ten/)

El Top 10 de OWASP es un documento de concienciación estándar para desarrolladores y seguridad de aplicaciones web. Representa un amplio consenso sobre los riesgos de seguridad más críticos para las aplicaciones web.

### [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)

Es una aplicación web de demostración diseñada para ser altamente vulnerable a ataques de seguridad. Se utiliza como una herramienta de formación y evaluación de habilidades en seguridad de la información, y se considera una de las aplicaciones más realistas y desafiantes para probar la seguridad de las aplicaciones web.

Se puede crear el entorno virtualizado mediante [docker](https://github.com/juice-shop/juice-shop#docker-container) o [gitpod](https://gitpod.io/#https://github.com/juice-shop/juice-shop/) entre otras.

La comunidad va creando writeups de los retos, en caso de que querais ver [como se hace](https://pwning.owasp-juice.shop/appendix/solutions.html)

## Python

Lenguaje de programación muy utilizado en el mundo de hacking/redes.

### Ejercicio

¿Cuales son Usuario y password creados nuevos?

- Wireshark -> Ver parte de datos, seguir el flujo de datos tcp.stream eq 1
- Scapy -> ver analizador.py

## Analisis de puertos

Para esto vamos a generar un [distintos tipos de escaneadores](https://www.seguridadyfirewall.cl/2017/12/tecnicas-de-exploracion-tcp-port_21.html)



