def mod(fc):
    def mfc(*args, **koargs):
        print("\nFunction Start")
        fc(*args, **koargs)
        print("Function End\n")
    return mfc

@mod.setter #decorator
def add(a, b):
    print(a + b)

add(1,1)