import re
from collections import Counter

with open('test.txt') as f:
        text = f.read()

words = re.findall(r'\w+', text)

cap_words = [ word.upper() for word in words ]

words_counts = Counter(cap_words)
print(words_counts)
print("\n###########################")
print(words_counts.most_common(1))

print(words_counts.most_common(1)[0][0])
