# Program to call subprocess or outside commands
import subprocess
#code = subprocess.call(['ls', '-l'])
'''if code == 0:
    print("the command finishes successfully")
else:
    print("failed with code %i" %code)
'''
output = subprocess.check_output(['ls', '-l'])
print(output)