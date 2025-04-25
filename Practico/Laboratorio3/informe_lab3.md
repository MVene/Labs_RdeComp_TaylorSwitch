# Evaluación de performance en redes y ruteo interno dinámico Open Shortest Path First (OSPF)

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

#### 10 de Abril 2025

#### Información de contacto

- gaston.fernandez@mi.unc.edu.ar
- lujan.guimpelevich@mi.unc.edu.ar
- yesica.robles@mi.unc.edu.ar
- d.trujillo@unc.edu.ar
- milagros.venecia@unc.edu.ar

---

## Desarrollo

## 1- 
* **OSPF (Open Shortest Path First):** Es un protocolo de enrutamiento dinámico de estado de enlace. Se utiliza para tomar decisiones de enrutamiento calculando la ruta más corta para enviar paquetes dentro de un Sistema Autónomo (AS). 

* **Clases de Redes:** Las direcciones IP se dividen en clases (A, B, C, D y E) que determinan el tamaño de la red y el número de hosts que puede contener. Las clases A, B y C son las más comunes para asignar direcciones a los hosts. 

* **Algoritmos de Shortest Path:** Son algoritmos que calculan la ruta más corta entre dos puntos en una red. El algoritmo de Dijkstra es uno de los más utilizados por OSPF para encontrar la ruta más corta a través de un AS.

* **Teoría de Grafos y Redes OSPF:** La teoría de grafos se aplica a las redes al representar los dispositivos de red (routers, switches, hosts) como nodos y las conexiones entre ellos como aristas. OSPF utiliza esta representación para construir un mapa de la topología de la red y calcular las rutas más cortas. 


## 2-
<p align="center">
<img src="/Practico/Laboratorio3/Imagenes_tp3/2.jpg" ><br>
 <span><i>Imagen 1.Topologia de red</i></span>
</p>
Para diseñar el esquema de direccionamiento IP, se segmenta una red clase A o B para los hosts y se utiliza una red clase C para las conexiones entre routers.

* **Red Clase A para Hosts:** 10.0.0.0 /16
* **Redes Clase C para Enlaces entre Routers:**
    * R1-R2: 192.168.1.0 /30
    * R2-R3: 192.168.2.0 /30
    * R3-R4: 192.168.3.0 /30
    * R4-R5: 192.168.4.0 /30
    * R2-S1: 192.168.5.0 /30 (asumiendo S1 es un switch con una IP)

**Tabla de Direccionamiento:**

| Dispositivo | Interfaz | Dirección IP     | Máscara de Subred |
| :---------- | :------- | :--------------- | :---------------- |
| R1          | G0/0     | 10.0.1.1         | 255.255.0.0       |
|             | G0/1     | 192.168.1.1      | 255.255.255.252   |
| R2          | G0/0     | 192.168.1.2      | 255.255.255.252   |
|             | G0/1     | 192.168.2.1      | 255.255.255.252   |
|             | G0/2     | 192.168.5.1      | 255.255.255.252   |
| S1          | Vlan1    | 192.168.5.2      | 255.255.255.252   |
| R3          | G0/0     | 192.168.2.2      | 255.255.255.252   |
|             | G0/1     | 192.168.3.1      | 255.255.255.252   |
| R4          | G0/0     | 192.168.3.2      | 255.255.255.252   |
|             | G0/1     | 192.168.4.1      | 255.255.255.252   |
| R5          | G0/0     | 192.168.4.2      | 255.255.255.252   |
| h1          | NIC      | 10.0.1.10        | 255.255.0.0       |
| h2          | NIC      | 10.0.1.11        | 255.255.0.0       |
| h3          | NIC      | 10.0.2.10        | 255.255.0.0       |
| h4          | NIC      | 10.0.3.10        | 255.255.0.0       |
| h5          | NIC      | 10.0.4.10        | 255.255.0.0       |

## 3-
Cada router fue configurado con sus respectivas interfaces IP, tanto en los enlaces punto a punto como hacia las redes de hosts. Luego, se habilitó el protocolo OSPF utilizando el proceso número 1 (router ospf 1) y se asignaron todas las redes.

**Configuración del Router R2:**
 ```bash
enable
configure terminal


interface Serial1/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface Serial1/1
ip address 192.168.5.1 255.255.255.0
no shutdown
exit

interface FastEthernet0/0
ip address 10.0.0.1 255.0.0.0
no shutdown
exit

router ospf 1
network 10.0.0.0 0.255.255.255 area 0
network 192.168.1.0 0.0.0.255 area 0
network 192.168.5.0 0.0.0.255 area 0

```
Lo mismo se realiza con los demás routers. En particular, en el router R1 es necesario configurar una interfaz de loopback. Esto se hace de la misma forma que con las demás interfaces, especificando el nombre de interfaz como Loopback0

```bash
enable
configure terminal

interface Loopback0
ip address 1.1.1.1 255.255.255.255
no shutdown
```

Se utilizó ```bash show ip ospf neighbor ```para verificar el establecimiento de relaciones de vecinos OSPF entre routers directamente conectados.

 <img src="/Practico/Laboratorio3/Imagenes_tp3/3.jpg" >
 <img src="/Practico/Laboratorio3/Imagenes_tp3/4.jpg" >
 <img src="/Practico/Laboratorio3/Imagenes_tp3/5.jpg" >
 <img src="/Practico/Laboratorio3/Imagenes_tp3/6.jpg" >
 <img src="/Practico/Laboratorio3/Imagenes_tp3/7.jpg" >
 
Se realizaron pruebas de ping entre hosts y routers, confirmando la propagación de rutas y la correcta conectividad extremo a extremo.

<img src="/Practico/Laboratorio3/Imagenes_tp3/9.jpg" >

Luego se consultó la tabla de enrutamiento con ```bash show ip route ``` , observando entradas con la letra "O", que indican rutas aprendidas dinámicamente por OSPF

<img src="/Practico/Laboratorio3/Imagenes_tp3/10.jpg" >
<img src="/Practico/Laboratorio3/Imagenes_tp3/11.jpg" >
<img src="/Practico/Laboratorio3/Imagenes_tp3/12.jpg" >

## 4-
Con el objetivo de comprender en profundidad el funcionamiento del protocolo OSPF (Open Shortest Path First) y su impacto en la dinámica de la red, se llevó a cabo un análisis detallado de los mensajes intercambiados entre routers. OSPF es un protocolo de enrutamiento de estado de enlace que utiliza cinco tipos principales de paquetes para establecer, mantener y actualizar la topología de la red: Hello, Database Description (DBD), Link-State Request (LSR), Link-State Update (LSU) y Link-State Acknowledgment (LSAck).

Para identificar y analizar estos mensajes en detalle, se utilizó el modo de simulación paso a paso, lo cual permitió observar de manera controlada y secuencial el proceso de establecimiento de adyacencias, el intercambio de información de estado de enlace y la actualización de las bases de datos de los routers:

<img src="/Practico/Laboratorio3/Imagenes_tp3/16.jpg" >

Se observó especialmente el intercambio de paquetes Hello, fundamentales para establecer y mantener las adyacencias entre routers que utilizan el protocolo OSPF (Open Shortest Path First). Estos paquetes permiten detectar vecinos en la misma red, verificar la compatibilidad de parámetros (como el intervalo de Hello, Dead interval, ID de router, etc.) y mantener activa la relación de vecindad.

<img src="/Practico/Laboratorio3/Imagenes_tp3/17.jpg" >

Además, se visualizaron los paquetes Link-State Update (LSU), que contienen información sobre los cambios en el estado de los enlaces dentro de la red. Esta información es crítica para mantener actualizadas las bases de datos de estado de enlace (LSDB, Link-State Database) en todos los routers del área OSPF. Cada LSU puede incluir múltiples Link-State Advertisements (LSA), los cuales describen el estado y las conexiones de un router.

<img src="/Practico/Laboratorio3/Imagenes_tp3/18.jpg" >

Para asegurar una comunicación confiable, también se observó el envío de paquetes Link-State Acknowledgment (LSAck). Estos se utilizan para confirmar la recepción correcta de los LSUs, ya que OSPF, aunque es un protocolo confiable en cuanto a consistencia de base de datos, se basa en IP, un protocolo no confiable. Por ello, el acuse de recibo garantiza que los LSAs no se pierdan durante la transmisión.

<img src="/Practico/Laboratorio3/Imagenes_tp3/18.jpg" >

Gracias al intercambio de estos mensajes —Hello, LSU y LSAck—, los routers pueden construir una LSDB coherente y sincronizada en toda el área OSPF. A partir de esta base de datos, cada router ejecuta el algoritmo de Dijkstra (también conocido como algoritmo SPF, Shortest Path First) para calcular las rutas óptimas hacia cada destino en la red.








