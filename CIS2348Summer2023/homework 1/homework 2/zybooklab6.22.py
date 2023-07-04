# Sara Umer 1999495

def solve_equations(a1, b1, c1, a2, b2, c2):
    for x in range(-10, 11):
        for y in range(-10, 11):
            if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
                return x, y
    return None

# Inputs that are entered will be : 
8
7
38
3
-5
-1

a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())


solution = solve_equations(a1, b1, c1, a2, b2, c2)


if solution is not None:
    x, y = solution
    print(f"{x} {y}")
else:
    print("No solution")
