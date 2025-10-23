n = 10
k = 0

for i in range(n // 2, n):
    j = 2
    while j <= n:
        k += n // 2
        print(f"i = {i}, j = {j}, k = {k}")
        j *= 2

print(f"Final value of k: {k}")

# Linearithmic time complexity (O(n log n)) is generally considered to be more efficient than quadratic time complexity (O(n^2)) but less efficient than linear time complexity (O(n))