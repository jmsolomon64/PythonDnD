import myUserinterface as interface
import creatCharacter as create

characters = []

class Character: #class made for the character this is a blue print. Just like classes in c#
    def __init__(self, name, className, lvl, race, stng, dex, cont, intl, wisd, char): #Self refers to the new object made from the class 
        self.name = name
        self.className = className 
        self.lvl = lvl
        self.race = race
        self.stng = stng
        self.dex = dex
        self.cont = cont
        self.intl = intl
        self.wisd = wisd
        self.char = char  

def CLassName():
    classNames = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]

    for i in range(len(classNames)):
        print(classNames[i])
    
    print("or you can make your own by typing a custom answer!")

def RaceOptions():
    raceList = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"]

    for i in range(len(raceList)):
        print(raceList[i])

    print("or you could always make your own custom race by typing something different!")

def CreateCharacter():
    #GOAL
    #store character attributes as strings and makes a for loop to ask for all the attributes
    #create an array to hold all of the answers by appending the user input to the array
    #do some sort of self.name, self.className, self.lvl, etc = userInput (Which would be an array)

    attributes = ["Name", "Class Name", "Level", "Race", "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

    userInput = []

    for i in range(len(attributes)): #for loops iterates through attributes list and sets user strings into userInput array
        print("What is your characters " + attributes[i] + ": ")
        if i == 1: #1 is where class name is on index
            CLassName()
        elif i == 3:
            RaceOptions() # 3 is where race is on index

        attribute = input()

        if (i == 0) or (i == 1) or (i == 3):
            attribute = attribute[0].upper() + attribute[1:].lower()
            
        userInput.append(attribute)

    newCharacter = Character(userInput[0], userInput[1], userInput[2], userInput[3], userInput[4], userInput[5], userInput[6], userInput[7], userInput[8], userInput[9])

    characters.append(newCharacter)

    interface.Pause()



def DeleteCharacter():
    interface.CharacterName()
    name = input()
    for i in create.characters: 
        if (name.capitalize == i.name.capitalize):
            create.Character.remove(i)
        else: 
            interface.NotFound()
        interface.Pause()
    interface.CharacterDeleted()




def SeedData():
    #makes the cats all characters and puts them into an array that is returned, in main program I'll throw this function into a variable to store the list as a useable and changeable version for the user
    print()
