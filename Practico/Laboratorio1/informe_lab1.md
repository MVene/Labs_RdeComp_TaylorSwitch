# Parte I - Configuración y Análisis de tráfico IPv4/IPv6
**Integrantes**  
- Gastón E. Fernandez
- María L. Guimpelevich
- Karen Y. Robles
- David Trujillo
- Milagros A. Venecia

**Nombre del grupo**
 "Taylor Switch"

**Universidad Nacional de Cordoba - FCEFyN**  

**Cátedra de Redes de computadoras**

**Profesores**
- Santiago M. Henn
- Facundo N. Oliva Cuneo

 **17 de Marzo 2025**  
 
**Información de contacto**
- gaston.fernandez@mi.unc.edu.ar
- lujan.guimpelevich@mi.unc.edu.ar
- yesica.robles@mi.unc.edu.ar
- d.trujillo@unc.edu.ar
- milagros.venecia@unc.edu.ar
---
# Desarrollo

## 1- Marco Teórico

**Dual Stack**  

El término dual stack se refiere a la implementación simultánea de los protocolos IPv4 e IPv6 en una misma infraestructura de red. Esto permite la coexistencia de ambos protocolos, facilitando la transición hacia IPv6 sin perder compatibilidad con dispositivos o servicios que aún operan con IPv4.

El dual stack se logra configurando interfaces de red para que soporten ambas pilas de protocolo, asignando una dirección IPv4 y una dirección IPv6 a cada interfaz. De esta manera, las aplicaciones pueden usar cualquiera de los dos protocolos según lo requieran.

**Protocolos de Comunicación (ARP,NDP e ICMP)** 

- **ARP (Address Resolution Protocol):** Es un protocolo de la capa de red utilizado para resolver direcciones IP en direcciones MAC en redes IPv4. Cuando un dispositivo desea comunicarse con otro en la misma red local, utiliza ARP para descubrir la dirección física asociada a una dirección IP.

- **NDP (Neighbor Discovery Protocol):** Es el protocolo equivalente a ARP en redes IPv6. Además de la resolución de direcciones, NDP realiza tareas adicionales, como la autoconfiguración de direcciones y la detección de duplicados. Utiliza mensajes ICMPv6 para intercambiar información entre dispositivos.

- **ICMP (Internet Control Message Protocol):** Es un protocolo de diagnóstico y control utilizado tanto en IPv4 como en IPv6. Permite la notificación de errores y el envío de mensajes de control, como en el caso de los comandos ping y traceroute. En IPv6, ICMP también incluye funcionalidades adicionales a través de ICMPv6.

**Asignación de Direcciones IP (DHCP)** 

El *Dynamic Host Configuration Protocol (DHCP)* es un protocolo utilizado para asignar direcciones IP de manera dinámica a los dispositivos en una red. En el contexto de dual stack, pueden coexistir dos servicios DHCP:

- **DHCPv4:** Asigna direcciones IPv4 a dispositivos que utilizan este protocolo.

- **DHCPv6:** Realiza la asignación automática de direcciones IPv6, así como otros parámetros de configuración.

**Asignación de Direcciones IP (DHCP)** 

El enrutamiento en redes dual stack implica la coexistencia de rutas IPv4 e IPv6 en los dispositivos de red. Los routers configurados para dual stack manejan ambas pilas simultáneamente, realizando encaminamiento según el tipo de dirección de destino. Para garantizar la conectividad, los routers mantienen tablas de enrutamiento separadas para cada protocolo.

La correcta configuración y monitoreo de las rutas es fundamental para evitar conflictos y asegurar el rendimiento de la red en un entorno híbrido.

## 2-
**Diagrama de red propuesto:**
<p align="center"><img src="/Practico/Laboratorio1/Imagenes_tp1/9.jpg" alt="Diagrama"></p>

**Tabla de asignación de direcciones propuestas:**

![Tabla de asignacion IP](/Practico/Laboratorio1/Imagenes_tp1/10.jpg "Tabla de asignacion")

Para configurar las direcciones IPv4 de los host se ingresó al escritorio de cada uno, y se configuró manualmente al utilizar la aplicación “IP Configuration”. A continuación, se muestra las configuraciones:
<p align="center">
  <img src="/Practico/Laboratorio1/Imagenes_tp1/11.jpg" alt="Imagen 1" width="30%">
  <img src="/Practico/Laboratorio1/Imagenes_tp1/12.jpg" alt="Imagen 2" width="30%">
  <img src="/Practico/Laboratorio1/Imagenes_tp1/18.jpg" alt="Imagen 2" width="30%">
</p>

La configuracion del router se realizó de la siguiente manera:
<img src="/Practico/Laboratorio1/Imagenes_tp1/15.jpg" >
<img src="/Practico/Laboratorio1/Imagenes_tp1/16.jpg" >
<img src="/Practico/Laboratorio1/Imagenes_tp1/17.jpg" >

Mediante el comando ping, se envían paquetes de tipo ICMP y se prueba la conectividad entre los dispositivos los cuales funcionan correctamente:
<p align="center">
<img src="/Practico/Laboratorio1/Imagenes_tp1/13.jpg" >
<img src="/Practico/Laboratorio1/Imagenes_tp1/14.jpg" >
</p>

Se evalua la conectividad entre todos los host enviando 3 (tres) paquetes ICMPv6, utilizando el comando ping para IPv6:
<img src="/Practico/Laboratorio1/Imagenes_tp1/19.jpg" >
<img src="/Practico/Laboratorio1/Imagenes_tp1/20.jpg" >
<img src="/Practico/Laboratorio1/Imagenes_tp1/21.jpg" >

## 3- 

En el contexto de redes, los términos simulador y emulador se refieren a herramientas que permiten la creación y evaluación de topologías de red, pero difieren en su enfoque y grado de realismo.

- *Simuladores:* Reproducen el comportamiento de los dispositivos de red mediante modelos abstractos. No ejecutan el software real de los dispositivos, sino que **imitan** su funcionamiento. Ejemplos de simuladores son Packet Tracer y NS-3. Son ideales para estudiar conceptos teóricos y realizar prácticas educativas, ya que proporcionan un entorno controlado y sencillo de utilizar.

- *Emuladores:* Ejecutan el software real de los dispositivos de red, proporcionando un entorno muy similar al de una red física. Esto permite probar configuraciones reales y diagnosticar problemas de forma más precisa. Ejemplos de emuladores son GNS3 y CORE.

La principal diferencia radica en el nivel de realismo y precisión. Los simuladores son más ligeros y fáciles de usar, pero menos precisos, mientras que los emuladores ofrecen una experiencia cercana a la realidad, aunque requieren más recursos computacionales.

## 4-

<div style="text-align: center;">
Ping desde h1 a h2
</div>

<img src="/Practico/Laboratorio1/Imagenes_tp1/2.png" >


<div style="text-align: center;">
h1 a h3
</div>

<img src="/Practico/Laboratorio1/Imagenes_tp1/3.png" >


<div style="text-align: center;">
h2 a h3
</div>

<img src="/Practico/Laboratorio1/Imagenes_tp1/5.png" >


## 5-
Se configuró la red con IPv6 y se probó la conexión entre las PC<br>

h1 -> h2

![ ](/Practico/Laboratorio1/Imagenes_tp1/5%20-%20h1toh2.JPG "h1 -> h2")

h1 -> h3

![ ](/Practico/Laboratorio1/Imagenes_tp1/5%20-%20h1toh3.JPG "h1 -> h3")

h2 -> h3

![ ](/Practico/Laboratorio1/Imagenes_tp1/5%20-%20h2toh3.JPG "h2 -> h3")

## 6-

Iniciando el tráfico ICMP entre h1 y h2

<img src="/Practico/Laboratorio1/Imagenes_tp1/22.png" >


**a-** 

Cuando un dispositivo necesita comunicarse con otro en la misma red, pero no conoce su dirección MAC, envía una solicitud ARP (**ARP Request**) para averiguarla. El dispositivo destino responde con un **ARP Reply.**

Al iniciar un ping desde **h1 (192.168.1.10)** hacia **h2 (192.168.2.10)**, se pueden observar diferentes tipos de tráfico:

- h1 necesitará enviar el paquete al router porque h2 está en otra red.
- Si h1 no conoce la MAC del router (192.168.1.11), enviará una solicitud ARP al router para obtener su dirección MAC.
- El router responderá con un ARP Reply.
- Una vez que h1 conoce la dirección MAC del router, enviará el paquete ICMP al router, que se encargará de reenviarlo a h2.

<img src="/Practico/Laboratorio1/Imagenes_tp1/23.png" >

---

**b-**

Las direcciones IP que se observan son:

<img src="/Practico/Laboratorio1/Imagenes_tp1/24.png" >

	Source: 192.168.1.10 (h1)
	Destination: 192.168.2.10 (h2)

<img src="/Practico/Laboratorio1/Imagenes_tp1/25.png" >

	Source: 192.168.2.10 (h2)
	Destination: 192.168.1.10 (h1)
 ---

**c-**

El **router** usa su **tabla de enrutamiento** para decidir por qué interfaz reenviar un paquete.

- **h1 (192.168.1.10) quiere comunicarse con h2 (192.168.2.10).**
- **h1 nota que h2 está en otra red** y envía el paquete a su gateway (192.168.1.11, el router).
- **El router revisa su tabla de enrutamiento** y ve que *192.168.2.0/24* está en *GigabitEthernet0/0/1.*
- **El router reenvía el paquete a h2** a través de esa interfaz.

---
**d-**

El switch sirve para interconectar dispositivos en una misma red local (LAN). No tiene IP porque trabaja en la Capa 2 (Enlace de Datos), basándose en direcciones MAC para reenviar tramas.

---
**e-**

El comando arp -a muestra la tabla ARP (Address Resolution Protocol) de un dispositivo. La tabla ARP almacena las asociaciones entre las direcciones IP y las direcciones MAC en una red local.
Se visualiza la tabla ARP para h1.

<img src="/Practico/Laboratorio1/Imagenes_tp1/26.png" >

	192.168.1.11: Es la dirección IP del router en la red de H1.
	00:00:0C:76:62:01: Es la dirección MAC del router.
	Dynamic: Significa que esta entrada se obtuvo mediante una petición ARP automática y no fue configurada manualmente.
h1 ha aprendido la dirección MAC del router porque lo necesita para enviar paquetes fuera de su subred.

---
**f-**

Tabla ARP para el dispositivo h3.

<img src="/Practico/Laboratorio1/Imagenes_tp1/27.png" >

Como h3 no ha intentado comunicarse con otras direcciones IP, no se visualizan entradas en su tabla ARP. Las entradas ARP solo se generan cuando un dispositivo intenta comunicarse con otro en la red y necesita resolver la dirección IP en una dirección MAC.

---
**g-**

<img src="/Practico/Laboratorio1/Imagenes_tp1/28.png" >

La tabla ARP del router contiene las siguientes columnas:

    Protocol: El protocolo de red que utiliza la entrada (en este caso, "Internet" para direcciones IPv4).

    Address: La dirección IP asociada con la dirección MAC correspondiente.

    Age (min): El tiempo en minutos desde que se aprendió la dirección MAC asociada con la dirección IP. Si está en "-" significa que la entrada es estática o recién aprendida.

    Hardware Addr: La dirección MAC asociada con la dirección IP.

    Type: El tipo de la entrada ARP. "ARPA" es un estándar para la resolución de direcciones IP en direcciones MAC en redes Ethernet.

    Interface: La interfaz del router por la que se encuentra la dirección IP.

---
**h-**

Una dirección de broadcast es una dirección especial utilizada para enviar un mensaje a todos los dispositivos dentro de una red específica. En lugar de dirigir el paquete a un solo dispositivo (unicast) o a un grupo específico (multicast), el broadcast permite que todos los hosts en la red lo reciban. 

Son útiles para enviar información a todos los dispositivos dentro de una red sin necesidad de conocer sus direcciones individuales. Su uso principal es en protocolos de descubrimiento y configuración de red.

Cuando un dispositivo quiere comunicarse con otro en la misma red pero no conoce su dirección MAC, envía un mensaje ARP a la dirección broadcast de la red. Algunas aplicaciones o herramientas de red usan broadcast para notificaciones.

---
**i-**

Las direcciones multicast en IPv4 permiten enviar datos a un grupo específico de dispositivos en la red.
En lugar de enviar una copia por cada destinatario (unicast), el emisor envía una sola transmisión, y los dispositivos interesados la reciben. Esto es algo ideal para no colapsar las redes, ni tener que enviar copias de todos los paquetes a todos los clientes.

Algunos protocolos muy populares que se usan con tráfico Multicast:

RTP (Real-time Transport Protocol): es un protocolo a nivel de aplicación que se encarga de transmitir información en tiempo real. También se suele usar junto con el protocolo RTSP (Real-time Streaming Protocol) y también se usa el RTCP (RTP Control Protocol).

Internet Group Management Protocol (IGMP): IGMP gestiona los miembros de los grupos de multidifusión IPv4 y se ejecuta en el extremo de una red de multidifusión. Los hosts utilizan el protocolo IGMP para unirse o abandonar grupos multicast.

Protocol Independent Multicast (PIM): PIM se ejecuta en una red IPv4 y envía datos multicast a dispositivos multicast conectados a miembros del grupo interesados en los datos.

## 7-
**a-**

Durante la comunicación entre **H1 y H3**, se observaron dos tipos de mensajes principales:  

- Neighbor Discovery Protocol (NDP): Se usa en IPv6 para la resolución de direcciones, reemplazando a ARP en IPv4. Permite que los dispositivos descubran la dirección MAC de otros en la red antes de enviar paquetes.  
- ICMPv6: Es el protocolo utilizado para diagnóstico y control en IPv6. En este caso, se observó el envío de paquetes de solicitud y respuesta de ping entre H1 y H3 para verificar la conectividad.  

Antes de que los paquetes ICMPv6 sean enviados, ocurre un proceso NDP donde H1 resuelve la dirección MAC de H3. Una vez completado, los paquetes ICMPv6 pueden viajar entre ambos dispositivos.  

---

**b-**

Sí, NDP reemplaza a ARP en IPv6. Mientras que en IPv4 se usa ARP para obtener la dirección MAC de un dispositivo, en IPv6 se utiliza Neighbor Solicitation (NS) y Neighbor Advertisement (NA) dentro del protocolo NDP.  

Además, NDP incluye funcionalidades adicionales que ARP no tenía, como:  
- Descubrimiento de routers (Router Solicitation y Advertisement).  
- Detección de direcciones duplicadas (DAD - Duplicate Address Detection).  
- Redirección de tráfico optimizada (Redirect Messages).  

---

**c-**

El Neighbor Discovery Protocol (NDP) tiene cinco funciones principales:

1. Resolución de direcciones: Traduce direcciones IPv6 en direcciones MAC usando Neighbor Solicitation (NS) y Neighbor Advertisement (NA).  
2. Detección de routers: Permite que los dispositivos encuentren routers en la red mediante mensajes de Router Solicitation (RS) y Router Advertisement (RA).  
3. Autoconfiguración de direcciones: Permite a los hosts configurarse automáticamente usando la información proporcionada por los routers.  
4. Detección de direcciones duplicadas (DAD): Antes de asignarse una IP, un dispositivo verifica que no esté en uso.  
5. Redirección de tráfico: Un router puede indicar a un host una mejor ruta hacia un destino.  

---

**d-**

En IPv6, el broadcast no existe, ya que genera tráfico innecesario. En su lugar, se usan multicast y anycast:

- Multicast: Un paquete se envía solo a un grupo específico de dispositivos en la red.  
- Anycast: Un paquete se envía a la dirección más cercana dentro de un grupo de dispositivos con la misma IP anycast.  

Así, en IPv6 los dispositivos reciben solo los mensajes que realmente necesitan, mejorando la eficiencia.

---

**e-** ¿Cuál es la diferencia entre las direcciones link-local, unique-local y global? ¿En qué caso usaría cada una? Ejemplificar.

| **Tipo de Dirección IPv6** | **Prefijo** | **Alcance** | **Ejemplo** | **Uso** |
|---------------------------|------------|------------|------------|--------|
| **Link-Local** | `FE80::/10` | Solo en la red local (no se enrutan) | `FE80::1` | Comunicación entre dispositivos en la misma red sin necesidad de configuración. |
| **Unique-Local** | `FC00::/7` | Similar a IPv4 privado (`192.168.x.x`) | `FD12:3456:789A::1` | Redes internas sin conexión a Internet. |
| **Global** | `2000::/3` | Pública, accesible en Internet | `2001:db8::1` | Direcciones asignadas por un ISP para acceso a Internet. |

 Ejemplo de uso:
- Link-Local (`FE80::1`): Un router se comunica con una PC en la misma red.  
- Unique-Local (`FD00::1`): Una empresa usa direcciones privadas para su red interna.  
- Global (`2001:db8::1`): Un servidor web con acceso desde Internet.

# Parte II - Manejo de equipamiento físico, recuperación de contraseñas de equipos de red y establecimiento de red y análisis de tráfico.
## 1-
**Descripción General**

El Cisco Catalyst 2950 es un switch gestionado de configuración fija que proporciona conectividad de 10/100 Mbps con opciones de uplink Gigabit Ethernet. Diseñado para redes de pequeñas y medianas empresas, ofrece características básicas de switching LAN con funcionalidades avanzadas de seguridad y gestión de calidad de servicio (QoS).

**Modelos Disponibles**

- Cisco Catalyst 2950SX-48: 48 puertos 10/100 Mbps con 2 uplinks 1000BASE-SX.
- Cisco Catalyst 2950T-48: 48 puertos 10/100 Mbps con 2 uplinks 10/100/1000BASE-T.
- Cisco Catalyst 2950SX-24: 24 puertos 10/100 Mbps con 2 uplinks 1000BASE-SX.
- Cisco Catalyst 2950-24: 24 puertos 10/100 Mbps.
- Cisco Catalyst 2950-12: 12 puertos 10/100 Mbps.

**Especificaciones Técnicas**

- Capacidad de switching: Hasta 13.6 Gbps.
- Velocidad de reenvío: Hasta 10.1 Mpps.
- Memoria: 16 MB de DRAM y 8 MB de Flash.
- Direcciones MAC: Hasta 8,000 entradas.

**Interfaces de Red:**

- 10BASE-T/100BASE-TX en RJ-45.
- 1000BASE-SX en MT-RJ (según modelo).

**Seguridad**

- IEEE 802.1x: Autenticación por puerto con servidores RADIUS y TACACS+.
- SSHv2: Seguridad en acceso remoto por CLI.
- Private VLAN Edge: Aislamiento de puertos para mejorar la seguridad interna.
- MAC Address Notification: Notificación de cambios en dispositivos conectados.
- Control de acceso basado en MAC para prevenir conexiones no autorizadas.

**Consumo Energético y Dimensiones**

- Consumo: 30W (2950-24) a 45W (2950T-48 y 2950SX-48).
- Dimensiones:

2950SX-24, 2950-24, 2950-12: 1.72 x 17.5 x 9.52 in (4.36 x 44.45 x 24.18 cm).

2950SX-48, 2950T-48: 1.72 x 17.5 x 13 in (4.36 x 44.45 x 33.02 cm).

- Temperatura de operación: 0 a 45°C.
- Peso: 3 kg (2950-24) a 4.8 kg (2950T-48).

**Soporte**

Disponible vía Cisco SMARTnet para actualizaciones y reemplazo avanzado.

## 2- Procedimientos

**a-** 
Conectar el cable serie a RJ-45 al puerto de consola del switch y la otra extremidad a la computadora a través del adaptador serie a USB.
Luego para configurar PUTTY en Linux ejecutamos el siguiente comando:

			sudo putty /dev/ttyUSB0 -serial -sercfg 9600,8,n,1,N
  
**b-** 
Si todo esta correctamente conectado deberiamos ver la consola del Switch Cisco como se muestra a continuación.
Accedemos a las opciones de administración del switch y modificamos claves de acceso.

<img src="/Practico/Laboratorio1/Imagenes_tp1/30.jpeg" >

**c-**
A continuación conectamos dos computadoras al switch para configurar una red y testear conectividad:

PC1 con IP: 192.168.2.10

PC2 con IP: 192.168.2.11

PC2 enviando paquetes ICMP a PC1 con el comando ping

<img src="/Practico/Laboratorio1/Imagenes_tp1/29.jpeg" >

PC1 enviando paquetes ICMP a PC2 con el comando ping

<img src="/Practico/Laboratorio1/Imagenes_tp1/33.jpeg" >

Se observan las tablas ARP de cada PC para confirmar que la comunicación se realizó correctamente y se muestra la asociación entre direcciones IP y direcciones MAC de los dispositivos en la misma red local.

<img src="/Practico/Laboratorio1/Imagenes_tp1/31.jpeg" >

<img src="/Practico/Laboratorio1/Imagenes_tp1/34.jpeg" >

En la siguiente imagen se visualiza la tabla de direcciones MAC del switch, es decir, qué direcciones MAC están aprendidas en qué puertos.

<img src="/Practico/Laboratorio1/Imagenes_tp1/32.jpeg" >

**d-**
El Port Mirroring es una técnica que permite copiar todo el tráfico de uno o más puertos de origen a un puerto de destino. Esto puede resultar muy útil para analizar los flujos de red que transitan por ciertos puertos.

Para configurar un puerto del switch en modo mirroring se siguen los siguientes pasos: 

**1.** Se cambia a modo privilegiado y luego al modo terminal de configuración:

	Switch>enable
	password:
	Switch#configure terminal
	
 
**2.** Luego elegimos el puerto de origen fastEthernet 0/1 y copiamos tanto los paquetes recibidos como los transmitidos (both -ambos).

	
	Switch(config)#monitor session 1 source interface fa 0/1 both
	
 
**3.** Para finalizar la configuración, indicamos a qué puerto de destino queremos duplicar el tráfico proveniente del puerto de origen.

	
	Switch(config)#monitor session 1 destination interface fa0/2
	
 
Verificamos que la configuración este realizada correctamente:

<img src="/Practico/Laboratorio1/Imagenes_tp1/37.png" >

Luego utilizamos el software Wireshark para observar el tráfico entre PC1 Y PC2.

<img src="/Practico/Laboratorio1/Imagenes_tp1/35.jpeg" >

<img src="/Practico/Laboratorio1/Imagenes_tp1/36.jpeg" >

- **Paquetes ARP**: Se observa el intercambio de mensajes ARP entre 192.168.2.10 (PC1) y 192.168.2.11 (PC2), donde un dispositivo solicita la dirección MAC del otro para establecer comunicación.

- **Paquetes ICMP**: Se capturan solicitudes y respuestas de ping (Echo Request y Echo Reply) entre 192.168.2.10 y 192.168.2.11, confirmando la conectividad entre ambos dispositivos.
