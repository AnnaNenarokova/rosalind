source = 'one two three one two four'.split(' ')
counter = {}

for word in source:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print counter
