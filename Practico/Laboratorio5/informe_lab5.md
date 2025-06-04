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

## Desarrollo

# Del 1, falta hacer el punto a para tcp y udp.
# Faltan los punto 3 y 4

- 1 y 2: Existen dos scripts de python, `client` y `server`, ambos se pueden configurar por `CLI` para usar TCP (default) o UDP.

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

    - a: 
    - b: Los Scripts Client y Server loggean cada vez que se genera y recibe la información, respectivamente. Ambas sobre `log.txt`
    - c: El análisis de datos se hace mediante el script `analyze`.

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
