word = input("Enter a word: ").upper()

for letter in word:
    if letter == "A":
        print("A is found")
        break
    else:
        print("A not found")