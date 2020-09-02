# 1

print("uppgift 1")
def square(sq):
    for i in range(0, sq):
        for x in range(0, sq):
            print(f'{i}', end='')
        print()


sq = 10
square(sq)

# 2

print("uppgift 2")

def triangle1(n):
    for i in range(0, n):

        print(' ' * i, end='')
        for j in range(0, n - i):
            print(j, end="")

        print()


n = 8

triangle1(n)


# 3

print("uppgift 3")

def triangle2(n2):
    for i in range(0, n2):

        for j in range(0, n2 - i):
            print(j, end=" ")

        print()


triangle2(n)

# 4

print("uppgift 4")

def triangle3(n3):
    for i in range(0, n3):
        print(' ' * i, end='')
        for mirrored in range(n3 - 1 - i, -1, -1):
            print(str(mirrored), end='')

        for normal in range(1, n3 - i):
            print(str(normal), end='')
        print()


n3 = 10
triangle3(n3)
