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


 


