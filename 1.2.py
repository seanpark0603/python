dna = ' gcatgacgttattacgactctgtcacgccgcggtgcgactgaggcgtggcgtctgctgggcctttacttcgcctccgcgccctgcattccgttcctggcctcg '
dna = dna.replace(" ", "")
dna = dna.replace("t", "a")
dna = dna.replace("a", "t")
percent = (dna.count("gc")/len(dna))*100
