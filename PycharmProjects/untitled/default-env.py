#default environmentable variable

import os


stage = os.environ["STAGE"].upper()
output = "we're running in %s" % stage

if stage.startswith("PROD"):
    output = "DANGER!!!!" + output

print(output)
