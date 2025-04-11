# Topologías multi-path y evaluación de performance en redes
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

 **08 de Abril 2025**  
 
**Información de contacto**
- gaston.fernandez@mi.unc.edu.ar
- lujan.guimpelevich@mi.unc.edu.ar
- yesica.robles@mi.unc.edu.ar
- d.trujillo@unc.edu.ar
- milagros.venecia@unc.edu.ar
---
# Desarrollo

## 1- 
Para el diseño de la topología de red se utiliza Packet Tracer, con el objetivo de realizar posteriormente su representación física. La topología de red propuesta para todo el curso es la siguiente:
<p align="center">
<img src="/Practico/Laboratorio2/Imagenes_tp2/1.jpg" >
 <span><i>Imagen 1.Topologia de red</i></span>
</p>
Se utilizará direcciones IPv4 de clase C y subredes con prefijo /27 y se dejará reservadas las primeras direcciones de cada subred para la puerta de enlace predeterminada
La tabla de segmentación a utilizar para configurar el Switch, el Router y las PCs es la siguiente:

| **Dispositivo** | **Tipo**     | **Red/Subred**   | **Dirección IP (ejemplo)**        | **Conectado a**         |
|-----------------|--------------|------------------|-----------------------------------|-------------------------|
| H11, H12        | PC           | 192.168.1.0/24   | 192.168.1.11 / 192.168.1.12       | Switch S1               |
| H41, H42        | PC           | 192.168.1.0/24   | 192.168.1.41 / 192.168.1.42       | Switch S1               |
| S1              | Switch       | -                | -                                 | Router R1               |
| R1              | Router       | 12.0.0.0/30, 13.0.0.0/30 | 12.0.0.1, 13.0.0.1     | R2, R3, Switch S1       |
| R2              | Router       | 12.0.0.0/30, 23.0.0.0/30 | 12.0.0.2, 23.0.0.1     | R1, R3, Switch S2       |
| R3              | Router       | 13.0.0.0/30, 23.0.0.0/30 | 13.0.0.2, 23.0.0.2     | R1, R2, Switch S3       |
| S2              | Switch       | -                | -                                 | PCs H21, H22, R2        |
| H21, H22        | PC           | 192.168.2.0/24   | 192.168.2.21 / 192.168.2.22       | Switch S2               |
| S3              | Switch       | -                | -                                 | PCs H31, H32, R3        |
| H31, H32        | PC           | 192.168.3.0/24   | 192.168.3.31 / 192.168.3.32       | Switch S3               |

Para configurar las direcciones IP de los hosts, se accedió al escritorio de cada dispositivo y se utilizó la aplicación 'IP Configuration' para realizar la asignación manual de parámetros. Este procedimiento se repitió para todas las PCs de la red, asignando en cada caso la dirección IP correspondiente, junto con su máscara de subred y la puerta de enlace predeterminada asociada al router de su segmento. A continuación, se muestran las configuraciones:
  <div >
    <img src="/Practico/Laboratorio2/Imagenes_tp2/2.jpg"><br>
    <span><i>Imagen 2. Asignación de dirección IPv4 del host h11</i></span><br><br>
  </div>
  <div >
    <img src="/Practico/Laboratorio2/Imagenes_tp2/3.jpg"><br>
    <span><i>Imagen 3. Asignación de dirección IPv4 del host h12</i></span><br><br>
  </div>
  
**Configuración del Router R1:**
```bash
enable
configure terminal
interface FastEthernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit

interface Serial1/1
ip address 12.0.0.1 255.0.0.0
no shutdown
exit

interface Serial1/0
ip address 13.0.0.1 255.0.0.0
no shutdown
exit

ip route 192.168.2.0 255.255.255.0 12.0.0.2
ip route 192.168.3.0 255.255.255.0 13.0.0.3

```
**Configuración del Router R2:**

```bash
enable
configure terminal
interface FastEthernet0/0
ip address 192.168.2.1 255.255.255.0
no shutdown
exit

interface Serial1/0
ip address 23.0.0.2  255.0.0.0
no shutdown
exit

interface Serial1/1
ip address 12.0.0.2  255.0.0.0
no shutdown
exit

ip route 192.168.1.0 255.255.255.0 12.0.0.1
ip route 192.168.3.0 255.255.255.0 23.0.0.3

```
**Configuración del Router R3:**

```bash
enable
configure terminal
interface FastEthernet0/0
ip address 192.168.3.1 255.255.255.0
no shutdown
exit

interface Serial1/0
ip address 13.0.0.3 255.0.0.0
no shutdown
exit

interface Serial1/1
ip address 23.0.0.3  255.0.0.0
no shutdown
exit

ip route 192.168.1.0 255.255.255.0 13.0.0.1
ip route 192.168.2.0 255.255.255.0 23.0.0.2

```
Para verificar el funcionamiento correcto de las rutas estáticas configuradas en los routers, se utiliza el comando ping, que permite enviar paquetes ICMP (Internet Control Message Protocol) a distintos dispositivos de la red. Se prueba la conectividad entre hosts pertenecientes a diferentes redes. En cada caso, se comprueba que los paquetes lleguen correctamente a su destino y que exista una respuesta, lo cual indica que las rutas configuradas están operativas. Todas las pruebas realizadas confirmaron la comunicación exitosa entre los distintos segmentos de red, validando así la correcta implementación del enrutamiento estático:


<div>
   <div >
   <img src="/Practico/Laboratorio2/Imagenes_tp2/4.jpg" ><br>
   <span><i>Imágen 4. Comprobación de conectividad de h11 a h21 y h31</i></span><br><br>
   </div>
   <div>
   <img src="/Practico/Laboratorio2/Imagenes_tp2/5.jpg" ><br>
   <span><i>Imágen 5. Comprobación de conectividad de h21 a h11 y h31.</i></span><br><br>
   </div>
   <div>
   <img src="/Practico/Laboratorio2/Imagenes_tp2/6.jpg" ><br>
   <span><i>Imágen 6. Comprobación de conectividad de h31 a h11 y h21.</i></span><br><br>
   </div>
</div>

## 2 y 3-
**Principales comandos para pruebas con iPerf3**
- **Configuración del servidor y cliente:**
  - Iniciar el servidor:
  <img src="/Practico/Laboratorio2/Imagenes_tp2/14.jpeg" ><br>
Esto indica que iperf3 está esperando conexiones en el puerto 5201 (puerto por defecto de iperf3). Un cliente que se conecte a esa IP y puerto puede empezar a hacer pruebas de red.

  - Iniciar el cliente:
<img src="/Practico/Laboratorio2/Imagenes_tp2/7.png" ><br>

- **a) Protocolos TCP y UDP**
  - TCP (por defecto):

      <img src="/Practico/Laboratorio2/Imagenes_tp2/7.png" ><br>
  
  - UDP (agregar -u):
 
     <img src="/Practico/Laboratorio2/Imagenes_tp2/8.png" ><br>

- **b) Número y tamaño de paquetes**
   - Definir tamaño de paquete TCP (por defecto es 128 KB):
     
      <img src="/Practico/Laboratorio2/Imagenes_tp2/9.png" ><br>
      
   - Definir tamaño de paquete UDP:
     
      <img src="/Practico/Laboratorio2/Imagenes_tp2/10.png" ><br>

- **c) Frecuencia y tiempo de prueba**
   - Duración de la prueba (en segundos, por defecto 10s):
     
    <img src="/Practico/Laboratorio2/Imagenes_tp2/11.png" ><br>

- **d) Ancho de banda**
   - Definir ancho de banda UDP
     
    <img src="/Practico/Laboratorio2/Imagenes_tp2/12.png" ><br>

## 4- 
En primer lugar, **el ancho de banda alcanzado con TCP fue significativamente mayor**, llegando a ~94 Mbps, mientras que **UDP se mantuvo en 1.05 Mbps**. Esto demuestra cómo TCP puede aprovechar mejor la capacidad de la red al adaptarse dinámicamente.

Ambas pruebas tuvieron una duración de **10 segundos**, valor por defecto de iperf3, y **no se detectaron pérdidas de paquetes** ni en TCP ni en UDP. En UDP, incluso con el tráfico constante, el jitter fue prácticamente nulo (0.084 ms), lo que indica una red estable.

Respecto al **tamaño promedio de los paquetes**, se estimó que en UDP fue de aproximadamente 1,447 bytes, lo que es típico para datagramas que evitan la fragmentación. En TCP, no se puede calcular directamente, ya que el protocolo fragmenta y gestiona los datos dinámicamente.

Finalmente, se confirma que existe una relación entre los parámetros de la prueba y el comportamiento de la red, especialmente en UDP. Si el ancho de banda solicitado excediera la capacidad de la red, comenzarían a observarse pérdidas de paquetes. TCP, por su parte, maneja esto mediante mecanismos de control de congestión.

En resumen, TCP ofrece mayor rendimiento y confiabilidad, adaptándose a las condiciones de la red, mientras que UDP, aunque más simple y liviano, requiere una configuración adecuada para evitar pérdidas, especialmente cuando se aumenta el tráfico.

  



