import inflect

p = inflect.engine()
NUM = 1000
sum = 0
for num in range(1, NUM + 1):
    word = p.number_to_words(num)
    word = word.replace(" ", "")
    word = word.replace("-", "")
    sum += len(word)

print(sum)


