# Program for TRY ,EXCEPT and Finally

import argparse
parser = argparse.ArgumentParser(description = "reversing a file")
parser.add_argument('filename', help = 'enter a filename')
parser.add_argument('--version', '-v',action = 'version', version= '%(prog)s 2.0')
parser.add_argument('--limit','-l',type = int, help = 'enter the number of lines')
args = parser.parse_args()
try :
    f = open(args.filename)
except IOError as err:
    print("file not found")
else:
    limit = args.limit
    with f:
        lines = f.readlines()
        lines.reverse()
        if limit:
            lines = lines[:limit]
        for line in lines:
            print(line.strip()[::-1])
finally :
    print("end of file")

