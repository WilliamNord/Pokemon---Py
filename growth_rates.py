# "slow-then-very-fast"
def erratic(n):  
    if n <= 50:
        return n**3 * (100 - n) // 50
    if n <= 68:
        return n**3 * (150 - n) // 100
    if n <= 98:
        return n**3 * ((1911 - 10 * n) // 3) // 500
    return n**3 * (160 - n) // 100

#"fast-then-very-slow"
def fluctuating(n): 
    if n <= 15:
        return n**3 * (((n + 1) // 3) + 24) // 50
    if n <= 35:
        return n**3 * (n + 14) // 50
    return n**3 * ((n // 2) + 32) // 50

GROWTH_FORMULAS = {
    "medium": lambda n: n**3,
    "fast": lambda n: 4 * (n**3) // 5,
    "slow": lambda n: 5 * n**3 // 4,
    "medium-slow": lambda n: 6 * n**3 // 5 - 15 * n**2 + 100 * n - 140,
    "slow-then-very-fast": erratic,
    "fast-then-very-slow": fluctuating,
}

def exp_for_level(growth_rate: str, level: int) ->int:
    if level <= 1:
        return 0
    
    return max(0, GROWTH_FORMULAS[growth_rate](level))

