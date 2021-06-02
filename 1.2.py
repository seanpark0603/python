dna = ' gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg '
dna = dna.replace(" ", "")
dna = dna.replace("a", "A")
dna = dna.replace("t", "a")
dna = dna.replace("A", "t")
percent = (dna.count("gc")/len(dna))*100
