import sys 


def mult(a, b):
    print("Mult =", int(a) * int(b))

def summ(a, b):
    print("Sum =", int(a) + int(b))


print("Output:")
if sys.argv[1] == '-s':
    summ(sys.argv[2], sys.argv[3])
elif sys.argv[1] == '-m':
    mult(sys.argv[2], sys.argv[3])    
else:
    print('No operation arguments were passed!')