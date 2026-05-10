# Se usó Github Copilot (gpt-4.0) para escribir este código.
import random

def factorial(n):
  return n <= 1 and 1 or n * factorial(n - 1)

# Retorna true si arr está en orden no-decreciente
def isSorted(arr):
  for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
      return False
  return True;


# Fisher-Yates shuffle in-place. Retorna número de swaps realizados (n-1).
def shuffle(arr):
  swaps = 0
  for i in range(len(arr) - 1, 0, -1):
    j = random.randint(0, i)
    arr[i], arr[j] = arr[j], arr[i]
    swaps += 1
  return swaps;


# Corre bogo-sort sobre permutación aleatoria de [1..n].
# Retorna { iterations, swaps, timedOut }
def bogoSortIterations(n, maxIter = 100000):
  # Permutación inicial aleatoria
  arr = [i + 1 for i in range(n)]
  shuffle(arr)

  iterations = 0
  swaps = 0
  while not isSorted(arr):
    swaps += shuffle(arr)
    iterations += 1
    if iterations > maxIter:
      return {'iterations': iterations, 'swaps': swaps, 'timedOut': True}
  return {'iterations': iterations, 'swaps': swaps, 'timedOut': False}


# ── Verificación de distribución geométrica ─────────
n = 4; # n! = 24 → fácil de simular
TRIALS = 5000
totalIter = 0
totalSwaps = 0
timedOut = 0

for t in range(TRIALS):
  r = bogoSortIterations(n)
  if (r['timedOut']):
    timedOut += 1
  else:
    totalIter += r['iterations']
    totalSwaps += r['swaps']


validTrials = TRIALS - timedOut
print(f"n={n} (n!={factorial(n)}), {TRIALS} ensayos:")
print(f"  E[iteraciones] simulado : {(totalIter/validTrials):.2f}")
print(f"  E[iteraciones] teórico  : n! = {factorial(n)}")
print(f"  E[swaps] simulado       : {(totalSwaps/validTrials):.2f}")
print(f"  E[swaps] teórico        : (n-1)·n! = {(n-1)*factorial(n)}")
if (timedOut > 0): print(f"  Timeouts: {timedOut}")
print('\n→ El histograma de iteraciones cae exponencialmente: firma geométrica.');
