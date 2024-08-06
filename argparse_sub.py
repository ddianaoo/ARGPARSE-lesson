import argparse

parser = argparse.ArgumentParser(description='Math Operations')

# Create sub-parsers
subparsers = parser.add_subparsers(dest='operation', help='Available operations')

# Create a sub-parser for the 'add' operation
add_parser = subparsers.add_parser('add', help='Addition')
add_parser.add_argument('numbers', nargs='+', type=int, help='Numbers to add')

# Create a sub-parser for the 'subtract' operation
subtract_parser = subparsers.add_parser('subtract', help='Subtraction')
subtract_parser.add_argument('numbers', nargs='+', type=int, help='Numbers to subtract')


args = parser.parse_args()


if args.operation == 'add':
    result = sum(args.numbers)
elif args.operation == 'subtract':
    result = args.numbers[0] - sum(args.numbers[1:])

print(result)

# python3 argparse_sub.py add 2 3 4 
# python3 argparse_sub.py subtract 2 3 4