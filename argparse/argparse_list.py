import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--list', nargs='*')
parser.add_argument('--str-list', type=lambda args: args.split('-'))
parser.add_argument('--int-list', type=lambda args: list(map(int, args.split(','))), metavar='N')

args = parser.parse_args()
 
print(args.list)
print(args.str_list)
print(args.int_list)

# python3 argparse_list.py -h
# python3 argparse_list.py --list 1 2 3 --str-list a-b-c 
# python3 argparse_list.py --int-list 1,2,3,4
