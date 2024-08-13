import argparse


def mult(a, b):
    print("Mult =", a * b)

def summ(a, b):
    print("Sum =", a + b)

parser = argparse.ArgumentParser(
    prog="calculator",
    description='Perform addition or multiplication on two numbers.',
    epilog="So there are two options for operations with numbers",
    )

parser.add_argument('operation', choices=['s', 'm'], 
                        help='Operation to perform: s for sum, m for multiplication')
parser.add_argument('a', help='the first number', type=int)
parser.add_argument('b', help='the second number', type=int)

args = parser.parse_args()

if args.operation == 's':
    summ(args.a, args.b)
elif args.operation == 'm':
    mult(args.a, args.b)
