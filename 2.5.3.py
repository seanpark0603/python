d = {'g' : 0, 'c' : 0, 't' : 0, 'a' : 0}
l = {}
dna = 'gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg'
l = list(dna)
for i in l :
    d[i] += 1
print('g | ', end = "")
while d['g'] > 0:
    print('-', end = "")
    d['g'] -= 1
print("\n")
print("c | ", end = "")
while d['c'] > 0:
    print('-', end = "")
    d['c'] -= 1
print("\n")
print("t | ", end = "")
while d['t'] > 0:
    print('-', end = "")
    d['t'] -= 1
print("\n")
print("a | ", end = "")
while d['a'] > 0:
    print('-', end = "")
    d['a'] -= 1
print("\n")
