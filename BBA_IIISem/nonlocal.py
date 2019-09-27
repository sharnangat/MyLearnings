def f1():
    x="SICSR"
    def f2():
        nonlocal x
        y="SICSR College"

    f2()
    return x

print("Caling f1",f1())
