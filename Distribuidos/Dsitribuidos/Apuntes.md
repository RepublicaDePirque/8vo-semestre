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


#### 