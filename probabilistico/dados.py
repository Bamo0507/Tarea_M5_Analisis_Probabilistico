# Se usó Claude Code (claude sonnet 4.6)
import random

def roll_die():
    return random.randint(1, 6)

def expected_sum():
    return sum(j * (1/6) for j in range(1, 7))

def simulate(n, trials):
    total = 0
    for _ in range(trials):
        roll_sum = sum(roll_die() for _ in range(n))
        total += roll_sum
    return total / trials / n

# Configuración
N = 10
TRIALS = 100_000

theoretical = expected_sum()
observed_average_per_die = simulate(N, TRIALS)

print(f"Dados: {N}")
print(f"Teorico promedio por dado: {theoretical}")
print(f"Observado promedio por dado: {observed_average_per_die:.4f}")
print(f"Diferencia: {abs(theoretical - observed_average_per_die):.4f}")
