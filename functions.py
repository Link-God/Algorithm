import sys
import re

print(sum((int(x) for x in re.findall(r'-?\d+', ' '.join(line for line in sys.stdin)))))
