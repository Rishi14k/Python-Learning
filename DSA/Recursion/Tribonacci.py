def tribonacci(trib):
    if trib == 0 or trib == 1:
        return trib
    if trib == 2:
        return 1

    return tribonacci(trib-1) + tribonacci(trib - 2) + tribonacci(trib - 3)

print(tribonacci(4))