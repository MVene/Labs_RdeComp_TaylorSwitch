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

### Parte 2.
#### 1.