# Awful Sorting

## Comparaciones esperadas
Explique la fórmula usada para calcular P[Iₖ] en la prueba del Teorema 2 del paper "Sorting the Slow Way".
- Iₖ es el evento "se hace al menos la comparación k", es decir, que el algoritmo todavía no terminó antes de llegar a esa comparación.
- P[Iₖ] = 1/k!
- Cada comparación adyacente A[i] ≤ A[i+1] tiene una restricción de orden; combinarlas para k pares deja k! ordenamientos válidos sobre todas las posibilidades, dando 1/k!.

En la prueba del Teorema 2, ¿por qué E[C] = Σₖ₍>₀₎ P[Iₖ]?
- Esta es una identidad clásica de probabilidad para variables aleatorias no negativas enteras:
- E[X] = Σ_{k≥1} P(X ≥ k)
- E[C] = Σ_{k≥1} 1/k! = e − 1 ≈ 1.718
- Se lee como: "el valor esperado es la suma de las probabilidades de que X sea al menos k".
- En este caso, C es el número total de comparaciones, y P[Iₖ] = P[C ≥ k] (el algoritmo llega a hacer la k-ésima comparación). 


## Iteraciones de bogo-sort
¿por qué la variable aleatoria I que cuenta el número de iteraciones del algoritmo tiene distribución geométrica?
- P(ordenado tras un barajado) = 1/n!
- Iteraciones independientes ⇒ I ~ Geom(1/n!)
- P(I = k) = (1 − 1/n!)^{k−1} · (1/n!)
- E[I] = n!
- E[swaps] = (n − 1) · n!
- La distribución geométrica modela "cuántos intentos independientes se necesitan hasta el primer éxito". 
