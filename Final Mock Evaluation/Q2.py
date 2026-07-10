sentence = input("Enter your sentance: ")

word = sentence.split()

freq = {}

for x in word:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for x in freq:
    print(x, freq[x])