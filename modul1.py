from sys import argv

in_file, out_file = argv[1], argv[2]

s = 0

with open(in_file, 'r') as file:
    for line in file:
        if line == '\n':
            continue
        num = ''
        for index, el in enumerate(line):
            if el.isdigit():
                if (index - 1) >= 0 and line[index - 1] == '-':
                    num += '-' + el
                else:
                    num += el
            else:
                if len(num) > 0:
                    s += int(num)
                    num = ''
    if len(num) > 0:
        s += int(num)
        num = ''

s = s % 256
print(s)
with open(out_file, 'w') as file:
    file.write(str(s))
