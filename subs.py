import re
s = 'CGAACTGTGAAGGCCTGTGAAGTGTGAAGCTGTGAAGTGTGAAGTGTGAAGCCCTGGTGTGAAGTCTGTGAAGAGTAAGTGTGAAGGTGTGAAGTGTGAAGTTGTGAAGTGTGAAGATGTGAAGTGTTGGATGTGAAGCCCTGTGAAGGACTACACTACCTTGTGAAGACGTGTGAAGCGTGTGAAGAGTCGTGTGAAGTGTGAAGTTACCGCTGTGAAGGCTGTGAAGCTGCATGTGAAGTCTGTGAAGGGAGTGTGAAGGGGTGTGAAGGCGTGTGAAGGTGTGAAGTTGTGAAGCACGTGTGAAGATGATGTGAAGTTGTGAAGAGCTGTGAAGAGTCTGTGAAGAAGTGTGAAGATTGTGAAGCTGTGAAGTGTGAAGATGTGAAGCATGTGAAGATGTGAAGCGCCGTGTGAAGAGCCTGTGAAGAACCCTTATACAATGTGAAGGATTGTGAAGGCTGTGAAGATTGTGAAGCGATGTGAAGCTGTGAAGTGTGAAGACATGTGAAGGAGTTTTATGTGAAGGCTGTGAAGGATATTGTGAAGAAGTTGTGAAGTGTGAAGTTGCTGTGAAGTCTAAAAATGTGAAGACTGTGAAGTGTGAAGTATGTGAAGTGTGAAGCTGTGAAGGGTTGCTGTGAAGCTGTGAAGTCTTGTGAAGTGTGAAGATGTGAAGCTTGTGAAGTTGTGAAGCTGTGAAGTGTGAAGTGTGAAGCTGTGAAGCGTGTGAAGTGGGAGCTGTGTGAAGTACATTGTGAAGTCCTATGTTGTGTGAAGTGTGAAGTGTGAAGTGTGAAGGCCGTGTGAAGTGTGAAGTGTGAAGCTGTGAAG'
result = [m.start() + 1 for m in re.finditer('(?=TGTGAAGTG)', s)]
for i in result:
    print i,
