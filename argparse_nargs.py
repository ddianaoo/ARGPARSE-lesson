import argparse 

parser = argparse.ArgumentParser(description='Example with nargs="?"') 
parser.add_argument('value', type=int, nargs='?', default=42, help='an optional integer argument') 
parser.add_argument('--optional', type=str, nargs='?', const='default_value', help='an optional argument with a constant') 
args = parser.parse_args() 
print('value:', args.value) 
print('optional:', args.optional)
