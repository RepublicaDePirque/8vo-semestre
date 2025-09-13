# Capitulo 1---------------------------------------------

## Objetivos:
1. Visión general sobre los sistemas distribuídos
2. Conceptos básicos
3. Marco de trabajo

## Contenidos:
1. Evolución de sistemas distribuidos
2. Nociones básicas de arquitectura
3. Casos y tendencias en sistemas distribuidos

***Motivación  y evolución:***

**Porque son importntes:**
1. Alto rendimiento y escalabilidad
2. Alta disponibilidad y resiliencia: Es fiable y tolerante al fallo.
3. Compartición de recursos: Las organizaciones comparten mejor sus recursos y se facilita el trabajo colaborativo.
4. Distribución geográfica.
5. Inteligencia ambiental: Actual inteligentemente con el entorno, como IOT
6. Necesidades económicas.

**¿Que es un sistema distribuido?: Definiciones**

- Según Colorius: Un sistema que consta de componentes de hw y sw localizados en una red de computadores que comunican y coordinan sus acciones sólo por paso de mensajes. 
	- *Message passing: No hay memoria compartida y la única forma de comunicarse es a través de mensajes*
- Según Tanenbaum & Van Steen: Conjunto de computadores independientes que se muestra ante sus usuarios como un único sistema coherente.
- Según Leslie Lamport: Es un sistema donde la falla de un computador puede dejar inutilizable tu propio computador.
	- *Hay mucha independencia entre los servicios dentro del sistema.*
- **Objetivo principal:** Los prcesos trabajan en conjunto por un fin.

**¿Que se distribuye?**

1. *Procesamiento*, lo que provoca mayor paralelismo, lo que disminuye la carga para cada computador. Este requiere coordinación.
2. *Datos:* Colocamos copias de los diferentes datos en diferentes lugares para aliviar carga y mayor tolerancia a fallos. Requiere mantener consistencia.
3. *Control:* Provee mayor autonomía a los nodos para mejorar rendimiento, resiliencia y escalabilidad. Requiere una coordinación inicial.
4. *Geográfica:* Acercamiento de nodos a usuarios puede mejorar la calidad del servicio.
5. *Gestión:* Nodos pueden estar bajo diferentes dominios administrativos. Hay que resolver si problemas de integración, gobernanza, etc.

**Falacias: Según Peter Deutsch**
- La red es fiable
- La latencia es 0
- El ancho de banda es infinito
- La red es segura
- La topología no cambia
- Existe un único administrador
- El costo de transporte es 0
- La red es homogénea


## Caracteristicas principales:
1. Múltiples elementos de computación autónomos: Su funcionamiento no depende de otros.
2. Subred de comunicación compartida: Permite un intercambio de datos coordinado. La comunicación es por paso de mensajes. 
3. El sistema tiene un estado global. Los nodos/ususarios no conocen el estado global del sistema. Es una construcción con los estados locales.
4. Tiempo global impreciso: Múltiples relojes sin sincronización perfecta, por lo tanto no hay un patrón de tiempo 100% confiable. 
5. Fallas independientes: Como hay muchas partes, estas partes pueden fallar independientemente, lo que puede significar tanto cosas positivas como negativas. En algunos casos puede ser bueno ya que no falla el sistema completo, mientras que en otros es algo crucial de solucionar. 
6. Aumento de ataques, ya que al haber un volumen más grande de componentes, nodos, usuarios, etc.

## Desafíos:
1. Como hacemos el sistema resiliente, garantizamos el funcionamiento correcto y continuo del sistema?
	1. Debemos implementar algún mecanismo que lo permita. 
	2. Se mide por fiabilidad, o probabilidad de que no haya fallado, y  la disponibilidad, o probabilidad de que esté funcionando correctamente. 
	- Esta asociado a la redundancia (*Hay diferentes tipos, como componentes, repetir una acción en el tiempo, etc*) y tolerancia de fallos. 
2. Como mantenemos un alto rendimiento con una mayor carga de trabajo? 
	1. Incrementando recursos y distribuyendo la carga.
3. Como mantengo el sistemaa consistente? 
4. Como mantenemos el sistema seguro ante amenazas? 

## Arquitectura de software distribuidos
1. Integración: Resolver problemas de interoperabilidad.
2. Observabilidad: Monitoreo.
3. Mantenibilidad: Facilitar la adaptación.

## Modelos fundamentales: Comportamiento esperado del SD
1. **Modelo de sincronismo.**
	1. Sincronico vs Asincronico.
2. **Modelos de fallas.**
	1. Tipos de fallas: Procesos, canales de comunicación, etc.
	2. Modelos de fallas: Detención, caídas, omisiones, etc.
3. **Modelos de consistencia:**
	1. Estados globales consistentes
	2. Consistencia de réplicas y caché.
	3. Transacciones, concurrencias y atomicidad. 
4. **Modelos de seguridad:** 
	1. Modelos de amenazas y control.
	2. Gestión de seguridad.

# Nociones básicas sobre arquitectura y diseño
## Computación de alto rendimiento:
- **Sistemas de multiprocesamiento con memoria compartida:**
	- Mayora capacidad de procesos, pero memoria compartida es cuello de botella.
- **Sistema multicomputados homogéneo:**
	- Múltiples CPU con memoria distribuida conectados en red. 
 ------------------
#### Meta: Transparencia: 
***Simplificar el manejo de la complejidad sistemática:***
1. Acceso
2. Ubicación
3. Reubicación
4. Migraci+on
5. Replicación
6. Concurrencia

#### Meta: Apertura:
***Facilidad de integración, interoperabilidad y portabilidad:***
1. Fuentes de heterogeniedad: Computadores, SO, LP, protocolos, etc.
2. Algunas estrategias: 
	1. Middleware
	2. Maquinas virtuales y código móvil interpretado.
3. Preocupaciones principales:
	1. Estandarización de interfacies (API): Componentes y conectores
	2. Extensiones, evolución e integración.

#### Meta: Escalabilidad:
***Capacidad de crecer y soportar cargas crecientes:***
1. Particionamiento y replicación
	1. Estructuras de múltiples servidores colaborativos.
	2. Distribución de carga entre servidores
2. Acercamiento del sistema a los usuarios
	1. Uso de proxies, caching y edge computing.
	2. Movilidad de código, acercando procesamiento al usuario.
3. Explotación de asincronísmo: Mejorar tiempos de respuesta. Escencialmente consiste en no esperar una respuesta para seguir trabajando.
4. Reducción de sobrecarga de coordinación:
	1. Usar componentes sin estado

#### Meta: Resiliencia:
***Asegurar continuidad operacional en ambientes hostiles:***
- Tolerancia a fallos y redundancia
- Modelos de fallas
- Atomicidad y enfoques de recuperación de datos
- Detección de fallas y recuperación de errores

#### Meta: Seguridad:
- Confidencialidad, integridad y disponabilidad (CIA)
- Autenticación de entidades y mensajes
- Control de acceso, autorización y auditoría.
- No repudio y firma digital
- Arquitectura de seguridad y protección de activos
- Detección de anomalías e intrusiones.
- etc


# Capitulo 2-------------------------------------------
## Arquitectura:
***Se refiere a la organización lógica y estructural de un sistema, abordando:***
- Componentes, o bloques
- Relaciones, o conexiones entre componentes
- Principios, guias de diseño
**Propósito:** Definir un plan para de construcción para sistemas robustos, eficientes, escalables, etc.

**A partir de esto, surgen paradigmas de comunicación,** que escencialmente indican como se comunican los componentes.

1. *Transferencia de control* indica una comunicación directa entre 2 entidades, similar a un esquema de mensaje/respuesta.
2. *Memoria compartida* indica una comuniación indirecta, donde ambas partes acceden a la información a través de un intemrediario o espacio de almacenamiento.
3. *Transferencia de datos* indica una comunicación en paquetes. (Directa o indirectamente)

### Estilos de interacción directa:
***Interacciones sincrónicas:***

1. **Invocación directa:** Request -> Reply
2. **Data streaming:** Transferencia de paquetes

### Estilos de interacción indirecta:
***Interacciones asincrónicas y desacopladas:***

1. **Repositorios:** Espacios de datos compartidos
2. **Colas de mensajes:** "Cartero" que hace de intermediario


# Que es un estilo arquitectónico?
## Def: 
Una estrategia abstracta de alto nivel que define la estructura general de un sistema. 

## Caracteristicas:
1. Define **reglas fundamentales**.
2. **Tecnologicamente agnostico** lo que significa que hay diversas maneras de implementarlo.
3. Orienta sobre **decisiones de diseño globales.**

## Estilo cliente-servidor:
#### Def: 
- Componente cliente solicita y componente servidor responde.
- A través de **requests**
- Con o sin estado. *(REST/Servidor de datos)*


## Binding:
***Nombramiento de componentes***

#### Resolución de nombre:
- **Estático:** A priori.
- **Dinámico:** En tiempo de ejecución.
#### Estilo de interacción:
- **Directa:** Iniciador conoce a priori nombre de la entidad objetivo.
- **Indirecta:** El iniciador solo debe conocer el nombre del intermediario.

## Patones arquitectónicos:
***Soluciones a problemas comunes:***

1. **Proxy:** Intermediario entre cliente y servidor.
2. **Broker:** Intermediario entre cliente y componente distribuido. Escencialmente maneja la información, comunicación y coordina. 
3. **Gateway:** Traduce protocolos, APIs, encapsula accesos proveyendo un punto de acceso *(REST, API gateway, etc.)*
4. **Adapter:** Convierte interfaces a unas esperadas.
5. **Fachada:** Interfaz unificada para fácil uso.
6. **Registro:** Seguimiento de objetos o servicios.
7. **MVC:** Divide interacción usuaria en *modelo, vista y control.*


## Gestión de cambios:

### Configuración:
1. Replicación..
2. Balance de carga.
3. Cambios de confugración por elasticidad.
4. Tolerancia a fallos.
5. Mantenibilidad.
### Registros, nombres y directorios:
1. Resolución de nombres
2. Requiere alta disponibilidad y tolerancia a fallos.


# Estilos arquitectónicos:
![[Pasted image 20250905203613.png]]

## 1) Multi-layered:
***Capas de abstracción de software***

### Características:  
- Organiza funciones por valor *(Modularización)*

### Interacciones:
- Cada capa usa servicios de capas inferiores *(downcall)*
- Registros superiores pueden recibir llamadas de capas inferiores *(upcall)*

1. **Estricto:** Solo permite que una función utilice estrictamente la función inferior.
2. **Permisivo:** Puede utilizar funciones de capas más inferiores.
3. **Con UPCALL:** Permite hacer llamados a funciones superiores.

##### ***Acá aparece el middleware***

### Servicios CLOUD:
***Principales capas de abstracción:***
1. **Infra. como servicio:** A través de internet entrega recursos virtualizados.
	1. *Usuarios administran SSOO, apps y almacenamiento*
2. **Plataforma como servicio:** Ofrece plataformas para dev para desarrollo y mantenimiento de aplicaciones en entornos preconfigurados.
3. **Software como servicio:** Aplicaciones completamente funcionales por internet.
4. 

## 2) Multi-tiered:
***Capas lógicas con responsabilidades específicas con el objetivo de definir un patrón de despliegue en un ambiente distribuído.***

- Mayor separación de responabilidades, modularidad, reusabilidad y escalamiento.
- Más latencia y sobrecarga además de un fuerte acoplamiento.
![[Pasted image 20250905212249.png]]


## 3) Servicios:

### Orientada a servicios (SOA):
***Aplicaciones complejas como conjunto de servicios compuestos reutilizables, autónomos, modulares y se comunican mediante una red.

- *Separación de responsabilidades, modularidad, escalabilidad.*
- *Sobrecarga*
#### Características:
- Acoplamiento débil
- Abstracto
- Reusable
- Interoperabilidad

#### Protocolos: 
- **SOAP:** XML
- **REST:** HTTP + JSON

#### Servicios de apoyo:
- **Brokers**

#### Componentes:
1. **Servicios:** Unidad funcional autónoma.
2. **Proveedor de servicio:** Entidad que presta el servicio.
3. **Consumidor de servicios:** Utiliza servicios.
4. **Contrato de servicio:** Como utilizar el servicio.
5. **Registro de servicio:** Directorio de servicios.
6. **Brokers de servicios:** Middleware que facilita comunicación entre servicios.


### Microservicios:
***Conjunto de servicios pequeños, independientes, poco acoplados y descentralizados.***

- *Autonomía de equipos, agilidad, mantención y despliegue, escalabilidad, diversidad, etc.*
- *Complejo, latencia, inconsistencia*

#### Características:
- Enfocado en única capacidad de negocio.
- Autónomo.
- Independencia de implementación
- Escalable, mejor rendimiento y agilidad.

### Serverless y FaaS (Function as server):
- ***Serverless: Desarrolladores despliegan aplicaciones sin gestionar la infraestructura.***
- ***FaaS: Usa serverless para desplegar funciones que se ejecutan bajo depanda en respuesta a eventos y finalizan cuando termina la tarea.***


## Mensajería
***Basado en sistemas que permiten intercambio de mensajes entre apps, servicios, etc. Mejora la escalabilidad y fiabilidad***

#### Características:
- **Desacomplamiento:** Productores y consumidores operan independientemente y se comunican indirectamente.
- **Durabilidad:** Almacen de mensajes persistente.
- **Escalabilidad:** Soporte para grandes volúmenes de mensajes.
- **Garantía de entrega.**
- **Ordenamiento:** Mensajes en orden.

### a) Arquitectura orientada a mensajes:
***Componenetes de comunican indirectamente a través de un intermediario con almacenamiento persistente.
- Comunicación asíncrónica y desacoplada

### b) Arquitectura dirigida por eventos:
***Eventos dirigen el flujo de datos y gatillan reacciones. 
- Comunicación asíncrona y desacoplada
- Procesamiento en tiempo real.
- Consistencia eventual
- Escalable y tolerante.

## Datos compartidos:
***Procesos interactúan indirectamente a través de espacios compartidos, como bbdd, repositories, etc.***

### Características:
- Desacompaliemtno de componentes
- Requiere sincronización y consistencia.
- Durabilidad de datos.

#### a) Memoria compartida y espacio compartido:

1. ***Memoria compartida distribuída:*** Varios procesos comparten memoria como un espacio de direcciones unificado.
2. ***Espacio de tuplas:*** Coordinación de procesos que interactúan indirectamente a través de un espacio compartido.

#### b) Sistemas de almacenamiento de datos persistentes:
***Componentes independientes interactúan asincrónica e indirectamente a través de un espacio compartido almacenado en u medio persistente.***

##### Características:
1. Datos estructurados, no estructurados y semi-estructurados.
2. Asegurar durabilidad en medio persistente.
3. Lenguaje de consulta.
4. Sincronización.
5. Rescalabilidad y tolerancia a fallos.

### Caching:
- Mejora el rendimiento
- Escalabilidad
- Alta disponibilidad y tolerancia a fallos.


## Arquitectura de redes P2P.
***Modelo descentralizado donde cada nodo es cliente/servidor.****
- No cuenta con autoridad central
- Pares se comunican directamente
- Auto-organizada.

### Tipos de redes p2p:
1. ***No estructurados:*** Pares conectados aleatoriamente.
2. ***Estructurados:*** Usan una topología especifica.
3. ***P2P híbrido:*** P2P + componentes centralizados.

### Ventajas P2P:
1. Descentralización
2. Escalabilidad y distribución
3. Tolerancia a fallos
4. Uso eficiente de recursos.

### Desventajas:
1. Gestión de peers.
2. Riesgos de seguridad
3. Coherencia de datos
4. Alta rotación de nodos.


# Nombramiento y descubrimiento:
***Un nombre se usa para identificar en un programa algún recurso del sistema.***
- La *resolución del nombre* liga a una entidad una dirección en memoria.
- Permite acceder y compartir recursos.

##### Tipos de referencias:
1. Nombre *(Que se quiere buscar)*
2. Dirección *(Donde está)*
3. Ruta *(Como llegar)*

## Nombramiento en SD:
***Asignación y resolución de identificadores. Esto permite descubrir y acceder a recursos sin requerir conocimiento de sus ubicación física.***

- *Resolución de nombres:* Dinámica
- *Transparencia* de ubicación, migración, eplicación, etc.
- *Servicio de nombramiento:* Requerido para descubrir dinámicamente componentes

### Algúnas definiciones:
- **Entidad**
- **Nombre:** Secuencia de caracteres que permite referenciar una entidad en un sistema. 
- **Espacio de nombres:** Conjunto de nombres válidos..
- **Ligado de nombre:** Asociar el nombre con un recurso. Puede ser dinámico o estático.
- **Nombramiento:** Mapeo entre nombres, id, direcciones, etc.


### Tiempo de ligado:
- **Compilación:** Direcciones fijas son de uso eficiente, pero inflexibles y dificiultan compartir. 
- **Tiempo de carga:** Direcciones se resuelven al momento de cargar el problema. Más flexible.
- **Tiempo de ejecución:** Se resuelve en tiempo de ejecución.


### Clasificación de nombres:
1. **Orientado a humanos:** Caracteres legibles, por ejemplo *"www.inf.utfsm.cl"*
2. **Orientado a sistemas:** Uso eficiente por sistemas, por ejemplo: *200.1.19.23*

3. **Nombre plano:** No tiene estructura, por ejemplo *JuanitoPerez*
4. **Nombre estructurado:** Está estructurado en varios campos, por ejemplo *usr/remote/bin/share*

### Unicidad de nombres: 
***Dificil de lograr a gran escala***

#### Para nombres planos:
Mediante secuencias de caracteres sin estructura para los humanos. Escencialmente dividimos el espacio de nombres usando prefijos. Al hacer esto, una parte del nombre es asignada por una autoridad central y la otra es asignada localmente. 

#### Para nombres estructuradso:
Se establece una jerarquía para organizar la información. Partiendo desde un punto base, como / en el computador.


### Modelos de nombramiento:
#### Nombramiento plano:
Sin estructura, son identificadores únicos. Dificil de gesitonar a gran escala, pero eficaz en la busqueda.
#### Nombramiento jerarquico:
Estructurado como arbol. Se adapta bien pero requiere más pasos de busqueda.

#### Nombramiento basado en atributos:
Identifica recursos por propiedades. Es flexible, pero requiere indexación y más procesamiento.

## Resolución de nombres:
***Mapeo de un nombre de una entidad  a algún atributo.***
#### Características:
- Se debe buscar y encontrar en el espacio cierta información asociada a una entidad.
- Busqueda simple y repetitiva.
- Implementación puede requerir bajar niveles de abstracción.
#### Mecanismo de clausura:
Si la información está distribuída en múltiples sitios hay que saber donde empezar y donde terminar para asegurar encontrar lo buscado.

### a) Resolución de nombres planos:
1. **Difusión:** Broadcast de un identificador de una entidad a la red.
	- No escala bien y requiere que todos los procesos escuchen solicitudes.
2. **Punteros de avance:** Cuando algo se mueve, deja un puntero hacia la siguiente ubicación.
	- Transparente para el cliente.
	- No escala bien y cadenas son muy largas. 
	- Caché puede mitigar el problema.
3. **Enfoque de base:** Cada entidad tiene una dirección permanente en un domicilio.

### b) Resolución en nombres estructurados:
1. **Iterativo controlado por el cliente:** Cliente repite la consulta a cada servidor de la cadena hasta llegar a la dirección.
	1. Cliente le pregunta al primer servidor por dirección completa. 
	2. Si el servidor no la tiene, referencia al cliente al siguiente servidor. 
	3. Repetir hasta llegar a la dirección completa.
2. **Iterativo controlado por el servidor:*** Cliente solo pregunta. El servidor hace el trabajo. 
3. **Recursivo controlado por el servidor:** La consulta se sumerge recursivamente en la jerarquía de servidores.
	1. Cliente le pregunta al servidor 1. 
	2. Servidor 1 le pregunta a servidor 2 en nombre del cliente.
	3. Repetir hasta encontrar la respuesta.
	4. La respuesta vuelve por el mismo camino.

## Nombramiento y descubrimiento de componentes:

#### Servicios de nombramiento: nombres estructurados:

##### Servicios de nombre:
1. Convención y sintaxis
2. Nombres definidos son únicos para cada entidad.
3. Puede conectar un conjunto de contextos del mismo tipo.
##### Servicio de directorio:
1. Extensión de un servicio de nombre: Entidades tengan varios atributos.
2. Permite búsquedas basada en atributos.


#### Espacio de nombres:
1. **Nombres** compuestos, definiendo un camino en un grafo dirigido.
	1. Arcos
	2. Nodo raíz
	3. Nodo
2. **Nodos hoja:** Entidades nombradas.
3. **Nodos directorios:** Entidades que refieren a otros.
4. **Enlace simbólico:** Se define agregando en un nodo directorio un nombre absoluto. 

![[Pasted image 20250909145019.png]]


## Metas de diseño:
#### Escalabilidad y buen desempeño: 
- **Particionamiento** en multiples dominios administrativos y servidores para descentralizar mantención y resolución de datos.
- **Caching** para nombres resueltos y replicación.
- **Consistencia eventual** para mejor desempeño.
#### Alta disponibilidad:  
Replicar datos para mejor disponibilidad, pero hay que gestionar fallos.
#### Seguridad:
Suplantación de identidad, datos sensibles, integridad, etc.


## Sistema de archivo Sun-NFS:
***Protocolo que permite a un computador acceder a archivos a través de una red como carpeta compartida.***

#### Arquitectura y flujo: 
##### Cliente:
1. Programa quiere acceder a un archivo. Para eso hace una llamada al sistema sin saber si es u archivo local o remoto.
2. Sistema de archivo virtual (VFS) intercepta la llamada y define si el archivo es local o corresponde a un archivo remoto. Si es remoto, redirige la operación al CLIENTE NFS.
3. Cliente NFS empaqueta la solicitud y la envía a través de la red hacia el servidor.
##### Servidor:
1. El Servidor NFS recibe la solicitud, la decodifica, y entiende la operación.
2. Servdor NFS pasa la solicitud al VFS del servidor. 
3. La información toma el camino inverso.

***Podemos montar diferentes servidores a nuestro nodo.***

1. *Permite escalamiento:* Permite centralizar el almacenamiento en servidores dedicados. 
2. *Transparencia de acceso y ubicación:* No nos importa como clientes donde se encuentra la información, pero podemos acceder a ella facilmente. 

## Lightweight directory access protocol:
***Permite acceder y gestionar servicios de directorio. Su función principal es centralizar información para que sea consultada de manera eficiente.***

#### Base de información de directorio:
DIB: A diferencia de una BD tradicional, un directorio está optimizado para lecturas y búsquedas rápida a través de TCP/IP

#### Estructura jerarquica:
La info no se guarda en tablas planas, sino en estructuras similares a un arbol de carpetas. Esto permite organizar de manera lógica y escalable organizacioens y departamentos.

#### Entradas y atributos:
Cada objeto es una entrada o nodo en el arbol. Cada entrada tiene un nombre único y contiene <atributo, valor> que lo describe.


# Capitulo 3-------------------------------------------

# Programación distribuida y comunicación:

## Programación distribuida
***Múltiples programas o componentes se ejecutan en diferentes computadores conectados para lograr un objetivo común.***

#### Conceptos claves: 
1. Protocolos de comunicación
2. Coordinación y sncronización
3. Tolerancia a fallos
4. Consistencia de datos.

## Programación concurrente:
***Múltiples tareas o procesos que se traslapan en su ejecución y pueden interactuar entre si.***

#### Programación distribuida:
1. Programas que se ejecutan en multiples máquinas independientes.
2. Cada maquia con su CPU y memoria. Se comunican por red.
3. **Desafíos:** Fallas, latencia, consistencia, escalabilidad, etc.
#### Programación paralela:
1. Ejecución simultanea de tareas en varios CPUs o núcleos.
2. Procesadores comparten memoria, o tienen acceso a la memoria de los demás.
3. **Desafíos:** Sincronización, uso de memoria. consistencia, etc.

## Paradigmas de comunicación:
#### a) Control
Comunicación directa a través del paso de parametros y resultados.
#### b) Memoria compartida
Comunicación indireta mediante un espacio de almacenamiento de datos compartido. Requiere control de concurrencia.
#### c) Mensajes
Paso de mensajes y data streaming.
## Protocolos de redes de comunicación:
***Conjunto de reglas para que dos computadoras puedan hablar entre si***
#### Capas de la comunicación:
1. **Modelo TCP/IP:** Modelo real del internet con 4 capas principales. 
2. **OSI:** Modelo teórico con 7 capas. 

#### Calidad del servicio:
***Características y garantías que nos ofrece un protocolo de comunicación:***

1. **Desempeño:** Que tan rápida es la comunicación *(Latencia y throughput)*
2. **Control de flujo**
3. **Ordenamiento:** Orden de los mensajes
4. **FIabilidad:** Garantía de entrega
5. **Durabilidad:** Mensajes persistentes
6. **Seguridad:** Autenticación y control de confidencialidad.
#### Gestion de la comuniacación:
- **Endpoints:** E/S de la comunicación en cada programa. 
- **Coordinación:** Establecimiento, mantención y terminación de una conversación de manera estructurada.
- **Enlaces de comunicación:** Reserva de recursos en la red para garantizar una conversación. 
- **Memoria:** Almacenar temporalmente mensajes que se envían o reciben.

## Comunicación basada en mensajes:
#### Patrones de flujo:
- One to one
- One to many
#### Dirección:
- Unidireccional
- Bidireccional-
#### Sincronismo:
- Sincrónico
- Asincrónico
#### Ordenamiento de mensajes:
- Sin ordenamiento
- FIFO
- Orden parcial
- Orden total
#### Control de flujo:
- Regula flujo de mensajes.
#### Garantía de entrega:
***Más adelante se profundiza
- Maybe
- At least once
- At most once
- Exactly once
#### Persistencia:
- Transiente
- Persistente
#### Seguridad:
- Autenticación
- Cifrado
- Control de integridad.


## Sincronización de mensajes:
#### En el iniciador:
- Paso de mensaje unidireccional
- Request-Reply bidireccional.
#### En el receptor:
- Recepción explicita o implicita.
- Recepción selectiva
- Recepción con límite de tiempo.

## Multicasting:
***Un emisor transmite a un grupo de receptores simultáneamiente.***
- Grupo abstrae una unidad de interacción
- Distribución de datos eficiente y escalable
- Distribución de carga paralela.
- Descubrimiento de recursos.
- Útil para tolerancia a fallos.

**Desafíos:**
1. Escalabilidad y rendimiento
2. FIabilidad y consistencia
3. Seguridad.

#### Semántica de multicasting:
###### Entrega de mensajes:
- Semántica de entrega
	- Fiabilidad *(La calidad de los mensajes)*
	- Ordenamiento
- Semántica de respuesta:
	- Fiabilidad
	- Sincronización con el emisor
###### De grupo:
- Clausura:
	- Grupos cerrador
	- Grupos abiertos
- Simetría:
	- Simétricos: peer.
	- Asimétricos: Coordinador central.

# Comunicación entre procesos a través de sockets:

## API de Sockets:
***Una interfaz para comunicación entre procesos o maquinas***
***Un socket es escencialmente una tupla  \<id-puerto> que permite entablar una puerta de enlace para el envío y recepción de paquetes.***

### a) Sockets con UDP
**Endpoint que usa UDP para enviar y recibir mensajes datagramas. Lo principal relacionado con UDP, es que es un protocolo no orientado a la conexión y no fiable.

1. Servidor crea un socket UDP.
2. Lo liga a una dirección ip y número de puerto..
3. Se queda a la espera de que haya ruido en ese puerto.

4. El cliente crea su propio socket UDP y el sistema puede asigrnarle un puerto.
5. Para enviar un mensaje, crea un datagrama que contiene los datos de la ip y el servidor.
6. Envia el datagrama a través de su socket.

##### Pero porque? 
Baja latencia, velocidad, menos sobrecarga, soporte para multi y broadcast.

### b) Sockets con TCP
***Establece un canal de comunicación fiable, orientado a la conexión y basado enstram de datos.***

*La principal diferencia es que primero TCP establece una conexión, mientras que UDP no.*

1. Servidor crea un socket TCP.
2. Lo liga a una ip y puerto.
3. Pone el socket en modo listen, preparandoo para aceptar conexiones entrantes.
4. Espera que alguien se conecte.

5. El cliente crea su propio TCP
6. Inicia la conexión indicando direcctión y puerto.
7. Despues de aceptar la conexión, puedes armar un flujo continuo por el socket.

##### Pero porque?
Principalmente, fiabilidad. No tienes que preocuparte por pérdida de datos, etc; control de flujo, y control de congestión.

***Pero:*** Hay sobrecarga y latencia en comparación con UDP debido al handshake, confirmaciones, etc.

### c) Multicast IP
- **Abstraccion:** Es una abstracción del MC físico, donde escencialmente los Datagramas IP se transmiten a redes separadas.
- **Calidad de servicio:** Sin conexión, sin orden y entrega de mejor esfuerzo
- **Gestión de grupos:** Grupos dinámicos. El emisor no conoce los destinatarios de sus mensajes.

#### Direcciones Multicast:
- **IPv4:** 32 bits de clase D *(comienzan con 1110)*
	- 224.0.0.0 - 239.255.255.255
		- 224.0.0.0 no se usa
		- 224.0.0.1 a todos.
	- 224.0.1.0 - 238.255.255.255
		- Grupos a través de internet.
	- 239.0.0.0 - 239.255.255.255
		- Grupos privados.
- **IPv6:** Direcciones de 128 bits y comienzan con 0xff

#### Multicast e Internetworking:
***Como enviar un paqute a un grupo cuyos miembros están dispersos en redes diferentes.***
##### Red sobrepuesta:
Los routers no pueden usar las tablas de ruteo normales. En ves, deben construir una red sobrepuesta, o un arbol de distribución lógico. Escencialmente es una red virtual construida sobre la infraestructura del internet dedicada a enrutar tráfico multicast.
##### Limitar el alcance:
Fundamental ya que un paquete puede terminar en todas partes del internet.
+ **En ipv4:** Usando TTL
+ **En ipv6:** Usando el campo scope que define si es para una red local, un sitio, organización, o el mundo.
#### Gestión de grupos en multicast:
- **Protocolo IGMP:** Usado por maquinas para reportar su membresia a routers cercanos.
- **Routers:** Intercambian información periodicamente sobre estado de membresía en su red.
	- Aparece Protocol.Independent Multicast para ruteo.
	- Uso de tunneling para enviar paquetes a través de redes sin multicasting.
- *Send() y Recieve()*
- *JoinHostGroup() y LeaveHostGroup()*


#### Evaluación:
##### Soporte
No es bien soportado en internet ya que no todas las redes son compatibles, consume recursos, la configuración es compleja, etc.
Por otro lado, con IPv6 soporta mejor el multicast, pero sigue siendo poco frecuente.


# Intercambio de datos en ambientes distribuídos:
## Representación de datos:
***Surge de la necesidad de que los datos sean heterogeneos, puedan operar entre si siguiendo un estandar común.***
##### Solucion:
Formatos de estándares de representación de datos y metodos de serialización y deserialización de los datos.

## Serialización y deserialización de datos:
#### Marshalling:
Ensamblar en el emisor los datos a ser intercambiados.
#### Unmarshalling:
Proceso inverso, donde el receptos determina para un programa los valores de variables.

## Protocolos de intercambios de datos:

#### Formatos de representación de los datos:
- **Binario:** Compacto y eficiente, pero solo legible para maquinas. 
- **Textual:** Strings de caracteres, legibles por humanos, menos eficiente y requiere mayor procesamiento para parsing de caracteres.
#### Técnicas de codificación:
- **Autocontenida:** Datos se autodescriben. 
	- Interpretación de mensajes independiente al emisor.
	- Puede ser binaria o textual.
- **Acordada:** Partes comparten formato de codificación correcta.

# Invocación remota:
***Mecanismo de comunicación entre procesos que permite invocar funciones en otros procesos.***
- Abstrae la comunicaciónd de red generando transparencia de acceso.
## STUB:
**Ayudantes que facilitan la comunicación entre dos pares de manera transparente.**
##### Ejemplo simple:
Como gerente quieres enviar una orden al director de operaciones en Alemania.
1. Tu asistente *(Stub)* recibe tu orden en español.
2. El asistente traduce la información a un formato neutro. *(Marshalling)*
3. El asistente envía el mensaje.
4. El asistente remoto *(Stub)* recibe el mensaje y lo desempaqueta del lenguaje neutro al lenguaje del director alemán.
5. El asistente remoto entrega el paquete al director quien lo lee en su idioma.

##### Desafíos:
- Latencia
- Serialización
- Fallas parciales
- Seguridad

## Generación automátiva de STUBS:
***Uso de IDL***
- El IDL escencialmente describe la interfa de un servicio remoto de manera neutral, sin ligarse a algún lenguaje.
#### Proceso:
1. Se define un contrato IDL en formato .idl
	1. Este tiene la función de traducir, y de obtener idiomas soportados.
2. Usando un compilador de IDL generamos un codigo fuente para el LP a elección.
3. El compilador produce archivos con métodos para lo que es el proceso de marshalling, comunicación, y unmarshalling.
4. Ambas partes importan los archivos de traducción. 

## Ligado dinámico:
Gracias a la creación de un intermediario, el cliente y servidor pueden conectarse sin saber sus ubicaciones de antemano, un servidor de nombres.


## Descubrimiento y ligado en invocaciones remotas:
#### Descubrimiento:
1. **Configuración estática**
2. **Portmapper:** mapea nombre del servicio en puerto en maquina fija
3. **Descubrimiento integrado**
4. **Servicios de directorio**
5. **Servicios de registro**
#### Tipos de ligados:
- **Estático:** No requiere resolver, inflexible.
- **Dinámico:** Dirección del servidor se resuelve en ejecución.
- **Stub Cliente:** Actúa como proxy y resuelve transparentemente.

## Transparencia de invocaciones remotas:
***Diferencias entre local y remota**
- **Rendimiento**
- **Paso de parametros:** Sin memoria compartida es dificil la transparencia.
- **Fiabilidad:** Procesos pueden fallar

## Semántica de fallas en invocaciones remotas:
***Las cosas pueden salir mal si invocas una función remota, entre eso, fallas de servidor, perdidas de mensajes, etc; La semántica de fallas define qué garantía tienes como programador sobre si se ejecutó o no la operación.

**Op:** Número de veces que el servidor ejecuta la operación.
**Res:** Número de veces que el cliente recibe el resultado.

#### 4 garantías:

1. ***Maybe:*** Es la menos fiable. Se envía el mensaje una vez y se olvida. Si se falla, o se pierde no se reintenta.
2. ***At least once:*** Se asegura que llegó el mensaje al servidor. Si no recibe la confirmación lo reenvía. El riesgo es que el servidor puede recibir el mensaje duplicado.
3. ***At most once:*** Si el servidor recibe un mensaje reenviado lo ignora. O llega una vez, o no llega.
4. ***All or nothing:*** O el mensaje se envía y el servidor lo recibe, o la operación de cancela por completo, como si no hubiese sido enviado.
![[Pasted image 20250910224318.png]]

## Variaciones al modelo de inovación remota:
- **Idempotencia:** Repetición del procesamiento de una petición produce el mismo resultado
- **Renuncia a la respuesta:** Solo existe petición.
- **Delegación:** Respuesta puede ser generada por terceros.
- **Llamada de vuelta:** Se pasa una dirección del cleitne para realizar invocaciones inversas.
- **Streaming de múltiples peticiones y/o respuestas:** Flujo de peticiones/respuestas sin sincronización.
- **Invocación múltiple:** Tipo multicast.

## Conclusiones sobre invocación remota:
#### Ventajas:
- Uso de un paradigma bien conocido por los programadores facilita programación distribuída.
- Abstrae comunicación remota.
- Modelo apoya bien uso de procesos y hebras para mayor concurrencia o paralelismo.
- Reduce esfuerzo de desarrollo al automatizar generación de código para lógica de comunicación y manejo de mensajes.
- integra bien otros servicios de apoyo requeridos.

#### Desventajas:
- Define modelo de comunicación acoplado.
- Requiere sincronizar cliente con servidor.
- Uso de entornos distribuídos es complejo.
- No existen estándares comunes bien establecidos en la industria. Es bastante diverso.
