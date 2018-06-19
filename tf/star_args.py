def fun2(*args):
    print(args)

def fun1(*args):
    fun2(*args)


if __name__ == "__main__":
    fun1(1,2,3,4,5)


