# Example file for Programming Foundations: Algorithms by Joe Marini
# use a set to count unique items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a set to perform a filter
dataset = set()

# TODO: loop over each item and add to the set
for i in items:
  dataset.add(i)
print(dataset)

# TODO: Count the unique letters in a sentence
datalist = []
sentence = "The quick brown fox jumps over the lazy dog."
for i in sentence:
  if i != " ":
    datalist.append(i)

sentence_no_space = ''.join(sentence.split(' '))
print(datalist)
print(len(datalist))
print(sentence_no_space)
print(len(sentence_no_space))