# Laboratorio N°5
## Networking Y Capa de Transporte en Sistemas Encriptados.

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

# Desarrollo
## Scripts Python para envío y recepción de paquetes por TCP
## 1.a) Envío y recepción de paquetes TCP

Se desarrollaron dos scripts en Python, uno actuando como cliente y otro como servidor, que permiten enviar y recibir paquetes de datos utilizando el protocolo TCP (default) o UDP.
  Ambos scripts debe ser ejecutados como:
  
```bash
    python3 -u ./server.py # Este debe ejecutarse primero. 
    # Para ver sus opciones, ejecutar con '-h | --help'
```
Y luego el cliente:
    
```bash
    python3 -u ./client.py
    # Para ver sus opciones, ejecutar con '-h | --help'
```

El cliente envía mensajes identificatorios del tipo `Taylor_Switch_XX`, donde `XX` representa un número incremental.
El servidor escucha en un puerto determinado y registra los mensajes recibidos.

El envío se realiza a intervalos configurables (por defecto 1 segundo) y se implementó una opción para alternar entre TCP y UDP mediante argumento de línea de comandos.

## 1.b) Log de paquetes con timestamp
Ambos scripts registran los eventos de envío y recepción de paquetes en un archivo de log (log.txt). Cada línea contiene:
- El tipo de evento (SENT o RECEIVED),
- El contenido del mensaje,
- El timestamp de envío o recepción,
- El protocolo usado.

Ejemplo de log:
```bash
SENT Taylor_Switch_0 at 1749698804.4373617 - Protocol: tcp
RECEIVED Taylor_Switch_0 at 1749698804.4388385 - Protocol: tcp
```

Esto permite realizar un posterior análisis temporal de los mensajes intercambiados.

Código relevante:

```bash
def log_packet(data: str, timestamp: float, protocol: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"SENT {data} at {timestamp} - Protocol: {protocol}\n")
```
## 1.c): Métricas de la conexión TCP
Se analiza el rendimiento de la comunicación TCP calculando:
- Latencia promedio
- Latencia mínima y máxima
- Jitter
Para ello se utilizaron los timestamps registrados en log.txt, tanto del cliente (envíos) como del servidor (recepciones).

Se desarrolló un script en Python que:

- Parsea el archivo de log buscando líneas con estructura:
```bash
SENT Taylor_Switch_0 at 1749698804.4373617 - Protocol: tcp
RECEIVED Taylor_Switch_0 at 1749698804.4388385 - Protocol: tcp
```

- Agrupa por protocolo y ID de mensaje.

- Calcula la latencia como la diferencia entre received - sent.

- Calcula el jitter como el promedio de las diferencias absolutas entre latencias consecutivas.

Fragmento clave del script:
```bash
latency = times["received"] - times["sent"]
jitter_values = [
    abs(latencies[i] - latencies[i - 1]) for i in range(1, len(latencies))
]
avg_jitter = sum(jitter_values) / len(jitter_values)
```

 ```bash
  python3 -u ./analyze.py 'log.txt'
 ```
        Métricas para TCP: 
            Muestras: 100
            Latencia promedio: 0.100 ms
            Latencia mínima: 0.054 ms
            Latencia máxima: 0.456 ms
            Jitter: 0.004 ms

        Métricas para UDP:
            
            Muestras: 100
            Latencia promedio: 0.076 ms
            Latencia mínima: 0.055 ms
            Latencia máxima: 0.206 ms
            Jitter: 0.002 ms       

## 4.a) 
El **encriptado simétrico** utiliza una única clave secreta que emplean tanto el transmisor como el receptor, ya sea para encriptar o para desencriptar los mensajes. Es un método sencillo, muy eficiente y rápido, ideal para cifrar grandes volúmenes de datos (por ejemplo, bases de datos o almacenamiento). No obstante, su principal desafío es la distribución segura de la clave: si alguien la intercepta, todo el sistema queda comprometido. 

Ventajas:
- Alta velocidad y bajo consumo de recursos computacionales.
- Simplicidad de implementación y menor tamaño de clave (por ejemplo, AES-128 o AES-256) .

Desventajas:
- El secreto de la clave debe mantenerse intacto.
- Requiere canales seguros o mecanismos adicionales (como intercambio Diffie–Hellman) para el envío de la clave .

El **encriptado asimétrico** Este sistema emplea un par de claves: una pública, que cualquiera puede usar para cifrar mensajes, y una privada, que solo el destinatario posee para descifrarlos. Su fortaleza radica en que no requiere compartir la clave privada, eliminando el riesgo asociado en el modelo simétrico .

Ventajas:
- Gran seguridad para intercambios en redes abiertas (Internet, correo electrónico, firmas digitales, etc.).
- Permite autenticidad y no repudio mediante el uso de firmas criptográficas .
  
Desventajas:
- Más lento y costoso computacionalmente debido a llaves largas (por ejemplo, RSA de 2048 bits frente a AES-256) .
- La validación de claves (certificados, infraestructura PKI) añade complejidad adicional 


