username = "chaiaurcode"

def func():
    username = "chai"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)


def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()