

x = "global x"
y = "global y"
z = "global z"

def foo():
    print(x)
    print(y)
    print(z)
    z = "local z"

def bar():
    y = "local y"
    print(x)
    print(y)
    print(z)

def fum():
    print(x)
    print(y)
    z = "local z"
    print(z)
 
