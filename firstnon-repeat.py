arr = [1,2,2,3,3,4,4,4]
freq = {}

for item in arr:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

for i in freq:
    if freq[i] == 1:
        print(i)
        break