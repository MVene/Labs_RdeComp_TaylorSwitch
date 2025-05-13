# Laboratorio N°4
## Ruteo Dinámico y Sistemas Autónomos.

### Integrantes

- Gastón E. Fernández
- María L. Guimpelevich
- Karen Y. Robles
- David Trujillo
- Milagros A. Venecia

### Nombre del grupo

 "Taylor Switch"

### Universidad Nacional de Córdoba - FCEFyN

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

- A: Sistemas Autónomos (AS).
    - Los sistemas autónomos son grandes redes que forman el internet. Más específicamente, un sistema autónomo (AS) es una gran red, ó grupo de redes que tienen una política de ruteo unificada. \
    De esta manera, al enviar paquetes de datos a través del internet, estos saltan de AS a AS, hasta que alcanzan el AS que contiene su dirección IP de destino. Y los routers dentro de ese AS envía el paquete a la dirección IP.
    - Política de Ruteo:  Una política de ruteo de AS es una lista de direcciones IP del espacio que controla el AS, más una lista del resto de ASes a los que se conecta. Esta información es necesaria para el ruteo de los paquetes a las redes correctas. Los ASes anuncian este información al internet usando el _Border Gateway Protocol_(BGP).

- B: Número de Sistema Autónomo (ASN).
    - A cada AS se le asigna un número oficial, ó "número de sistema autónomo" (_autonomous system number_(ASN)), similar a cómo cada empresa  de licencia con un único 'número oficial'.
    - Los número de AS ó ASNs, son números únicos de 16 bits entre "1" y "65534", ó de 32 bits entre "131072" and "4294967294". Se presentan en este formato: AS(número).
    - Los ASNs sólo son requeridos para comunicaciones externas con routers inter-redes.
    - Los AS deben cumplir ciertos requisitos previo a que se le asigne un ASN. Debe tener una política de ruteo específica, ser de cierto tamaño y tener más de una conexión a otros ASes.

- C: Ejemplos de ASNs de 3 empresas/universidades/organizaciones.
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

- D: La conexión actual es:
    - Telecom Argentina S.A
    - ASN: AS7303
    - Dominios Hosteados: 27967
    - Tipo de ASN: ISP
    - Asignado: 9/6/2000
    - Protocolos Soportados: IPv4 / IPv6
    - Peers en IPv4: 236
    - Peers en IPv6: 53

2. 

- A: Border Gateway Protocol (BGP).
    - Los ASes anuncian su política de ruteo a otros ASes y routers mediante el _Border Gateway Protocol_(BGP). BGP es el protocolo de ruteo de paquetes de datos entre ASes. Sin esta información de ruteo, los paquetes de información se perderían, ó tomarían demasiado tiempo para llegar a su destino. \
    Cada AS usa BGP para anunciar de qué dirección de IP son responsables, y a qué otros AS están conectados. Los routers BGP toman esta información de los ASes y la pone en bases de datos llamadas _tablas de ruteo_ para determinar el  camino más rápido de AS a AS. Cuando los paquetes llegan, los routers BGP refieren a sus tablas de ruteo, para determinar a qué AS debe ir el paquete.

- B: Explicación del BGP
    
    - B.1 Procedimientos Funcionales Del BGP
    - B.1.1: Adquisición de Vecinos.
        - Este proceso ocurre cuando un router BGP intenta establecer una conexión con otro router BGP (llamado peer o vecino).
        - BGP utiliza TCP (puerto 179) para establecer la conexión.
        - Una vez establecida la conexión TCP, se intercambian mensajes OPEN, sí ambos lados aceptan los parámetros intercambiados (como ASN, BGP ID, capacidades), se establece la sesión BGP.
    
    - B.1.2: Detección de vecino alcanzable _(Neighbor Liveness Detection)_
        - Después de establecer la sesión, se envían mensajes KEEPALIVE periódicamente para mantener la conexión activa.
        - Si no se recibe un KEEPALIVE o cualquier otro mensaje en un intervalo (Hold Time), se considera que el vecino está inalcanzable, y se cierra la sesión.
    
    - B.1.3: Detección de red alcanzable _(Reachability Detection)_
        - Los routers BGP intercambian mensajes UPDATE para anunciar o retirar rutas (prefijos de red).
        - Estos anuncios contienen atributos como el AS Path, Next Hop, MED, etc.
        - La tabla BGP se actualiza con la mejor ruta según estos atributos y políticas  de enrutamiento.
        - Cuando una red deja de estar disponible, se envía una actualización con la ruta retirada (withdrawal).

    - B.2: Tipos de Mensajes en BGP:
        - OPEN: Iniciar una conexión BGP, intercambiar parámetros básicos.
        - KEEPALIVE: Confirmar que la conexión sigue activa (se envía periódicamente).
        - UPDATE: Anunciar nuevas rutas o retirar rutas existentes.
        - NOTIFICATION: Señalar errores y cerrar la conexión.

    - B.3: Formato de Paquetes en BGP
        - Cada mensaje BGP tiene una cabecera común de 19 bytes.
        - Marker: 16 bytes, usado para detección de errores (típicamente todos 1s).
        - Lenght: 2 bytes, longitud total del mensaje (mínimo 19 bytes, máximo 4096).
        - Type: 1 byte, tipo de mensaje (OPEN, UPDATE, etc)
  
- C: iBGP y eBGP.
    - C.1: Diferencia entre BGP externo _(eBGP)_ y BGP interno _(iBGP)_
    - C.1.1: BGP Externo _(eBGP)_
        - eBGP: Es el protocolo que se usa para intercambiar información de enrutamiento entre diferentes AS. 
        - Los routers que están en diferentes AS utilizan eBGP para comunicar rutas. 
            - Por ejemplo (basado en la imagen), R1 (AS1) y R2 (AS2) se comunican mediante eBGP.

    - C.1.2: BGP Interno _(iBGP)_
        - iBGP: Es el protocolo que se usa para intercambiar información de enrutamiento dentro de un mismo AS. Los routers que pertenecen al mismo AS utilizan iBGP. 
            - En el ejemplo de la imagen, R2 y R3 (ambos en AS2) usan iBGP para compartir información de rutas aprendidas por eBGP.

    - C.2: Ejemplo.
        ![alt text](/Practico/Laboratorio4/Imagenes_tp4/Punto_2_c.png)

        - Un AS se considera de tránsito sí este permite que otros AS usen su red para pasar hacia otros AS. En este caso, AS2, es un AS de tránsito

- D: Gráfico sobre la conexión de los AS de mí conexión actual (AS7303 - Telecom Argentina S.A.)

    ![alt text](/Practico/Laboratorio4/Imagenes_tp4/AS7303_grafico.png)

    - Se puede ver que AS7303 mantiene 4 conexiones eBGP, con AS3356, AS6762 y AS3257
    
    - Y a uno o dos grados de separación, están los AS, AS6939, AS6453, y AS5511, entre otros.

- E: Conexiones desde eBGP desde un AS diferente. (En este caso, Claro AR 5G)
    - AS11664 - Techtel LMDS Comunicaciones Interactivas S.A.
    - Sus conexiones eBGP son los AS, AS6762, AS1299, AS3257
    - Y uno ó dos grados de separación se encuentran AS174, AS6939, AS3356, entre otros.
    - Se puede observar que comparten ASs

    ![alt text](/Practico/Laboratorio4/Imagenes_tp4/AS11664_grafico.png)

- F: Podría servir de ejemplo el caso del [Hijacking de BGP por parte de Telekom Malaysia.](https://www.bgpmon.net/massive-route-leak-cause-internet-slowdown/)
    - El 12 de junio de 2015, Telekom Malaysia (AS4788) anunció por error, miles de prefijos IP que no le pertenecían, redirigiendo tráfico que debía ir a otros destinos. \
    Y muchos proveedores de Internet aceptaron estos anuncios sin verificar su legitimidad (lo cual es una debilidad inherente al diseño de BGP).
    - Esto provocó una significativa pérdida de paquetes, y el internet disminuyó su velocidad en todas partes del mundo. 

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

Esta comprobación confirma que BGP está funcionando correctamente como protocolo de enrutamiento externo, y que la red puede mantener conectividad entre hosts de distintos dominios.

## 3-
**Simular tráfico en modo Simulation**

Se utilizó la herramienta de simulación de Packet Tracer para enviar un paquete ICMP desde el host PC0 (perteneciente al AS100) hacia el host PC2 (en AS200). En la simulación, se observaron los pasos intermedios del paquete:

<img src="/Practico/Laboratorio4/Imagenes_tp4/16.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/17.jpg" >

- El ping fue enviado desde PC0 y atravesó Switch0, Router0, Router1 y Switch1 hasta llegar a PC2.

- Se registró también el retorno del paquete ICMP (respuesta del ping), volviendo desde PC2 a PC0 por el mismo camino.
  
- Se observaron múltiples paquetes del protocolo BGP intercambiados entre Router0 y Router1. Analizando los eventos capturados en el modo Simulation, se identificaron mensajes del tipo KEEPALIVE, que son enviados periódicamente para mantener la sesión BGP activa. Esto confirma que la conexión BGP entre ambos routers está establecida correctamente.

Esto confirma que el tráfico entre hosts de diferentes AS funciona correctamente y que las rutas BGP están activas.

Se visualizaron también mensajes STP de los switches, lo cual es normal en la simulación de red.

**Se apaga el Router1**

Para simular una falla en la red, se procedió a apagar el router Router1, que actúa como frontera entre los Sistemas Autónomos AS100 y AS200. Esto se realizó desde la pestaña Physical, utilizando el botón de apagado.
Luego de apagar el router, se ejecutó un ping desde PC0 (AS100) hacia PC2 (AS200), observando el tráfico en modo Simulation. El resultado fue el esperado: el tráfico se interrumpió y el paquete ICMP no alcanzó su destino.

<img src="/Practico/Laboratorio4/Imagenes_tp4/18.jpg" >

Para verificar cómo BGP maneja la pérdida de conectividad con un vecino externo. Al ejecutar el comando `show ip bgp` en Router0 (AS 100), se observó que ya no se recibían rutas del vecino BGP, y solo permanecía la red local 192.168.1.0/24.
Asimismo, la tabla de ruteo (`show ip route`) reflejaba únicamente rutas directamente conectadas, sin rutas aprendidas vía BGP.

<img src="/Practico/Laboratorio4/Imagenes_tp4/19.png" >

**Se enciende el Router1**

Una vez encendido Router1 (AS 200), se verificó el restablecimiento de la sesión BGP con Router0 (AS 100). A los pocos segundos, Router0 recibió la red 192.168.2.0/24 mediante BGP.
El comando  `show ip bgp` confirmó la recepción de esta red con origen en AS 200, y el comando `show ip route` mostró correctamente la ruta aprendida por BGP, etiquetada con la letra B, con un next hop de 10.0.0.2.

<img src="/Practico/Laboratorio4/Imagenes_tp4/20.jpg" >

## 4-
- Se activa IPv6 en los routers:

<img src="/Practico/Laboratorio4/Imagenes_tp4/21.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/22.jpg" >


- Se asigna IPv6 en interfaces:

<img src="/Practico/Laboratorio4/Imagenes_tp4/23.jpg" >
<img src="/Practico/Laboratorio4/Imagenes_tp4/24.jpg" >

Se intentó habilitar conectividad dual-stack entre los sistemas autónomos AS100 y AS200 mediante la incorporación de configuración IPv6 en la red. Aunque fue posible asignar direcciones IPv6 a interfaces y hosts, se identificó una limitación importante en Cisco Packet Tracer relacionada con la implementación de BGP para el enrutamiento IPv6.
Limitación de BGP con IPv6 en Packet Tracer: Al configurar la vecindad BGP utilizando direcciones IPv6 (mediante el comando  `neighbor <ipv6-address> remote-as <asn>` dentro del proceso router bgp <asn>), Packet Tracer genera el error `% Invalid input detected`. Esto sugiere que la versión utilizada de Packet Tracer no soporta completamente el establecimiento de sesiones BGP sobre IPv6 de forma directa, o bien requiere un enfoque alternativo —como el uso de address families— que también podría estar restringido en esta plataforma.
En consecuencia, no fue posible establecer el intercambio dinámico de rutas IPv6 entre los routers R0 y R1 utilizando BGP dentro de esta simulación.

## 5-
| **Equipo** | **Interfaz**     | **IP de red** | **IPv4**        | **Máscara**     | **IPv6**              | **Comentarios**                                        |
|------------|------------------|---------------|------------------|------------------|------------------------|---------------------------------------------------------|
| PC0        | FastEthernet0    | 192.168.1.0   | 192.168.1.2      | 255.255.255.0    | 2001:DB8:0:A::2/64       | Host en AS100                                           |
| PC1        | FastEthernet0    | 192.168.1.0   | 192.168.1.3      | 255.255.255.0    | 2001:DB8:0:A::3/64       | Host en AS100                                           |
| Switch0    | -                | -             | -                | -                | -                      | Switch de capa 2 en AS100                               |
| Router0    | FastEthernet0/1  | 192.168.1.0   | 192.168.1.1      | 255.255.255.0    | 2001:DB8:1::1/64       | Gateway para AS100                                      |
| Router0    | FastEthernet0/0      | 10.0.0.0      | 10.0.0.1         | 255.255.255.0    | 2001:DB8:10::1/64      | Enlace eBGP hacia Router1                        |
| Router1    |  FastEthernet0/0       | 10.0.0.0      | 10.0.0.2         | 255.255.255.0    | 2001:DB8:10::2/64      | Enlace eBGP hacia Router0                        |
| Router1    | FastEthernet0/1  | 192.168.2.0   | 192.168.2.1      | 255.255.255.0    | 2001:DB8:2::1/64       | Gateway para AS200                                      |
| Switch1    | -                | -             | -                | -                | -                      | Switch de capa 2 en AS200                               |
| PC2        | FastEthernet0    | 192.168.2.0   | 192.168.2.2      | 255.255.255.0    | 2001:DB8:0:B::2       | Host en AS200                                           |
| PC3        | FastEthernet0    | 192.168.2.0   | 192.168.2.3      | 255.255.255.0    | 2001:DB8:0:B::3      | Host en AS200   
  
