x = 0

def foo():
    global x
    print("x inside:", x)
    x = x + 1


foo()
print("x outside:", x)