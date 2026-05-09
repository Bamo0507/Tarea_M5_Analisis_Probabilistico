# Se usó Claude Code (claude sonnet 4.6)
import random

def count_inversions(arr):
    total_inversions = 0
    for left_index in range(len(arr)):
        for right_index in range(left_index + 1, len(arr)):
            if arr[left_index] > arr[right_index]:
                total_inversions += 1
    return total_inversions

def expected_inversions(n):
    return n * (n - 1) / 4

def verify_experimentally(n, trials):
    total_inversions_accumulated = 0
    for _ in range(trials):
        permutation = list(range(1, n + 1))
        random.shuffle(permutation)
        total_inversions_accumulated += count_inversions(permutation)
    return total_inversions_accumulated / trials

# Configuración
N = 10
TRIALS = 10_000

theoretical = expected_inversions(N)
observed_average = verify_experimentally(N, TRIALS)

print(f"n: {N}")
print(f"Teorico n*(n-1)/4: {theoretical}")
print(f"Observado promedio de inversiones: {observed_average:.4f}")
print(f"Diferencia: {abs(theoretical - observed_average):.4f}")
