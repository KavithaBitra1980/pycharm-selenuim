#Exception Handling with Try

import argparse
parser = argparse.ArgumentParser(description= "the reversing the file")
parser.add_argument('filename', help = "enter a file name")
parser.add_argument("--limit","-l", type=int, help='enter the lines to read')
parser.add_argument("--version","-v",action="version",version='%(prog)s2.0')
args=parser.parse_args()
try:
    f = open(args.filename)
except IOError as err:
    print("Error: File not found")
else:
    with f:
        limit = args.limit
        lines=f.readlines()
        lines.reverse()
        if limit :
            lines=lines[:args.limit]
        for line in lines:
            print(line.strip()[::-1])
finally:
    print("end of file")