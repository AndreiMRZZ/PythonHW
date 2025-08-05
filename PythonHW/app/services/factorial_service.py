def factorial_calc(n: int):
    if n < 0:
        raise ValueError("numar negativ")

    cnt = 1
    for i in range(2, n+1):
        cnt *= i

    return cnt