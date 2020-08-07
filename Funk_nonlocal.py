def func1():
    x=2
    print ("x равно", x)
    def func2():
        nonlocal x
        x=5
        print(x)
    func2()
    print("локальное х сменилось на", x)
func1()
print("2й проход_______________________")
def func3():
    y=2
    print ("y равно", y)
    def func4():
        global y
        y=5
        print(y)
    func4()
    print("локальное х сменилось на", y)
func3()