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

