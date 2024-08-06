import argparse


parser = argparse.ArgumentParser(
    description='Perform writing given message to a file',
    )

parser.add_argument('-f', '--file', help='filename')
parser.add_argument('-msg', '--message', help='message string')

args = parser.parse_args()
message = args.message
file = args.file

with open(file,'w') as f:
     f.write(message.swapcase())
