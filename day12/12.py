import fileinput
import json
import re

pat = re.compile(r'-?\d+')
ans1 = 0
ans2 = 0

def obj_val(obj):
    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        else:
            return sum(obj_val(x) for x in obj.values())
    elif isinstance(obj, list):
        return sum(obj_val(x) for x in obj)
    elif isinstance(obj, int):
        return obj
    else:
        return 0

for line in fileinput.input():
    ans1 += sum(int(x) for x in re.findall(pat, line.strip()))
    ans2 += obj_val(json.loads(line.strip()))

print(ans1)
print(ans2)
