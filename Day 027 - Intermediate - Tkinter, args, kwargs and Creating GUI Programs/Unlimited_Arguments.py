#  *args  **kwargs

def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum
print(add(4,3,5,6,7,8,4,3,1,2))