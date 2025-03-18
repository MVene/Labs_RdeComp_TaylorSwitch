# Parte I - Configuración y Análisis de tráfico IPv4/IPv6
**Integrantes**  
- Gaston Fernandez
- Maria Lujan Guimpelevich
- David Trujillo
- Milagros Venecia

**Nombre del grupo**
 "Taylor Switch"

**Universidad Nacional de Cordoba - FCEFyN**  

**Cátedra de Redes de computadoras**

 **17 de Marzo 2025**  

---
# Consignas

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
## 3- 

En el contexto de redes, los términos simulador y emulador se refieren a herramientas que permiten la creación y evaluación de topologías de red, pero difieren en su enfoque y grado de realismo.

- *Simuladores:* Reproducen el comportamiento de los dispositivos de red mediante modelos abstractos. No ejecutan el software real de los dispositivos, sino que **imitan** su funcionamiento. Ejemplos de simuladores son Packet Tracer y NS-3. Son ideales para estudiar conceptos teóricos y realizar prácticas educativas, ya que proporcionan un entorno controlado y sencillo de utilizar.

- *Emuladores:* Ejecutan el software real de los dispositivos de red, proporcionando un entorno muy similar al de una red física. Esto permite probar configuraciones reales y diagnosticar problemas de forma más precisa. Ejemplos de emuladores son GNS3 y CORE.

La principal diferencia radica en el nivel de realismo y precisión. Los simuladores son más ligeros y fáciles de usar, pero menos precisos, mientras que los emuladores ofrecen una experiencia cercana a la realidad, aunque requieren más recursos computacionales.
## 4-
## 5-
## 6-
## 7-





