from lingualeo import LinguaLeo

lingLeo = LinguaLeo("dumacukps@gmail.com")
# print(lingLeo.add_word("ass").text)

words = {}
with open("GoldenDict-history.txt") as file_object:
    for line in file_object:
        word = line.strip()
        print("adding word: " + word)
        lingLeo.add_word(word)

print(words)



