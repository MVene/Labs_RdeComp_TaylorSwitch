# Laboratorio N°4
## Ruteo Dinámico y Sistemas Autonomos.

### Integrantes

- Gastón E. Fernandez
- María L. Guimpelevich
- Karen Y. Robles
- David Trujillo
- Milagros A. Venecia

### Nombre del grupo

 "Taylor Switch"

### Universidad Nacional de Cordoba - FCEFyN

### Cátedra de Redes de computadoras

### Profesores

- Santiago M. Henn
- Facundo N. Oliva Cuneo

#### Información de contacto

- gaston.fernandez@mi.unc.edu.ar
- lujan.guimpelevich@mi.unc.edu.ar
- yesica.robles@mi.unc.edu.ar
- d.trujillo@unc.edu.ar
- milagros.venecia@unc.edu.ar

---

## Desarrollo
### Parte 1.
#### 1. 

- A: 
    - Los sistemas autonomos son grandes redes que forman el internet. Más específicamente, un sistema autonomo (AS) es una gran red, ó grupo de redes que tienen una política de ruteo unificada. \
    De esta manera, al enviar paquetes de datos a través del internet, estos saltan de AS a AS, hasta que alcanzan el AS que contiene su dirección IP de destino. Y los routers dentro de ese AS envía el paquete a la dirección IP.
    - Política de Ruteo:  Una política de ruteo de AS es una lista de direcciones IP del espacio que controla el AS, más una lista del resto de ASes a los que se conecta. Esta información es necesaria para el ruteo de los paquetes a las redes correctas. Los ASes anuncian este informacion al internet usando el _Border Gateway Protocol_(BGP).

- B: 
    - A cada AS se le asigna un número oficial, ó "número de sistema autonomo" (_autonomous system number_(ASN)), similar a cómo cada empresa  de licencia con un único 'número oficial'.
    - Los número de AS ó ASNs, son números únicos de 16 bits entre "1" y "65534", ó de 32 bits entre "131072" and "4294967294". Se presentan en este formato: AS(número).
    - Los ASNs sólo son requeridos para comunicaciones externas con routers inter-redes.
    - Los AS deben cumplir ciertos requisitos previo a que se le asigne un ASN. Debe tener una política de ruteo específica, ser de cierto tamaño y tener más de una conexión a otros ASes.

- C:
    - C.1: Google LLC.
        - Website: google.com
        - ASN: AS15169
        - Dominios Hosteados: 18263694
        - Tipo de ASN: Hosting.
    
    - C.2: Facebook, Inc.
        - Website: facebook.com
        - ASN: AS32934
        - Dominios Hosteados: 419599
        - Tipo de ASN: Business.
    
    - C.3: MIT
        - Website: mit.edu
        - ASN: AS3
        - Dominios Hosteados: 660
        - Tipo de ASN: Education.

- D:
    - Telecom Argentina S.A
    - ASN: AS7303
    - Dominios Hosteados: 27967
    - Tipo de ASN: ISP
    - Asignado: 9/6/2000
    - Protocolos Soportados: IPv4 / IPv6
    - Peers en IPv4: 236
    - Peers en IPv6: 53

2. 

- A:
    - Los ASes anuncian su política de ruteo a otros ASes y routers mediante el _Border Gateway Protocol_(BGP). BGP es el protocolo de ruteo de paquetes de datos entre ASes. Sin esta información de ruteo, los paquetes de información se perderían, ó tomarían demasiado tiempo para llegar a su destino. \
    Cada AS usa BGP para anunciar de qué dirección de IP son responsables, y a qué otros AS están conectados. Los routers BGP toman esta información de los ASes y la ponene en bases de datos llamadas _tablas de ruteo_ para determinar el  camino más rápido de AS a AS. Cuando los paquetes llegan, los routers BGP refieren a sus tablas de ruteo, para determinar a qué AS debe ir el paquete.


- B:
- C:
- D:
- E:
- F:

# Parte II - Simulaciones y análisis
Se implementó una topología de red compuesta por dos Sistemas Autónomos (AS100 y AS200) utilizando Cisco Packet Tracer, con el propósito de configurar y analizar el protocolo BGP (Border Gateway Protocol) para permitir el intercambio de rutas entre ambos AS. La configuración busca simular un escenario de interconexión entre redes independientes, utilizando BGP como protocolo de enrutamiento externo (eBGP).

<p align="center">
<img src="/Practico/Laboratorio4/Imagenes_tp4/11.jpg" ><br>
 <span><i>Imagen 1.Topologia de red</i></span>
</p>

## 1- 
Se investigaron y aplicaron los siguientes comandos clave en la CLI de los routers (Router0 y Router1) con el objetivo de configurar, verificar y analizar el funcionamiento del protocolo BGP:

```bash
show ip bgp summary

```
 Este comando muestra un resumen del estado del protocolo BGP en el router. Es útil para verificar rápidamente:
- Qué vecinos BGP están configurados.
- Si las sesiones están activas (Established).
- Cuántas rutas (prefijos) se han recibido de cada vecino.
- Qué número de AS tiene el router.
- Cuánto tiempo lleva activa cada sesión BGP.
  
<img src="/Practico/Laboratorio4/Imagenes_tp4/1.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/2.jpg" >

*Fragmento que evidencia BGP:*

<img src="/Practico/Laboratorio4/Imagenes_tp4/12.jpg" >

- Router ID: 192.168.1.1 → Identificador único de BGP (generalmente se toma la IP más alta de una interfaz activa si no se configura manualmente).
- Local AS: 100 → Este router pertenece al Sistema Autónomo 100.

<img src="/Practico/Laboratorio4/Imagenes_tp4/13.jpg" >

- Router ID: 192.168.2.1 → Identificador único de BGP 
- Local AS: 200 → Este router pertenece al Sistema Autónomo 200.

```bash
show ip bgp
```
Se utiliza para visualizar la tabla BGP (Border Gateway Protocol). Esta tabla contiene todas las rutas BGP que el router ha aprendido de sus vecinos, así como las rutas locales que está anunciando. Es una herramienta fundamental para diagnosticar y comprender cómo está funcionando el ruteo BGP en la red.

<img src="/Practico/Laboratorio4/Imagenes_tp4/5.jpg" >

- 192.168.1.0/24
  - Es red local del Router0.
  - El next hop es 0.0.0.0 → indica que la red fue originada localmente (por comando network).
  - El weight (32768) indica que es la preferida (es el valor por defecto para rutas locales).
  - El símbolo *> indica que es válida y la mejor ruta.
  - El origen es ? → incompleto (posiblemente redistribuida o configurada sin IGP).

- 192.168.2.0/24
  - Aprendida desde el vecino 10.0.0.2 (Router1).
  - El AS 200 aparece en el camino → muestra que esta red pertenece a otro AS.
  - El origen es i → indica que fue originada en ese router con IGP (probablemente por network).

<img src="/Practico/Laboratorio4/Imagenes_tp4/6.jpg" >

```bash
show ip route bgp
```
Este comando muestra únicamente las rutas que han sido aprendidas mediante el protocolo BGP, filtrando otras rutas (como las estáticas, conectadas, OSPF, etc.).
Muestra:
- Prefijos o redes aprendidas por BGP.
- Next-hop (el próximo salto hacia esa red).
- Métrica BGP (usualmente 20 para eBGP).
- Interfaz de salida.
- Tiempo desde que la ruta fue aprendida.

<img src="/Practico/Laboratorio4/Imagenes_tp4/7.jpg" >

- El router aprendió la red 192.168.2.0/24 (perteneciente al otro AS).
- El tráfico hacia esa red se envía a través del next-hop 10.0.0.2.
- El número [20/0] indica:
  - 20: distancia administrativa para rutas BGP externas (eBGP).
  - 0: métrica (MED, Multi-Exit Discriminator).
- El tiempo muestra cuánto hace que la ruta fue aprendida.

<img src="/Practico/Laboratorio4/Imagenes_tp4/8.jpg" >

```bash
show running-config | section router bgp
```
Muestra la configuración activa del router relacionada con BGP. Incluye el número de sistema autónomo (ASN) local, los vecinos BGP configurados, y las redes que están siendo anunciadas.

<img src="/Practico/Laboratorio4/Imagenes_tp4/3.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/4.jpg" >

```bash
show ip protocols
```
Ofrece una visión general de los protocolos de enrutamiento activos en el router. En el contexto de BGP, muestra el ASN local, los vecinos configurados, los timers y las redes que están siendo anunciadas por el protocolo.

<img src="/Practico/Laboratorio4/Imagenes_tp4/9.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/10.jpg" >

## 2- 
Una vez completada la configuración de BGP y confirmado el correcto intercambio e instalación de rutas en las tablas de enrutamiento de los routers, se procedió a realizar pruebas de conectividad extremo a extremo entre los hosts de ambos Sistemas Autónomos (AS100 y AS200).

Pruebas realizadas:
- Desde AS100 hacia AS200:
  - H0 (192.168.1.2) → H2 (192.168.2.2)
  - H0 (192.168.1.2) → H3 (192.168.2.3)

- Desde AS200 hacia AS100:
  - H3 (192.168.2.3) → H0 (192.168.1.2)
  - H3 (192.168.2.3) → H1 (192.168.1.3)
  - 
<img src="/Practico/Laboratorio4/Imagenes_tp4/14.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/15.jpg" >

En todos los casos, las pruebas de ping fueron exitosas, demostrando que existe conectividad completa entre los dispositivos ubicados en diferentes sistemas autónomos. Esto valida que:
- R0 (AS100) recibió correctamente las rutas BGP hacia las redes 192.168.2.0/24, permitiéndole alcanzar los hosts H2 y H3 en AS200.
- R1 (AS200) recibió correctamente las rutas BGP hacia la red 192.168.1.0/24, lo que le permitió reenviar tráfico hacia los hosts H0 y H1 en AS100.
  
Las rutas aprendidas vía BGP fueron instaladas correctamente en las tablas de enrutamiento principales (RIB) de cada router, lo que habilitó el reenvío de paquetes ICMP entre todos los hosts involucrados.

Esta comprobación confirma que BGP está funcionando correctamente como protocolo de enrutamiento externo, y que la red puede mantener conectividad entre hosts de distintos dominios
  
