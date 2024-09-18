import re, sys

data = ''
nrows = 0
nentries = 0

with open(sys.argv[1]) as file:
    for line in file:
        try:
            row = int(re.match(r'  row (\d*?):', line).group(1))
        except:
            continue

        pairlist = re.findall(r'\((\d*?), (.*?)\)', line)
        pairlist = [(int(col), float(val)) for col, val in pairlist if float(val) != 0]

        for col, val in pairlist:
            data += f'{row + 1} {col + 1} {val}\n'
        
        nrows += 1
        nentries += len(pairlist)

print('%%MatrixMarket matrix coordinate real general\n' + '%')
print(f'{nrows} {nrows} {nentries}\n' + data)
