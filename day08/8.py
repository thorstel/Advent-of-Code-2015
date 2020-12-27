import fileinput

string_code = 0
string_values = 0
new_encode = 0

for line in fileinput.input():
    xs = line.strip()
    string_code += len(xs)
    new_encode += 2 + len(xs) + sum(1 for x in xs if x in ['"', '\\'])
    xs = xs[1:-1]
    while xs:
        if xs[0] != '\\':
            string_values += 1
            xs = xs[1:]
        else:
            x = xs[:2]
            string_values += 1
            if x == '\\"' or x == '\\\\':
                xs = xs[2:]
            elif x == '\\x':
                xs = xs[4:]
            else:
                assert False

print(string_code - string_values)
print(new_encode - string_code)
