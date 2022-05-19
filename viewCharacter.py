import creatCharacter as create
import myUserinterface as interface

def ViewAllCharacters():
    #need to loop through every character in characters and print relevant info
    for i in create.characters:
        interface.PrintCharacter(i)

    interface.Pause()

def ViewCharacterByName():
    print("Please enter the name of a character")
    name = input()
    for i in create.characters: 
        if (name.capitalize == i.name.capitalize):
            interface.PrintCharacter(i)
        else: 
            interface.NotFound()
        interface.Pause()