def compute_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return compute_fibonacci(n-1) + compute_fibonacci(n-2)
