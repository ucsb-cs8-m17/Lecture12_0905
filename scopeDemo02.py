

# This results in an error

result = "foo"

def squared(x):
    print(result)
    result = x*x
    print(result)
    return result

if __name__=="__main__":
 
    print(squared(3))

