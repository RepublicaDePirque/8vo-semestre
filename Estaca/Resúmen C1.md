# Tema 1: Introducción
## Teoría de probabilidades:
***Modela un fenómeno aleatorio y calcula probabilidades asociadas***

## Inferencia estadística:
***Usa datos para sacar conclusiones.***

## Análisis exploratorio:
***Describe los datos***

#### Herramientas:
- Tablas de frecuencias
- Gráficos

#### Histogramas:
1. Calcular rango $x_{max} - x_{min}$
2. Elegir K clase.
3. Amplitud de la clase: A = R/K

- Sturges: K = $\log{_2}{(n)} + 1$
- Raíz cuadrada: K = $\sqrt(n)$
- Freedman-Diaconis: A = $2*IQE*n^{-\frac{1}{3}}$

## Muestreos:
1. **Aleatorio**
2. **No aleatorio**

## Tipos de variables:
1. **Cualitativas:**
	1. Ordinales
	2. Categóricas
2. **Cuantitativas:**
	1. Intervalares
	2. Razón
	3. Discretas
	4. Continuas
## Dimensionalidad:
1. **Univariados**
2. **Bivariados**
3. **Multivariados**

# Tema 2: Fundamento teoría de probabilidades

## Experimento aleatorio:
***Mismas condiciones, posibles diferentes resultados***

## Espacio muestral:
***Conjunto de posibles resultados***

## Evento:
***Subconjunto del espacio muestral $\Omega$ 

## Medida de probabilidad:
***Función que asigna 0 o 1 a cada evento.***

#### Propiedades:
1. $P(\Omega) = 1$
2. $P(\emptyset) = 0$
3. $P(A \cup B) = P(A) + P(B)$ para eventos disjuntos

## Reglas básicas:
- **Complemento:** $P(A^c) = 1 - P(A)$
- **Union:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- **Intersección es lo mismo**
- **Diferencia:** $P(A - B) = P(A) - P(A \cap B)$

## Conteo y principio multiplicativo:
***Descomponer en etapas -> Producto de posibilidades de cada etápa.***

#### Probabilidad clásica
***Resultados igualmente probables:***

- $P(A) = \frac{\mid A \mid}{\mid \Omega \mid}$
- ***Escencialmente $\frac{Ocurrencias}{Total}$

#### Permutaciones:
***Cuantas formas podemos elegir k elementos en un orden***

$P_{k,n} = \frac{n!}{(n - k)!}$

#### Combinatoria:
***Cuantas maneras podemos elegir k elementos de n-total elementos***

$C_{k,n} = \binom{n}{k} \frac{n!}{(n - k)!}$


## Probabilidad condicional:
***Probabilidad de A dado que ocurre B***
- $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$
- $P(A^c \mid B) = 1 - P(A \mid B)$
-  $P(A \mid B^c) \neq 1 - P(A \mid B)$

#### Independencia:
**A independiente de B si:**
- $P(A \mid B) = P(A)$
- $P(A \cap B) = P(A)P(B)$

#### Teorema de Bayes:
-  $P(A \mid B) = \frac{P(B|A)}{P(A)}$

#### Regla de la probabilidad total:
- $P(A) = \sum{P(A|B_{i}) * P(B_{i})}$


# Tema 3: Variables aleatorias

## Variable aleatoria: 
***Es una función que asigna un valor numérico a cada posible resultado de un experimento aleatorio. Se dice que es discreta si puede tomar valores finitos o numerables.***

## Función de probabilidad:
***Es una función denotada por f que entrega laprobabildad exacta de que la variable aleatoria X tome un valor especifico.***

- $f(x) = P(X = x)$

*Escencialmente cual es la probabilidad de que ocurra exactamente ese valor.*

## Medida de probabilidad inducida y propiedades:
#### Cálculo de probabilidades en intervalos:
**Se suman las probabilidades de cada valor.**
#### Requisitos:
**La suma de todo tiene que ser 1.**

## Función de distribución acumulada FDA:
***Obtener un valor hasta x***

## Valor esperado:
***Esperanza indica escencialmente el valor promedio que se esperaría obtener si el experimento se repite muchas veces.***

$E(X) = \sum{x_{i}*f(x_{i})}$

## Varianza o desviación estándar:
***Representa la dispersión de los valores respecto a la esperanza.***

- $Var(X) = \sum{(x_{i} - E(X))^2 * f(x_{i})}$
- Donde la desviación estándar s la raíz de Var.

## Distribuciones discretas:
#### Bernoulli:
**Puede tomar solo 2 valores**

![[Pasted image 20250912234120.png]]
**Si X es Ber(p):**
- $E(X) = p$
- $E(X^2) = p$
- $Var(X) = p(1-p)$

#### Binomial:
**Puede tomar o no tomar un valor***
![[Pasted image 20250912234352.png]]
**Si X es Bin(n,p):
- $E(X) = np$
- $Var(X) = np(1-p)$
- si p = 0,5 el gráfico es simétrico, si p > 0.5, está hacia la derecha, y a la izquierda si p < 0.5.

#### Poisson:
**Número de veces que ocurre un evento en particular durante un intervalo.**

![[Pasted image 20250912235226.png]]

**Si X es Pos($\lambda$):
- $E(X) = \lambda$
- $Var(X) = \lambda$
- Gráfica siempre hacia la izquierda.

#### Geométrica:

##### Repeticiones:
*Número de repeticiones hasta la primera ocurrencia.*
![[Pasted image 20250912235618.png]]
##### Fracasos:
*Número de fracasos hasta la primera ocurrencia.*
![[Pasted image 20250912235749.png]]
**Si X es Geo(P):**
*Y X el número de fracasos hasta la priemra ocurrencia*
- $E(X) = (1-p)/p$
- $Var(X) = (1-p)/p^2$
	- Gráfico concentrado a la izquierda.

#### Binomial Negativa:

##### Repeticiones:
*Número de repeticiones hasta lograr observar el evento una cantidad FIJA de veces*
![[Pasted image 20250913000217.png]]
##### Fracasos:
*Número total de FRACASOS hasta lograr observar el evento una cantidad FIJA de veces. El número total de repeticiones es r + X*
![[Pasted image 20250913000342.png]]

**Si X es $Bin^{-1}(n,p)$:**
*Y X el número de fracasos hasta la ocurrencia de los r éxitos*
- $E(X) = \frac{r(1-p)}{p}$
- $Var(X)=\frac{r(1-p)}{p^2}$
- Gráfica concentrada a la izquierda.

#### HiperGeométrica:
**De una población de N elementos, M son exitosos, y N-m son fracasos. Sirve para calcular cual es la probabilidad de tomar una muestra de n elementos sin reemplazarlos y obtengamos exactamente k elementos**
![[Pasted image 20250913000920.png]]
**Si X es HiperGeo(N,M,n):
- $E(X) = n(\frac{M}{N})$
- $Var(X) = (\frac{N-n}{N-1})n(\frac{M}{N})(1-\frac{M}{N})$
