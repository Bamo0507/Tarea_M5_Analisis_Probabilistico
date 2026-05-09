# Se usó Claude Code (claude-sonnet-4-6)
import random
import math

def biased_random(p):
    return 1 if random.random() < p else 0

def unbiased_random(p):
    total_calls = 0
    while True:
        first_flip = biased_random(p)
        total_calls += 1
        second_flip = biased_random(p)
        total_calls += 1

        if first_flip == 1 and second_flip == 0:
            return 1, total_calls
        if first_flip == 0 and second_flip == 1:
            return 0, total_calls

P = 0.7
TRIALS = 100_000

frequency = {0: 0, 1: 0}
total_calls = 0

for _ in range(TRIALS):
    bit, calls = unbiased_random(P)
    frequency[bit] += 1
    total_calls += calls

theoretical_expected_calls = 1 / (P * (1 - P))
observed_average_calls = total_calls / TRIALS

print(f"Distribucion de salida (p={P}, {TRIALS:,} pruebas)")
print(f"0: {frequency[0]}")
print(f"1: {frequency[1]}")
print(f"Promedio de llamadas")
print(f"Teorico E[llamadas]: {theoretical_expected_calls:.4f}")
print(f"Observado: {observed_average_calls:.4f}")
print(f"Diferencia: {abs(theoretical_expected_calls - observed_average_calls):.4f}")
