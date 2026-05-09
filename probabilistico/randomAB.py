# Se usó Claude Code (claude-sonnet-4-6)
import random
import math

def random01():
    return 0 if random.random() < 0.5 else 1

def random_uniform(a, b):
    valid_range = b - a + 1
    bits_amount = math.ceil(math.log2(valid_range))

    attempts = 0

    while True:
        attempts += 1

        generated_bits = [random01() for _ in range(bits_amount)]

        # Transformar los bits a su número correspondiente
        generated_number = 0
        for bit in generated_bits:
            generated_number = generated_number * 2 + bit

        # Validar que el número esté dentro del rango válido
        if generated_number <= valid_range - 1:
            return a + generated_number, attempts

A = 3
B = 7
TRIALS = 100_000

frequency = {n: 0 for n in range(A, B + 1)}
total_attempts = 0

for _ in range(TRIALS):
    value, attempts = random_uniform(A, B)
    frequency[value] += 1
    total_attempts += attempts

expected_frequency = TRIALS / (B - A + 1)

print(f"\n=== Distribución de salida ({TRIALS:,} pruebas) ===")
print(f"Frecuencia esperada por número: ~{expected_frequency:.0f}\n")

for num, count in frequency.items():
    bar = "█" * (count // 500)
    print(f"  {num}: {count:6}  {bar}")

valid_range = B - A + 1
bits_amount  = math.ceil(math.log2(valid_range))
theoretical_expected_attempts = (2 ** bits_amount) / valid_range
observed_average_attempts     = total_attempts / TRIALS

print(f"\n=== Promedio de intentos ===")
print(f"Teórico  E[intentos] = 2^{bits_amount} / {valid_range} = {theoretical_expected_attempts:.4f}")
print(f"Observado = {observed_average_attempts:.4f}")
print(f"Diferencia = {abs(theoretical_expected_attempts - observed_average_attempts):.4f}\n")
