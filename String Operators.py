# string concatenation

first_name = "Emmanuel"
last_name = "Okoh"

# full name = first + last name

print(first_name + " " + last_name)

# string repetition

word = "Hello "
# repeat 3 times
repeat_count = 3

repeated_word = word * repeat_count

print(repeated_word)

# string comparison or relational operators (==, !=, >, <, >=, <=)

fruit1 = "apple"
fruit2 = "banana"

print(fruit1 == fruit2) #false
print(fruit1 != fruit2) #true
print(fruit1 > fruit2) #false because unicode value of a is less than v. here 97<98 so it is false
print(fruit1 < fruit2) #true
print(fruit1 >= fruit2) #false
print(fruit1 <= fruit2) #true

# unicode value of a is 97, b is 98, c is 99...
# unicode value of A is 65, B is 66, c is 67...


# string membership operators (in, not in)

sentence = "The quick brown fox jumps over the lazy dog"

print("quick" in sentence) #true
print("slow" in sentence) #false
print("Quick" in sentence) #false because q != Q because they have different unicode values


# string slicing or indexing

text = "Hello, world"

# extract the word hello from the string text

extracted_string = text[0:5]

# 0 - H
# 1 - E
# 2 - L
# 3 - L
# 4 - O
# 5 - ,

print(extracted_string)
