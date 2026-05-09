# Se usó Claude Code (claude-sonnet-4-6)
import random
import math

def hiring_algorithm(candidates):
    current_best = candidates[0]
    total_hires = 1

    for candidate in candidates[1:]:
        if candidate > current_best:
            current_best = candidate
            total_hires += 1

    return total_hires

# Configuración

N = 8
TRIALS = 100_000

total_hires_accumulated = 0
best_case_count = 0
worst_case_count = 0

for _ in range(TRIALS):
    candidate_order = list(range(1, N + 1))
    random.shuffle(candidate_order)

    hires = hiring_algorithm(candidate_order)
    total_hires_accumulated += hires

    if hires == 1:
        best_case_count += 1
    if hires == N:
        worst_case_count += 1

# Parte 1: E[contrataciones] vs ln(n)

observed_average_hires = total_hires_accumulated / TRIALS
theoretical_average_hires = sum(1 / i for i in range(1, N + 1))
ln_n = math.log(N)

print("Parte 1: promedio de contrataciones")
print(f"Observado: {observed_average_hires:.4f}")
print(f"Teorico Hn: {theoretical_average_hires:.4f}")
print(f"ln(n): {ln_n:.4f}")

# Parte 2: frecuencia del mejor caso

observed_best_case_frequency = best_case_count / TRIALS
theoretical_best_case_probability = 1 / N

print("Parte 2: frecuencia del mejor caso (1 contratacion)")
print(f"Observado: {observed_best_case_frequency:.4f}")
print(f"Teorico 1/n: {theoretical_best_case_probability:.4f}")

# Parte 3: frecuencia del peor caso

observed_worst_case_frequency = worst_case_count / TRIALS
theoretical_worst_case_probability = 1 / math.factorial(N)

print("Parte 3: frecuencia del peor caso (n contrataciones)")
print(f"Observado: {observed_worst_case_frequency:.6f}")
print(f"Teorico 1/n!: {theoretical_worst_case_probability:.6f}")
