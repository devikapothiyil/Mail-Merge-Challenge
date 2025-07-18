PLACEHOLDER="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contents=letter.read()
    for name in names:
        stripped_name= name.strip()
        new_letter=letter_contents.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)
