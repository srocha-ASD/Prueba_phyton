f = open('DIVIPOL_20220509_103027_01 (2) (1).txt', 'r')

array = []
for line in f:

    words = line[0:2].split()

    array.append(words)

f.close()

print(array)


    