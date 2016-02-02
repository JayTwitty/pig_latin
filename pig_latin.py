



original_word = "Jamario"
first_letter = original_word[0]
end_of_word = original_word[1:]

vowels = ("a","e","i","o","u","A","E","I","O","U")

if first_letter in vowels:
    print(end_of_word + "Say")
else:
    print(end_of_word + first_letter + "ay")

###

sentence = input("What is the sentence you want to translate to pig latin? ")
sentence = sentence.split()
print(sentence)

results = []

for word in sentence:
    if word[0] in vowels:
        results.append(word [1:] + "say")
    else:
        results.append(word [1:] + word[0] + "ay")

print(' '.join(results))


