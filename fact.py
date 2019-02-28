def fact(n):
    xif n < 1 :
        return 1
    return n * fact(n-1)

print(fact((int(input("n = ")))))
