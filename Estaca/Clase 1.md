**Objetivos**: Obtener conclusiones acerca de un fenomeno aleatorio mediante recolección de datos y posterior analisis.
1. Analisis exrploratioro de datos
2. Probabilidad
3. Inferencia
4. Data

***Teoria de las probabilidades:*** Obtener conclusiones acerca de un fenomeno aleatorio a partir de un modelo. 
- *Siempre definir las variables para el certamen. Por ejemplo: El tiempo se denota por X*

***Objetivo de la ingerencia:*** Obtener conclusiones acerca de un fenómeno a partir de datos experimentales.

*Un poco la diferencia entre ambos, es que uno entrega conclusiones con datos y el otro no*


## Conceptos clave:
- **Población:** Conjunto de los elementos a caracterizar.
- **Variable:** Caracteristica que nos interesa medir.
- **Muestra:** Subconjunto finito representativo.
- **Datos**

## Tipos de muestreo:
Diremos que la muestra es aleatoria si cada elemento tiene la misma posibilidad de ser muestreado.
- *De momento asumimos una muestra de tipo aleatorio.*
- *En el caso de poblaciones conceptuales, el supuesto anterior se puede formalizar usando una definición matemática de independencia. ¿Que quiere decir esto? Podemos asimilarlo a un estudio estadistico con reposición.*


# Análisis exploratorio de datos
**Objetivo:** Generar representaciones gráficas y numéricas que describan y resuman los datos para encontrar hipótesis acerca de la población, detectar patrónes, relaciones, identificar errores o eventos anómalos en las mediciones, etc. 
- Visualización
- Agregación

***Tipos de datos:***
**Taxonomía de Stevens:** 
- Cualitativos: No son operables aritméticamente.
	- Pueden ser:
		- Categóricas: Valores que solo soportan la operación igual o distinto.
		- Ordinales: Soportan además las operaciones > y <.
- Cuantitativos: Valores operables. 
	- Pueden ser:
		- Intervalares: Cuando el valor 0 es arbitrario y no indica ausencia de variable. Asigna números para posición en escala. Por ejemplo 0°C, ya que es 0 pero si existe. *Valen todos los operadores menos \* y /*
		- De razón: Cuando existe un 0 absoluto. Por ejemplo la temperatura en Kelvin. *Si incluye \* y /*
- **Además:**
	- Discretas: Conjunto finito o infinito numerable de valores.
	- Continuas: Cualquier valor. 
***Dimensionalidad:***
- **Univariadas:** 1 cantidad.
- **Bivariadas:** 2 cantidad
- **Multivariadas:** Más 

# Visualización de datos:
Generar representaciones gráficas.

***Frecuencias absolutas y relativas:***
- Absoluta: Cantidad de un valor c.
- Relativa: Absoluta/total.

***Diagrama de torta:*** El área de cada sector es proporcional a la frecuencia del valor correspondiente. 
- Son complejos de visualizar.

***Diagrama de barra:*** Secuencias de barras de igual anchoy equivalen a la frecuencia de el dato en el estudio.

***Taligrama:*** ????

***Diagramas de puntos:*** Útil para datasets pequeños.

***Histogramas:*** Escencialmente barras pero con intervalos.

**Para hacer un histograma:**

- Dado un valor de K, sea:
	- xmax = max(x1,x2,...,xn)
	- xmin = min(x1,x2,...,xn)
 - Para determinar K:
	 - Sturges: K = \[log2(n)] + 1
	 - Raíz cuadrad: K = sqrt(n)
	