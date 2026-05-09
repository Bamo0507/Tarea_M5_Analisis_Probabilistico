# Análisis Probabilístico

## Random(a,b)

1. Bajo el rango de pruebas que se han hecho y los valores que se han utilizado, se confirmó que la distribución de salida es uniforme. Por ejemplo, para el rango entre 3 y 7 sobre 100,000 pruebas:
- El 3 salió 19.764 veces.
- El 4 salió 20.070 veces.
- El 5 salió 20.086 veces.
- El 6 salió 20.110 veces.
- Y 19.970 para el 7.
Las pequeñas diferencias observadas entre valores son variación estadística esperada en una muestra finita. Cada valor aparece muy cercano a 1/5 de las veces, lo cual es consistente con una distribución uniforme.

2. El número promedio de intentos en la teoría se dice que iba a ser 1.6 en este caso específico. Utilizando la función de 2 elevado a la cantidad de bits necesarios (k = ceil(log2(5)) = 3), partido la cantidad de posibles resultados que era lo que nosotros obteníamos como b (minúscula) menos a (minúscula) más 1, se sacaba el 1.6. La probabilidad real observada fue mínimamente mayor, siendo de 1.6026, dando una diferencia de tan sólo 0.0026.

## Dessesgar

1. Al realizar el desarrollo práctico de esto, se logró evidenciar que, al realizar cien mil pruebas y haber colocado una probabilidad de la moneda desfavoreciendo un lado por 0.7 en cada uno de los posibles resultados (cara o cruz), casi apareció la misma cantidad de veces. Cero salió 50.338 veces y el 1, 49.662. Estadísticamente, esto es algo que podemos esperar: que no fuera exactamente 50-50, pero muy cercano a ese valor, que es justamente lo que hemos obtenido.
2. Si coincide con el estimado, teóricamente se esperaban 4.7619 llamadas, mientras que realmente se necesitaron 4.7770, una diferencia bastante baja, ya que esta es solo de 0.0151. Como se discutió en la teoría, el funcionamiento de esto era paradójico, ya que mientras más sesgada estaba la moneda, mayor iba a ser la cantidad de intentos que se tenían que realizar. Esto tiene sentido, ya que esto afecta directamente la posibilidad de que tengamos el mismo resultado en los dos lanzamientos, lo que nos llevaría a tener que repetir el intento, ya que solamente estamos trabajando con las combinaciones de 0,1 y 1,0.

## Hiring

1. Efectivamente, tras realizar las 100,000 iteraciones, la cantidad de contrataciones realizadas fue muy similar entre lo teórico y lo práctico. La teoría nos dice que las contrataciones serían aproximadas por el logaritmo natural de n, aunque el valor teórico exacto es el número armónico Hn. Con el n utilizado, se esperaba un resultado de 2.7179. Al ejecutar el código, se encontró un promedio de contrataciones de 2.7131.
2. El mejor caso ocurrió muy cerca de lo esperado, presentándose en un 12.57% de las ocasiones, frente al 12.50% teórico.
3. El peor caso tuvo una presencia bastante baja, siendo de tan solo 0.0020%, por lo que el algoritmo se podría decir que no tiene un sesgo hacia este escenario. Esto es lógico ya que para que ocurra necesitaríamos que los candidatos llegaran en orden estrictamente creciente de calidad, es decir, el peor primero y el mejor al final.

## Dados

1. Efectivamente, el promedio empírico se mantiene a la hora de llevarlo de la teoría a la práctica. Al hacer las pruebas con los dados, se observó el promedio por dado 3.4989, cuando la teoría esperaba 3.5, teniendo una diferencia bastante baja en 0.0011. La linealidad de la esperanza en este caso es bastante importante, porque permite analizar cada dado de forma individual y simplemente sumar sus esperanzas, sin necesitar conocer cómo interactúan entre sí. Esto funciona incluso si los dados no fueran independientes, lo que elimina la necesidad de estudiar la distribución conjunta de todos los dados a la vez.

## Inversiones

1. Efectivamente, el promedio de inversiones tras realizar las 10.000 permutaciones aleatorias converge en el punto indicado. Los resultados en la práctica fueron de 22.4305; el teórico se esperaba que fuera de 22.5, ya que se probó con un N de 10. Con esto se corrobora que se cumple lo dicho sobre la esperanza, en donde, a pesar de no tener independencia sobre los valores entre pares, la linealidad de la esperanza permite sumar las esperanzas individuales de cada par y llegar al resultado correcto.