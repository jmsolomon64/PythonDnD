def Welcome(): #Welcome for the 
    print("Welcome to the DnD Character creator")

def MainMenu():
    print("Choose one please: \n" +
    "1. Create a character \n" +
    "2. View a character \n" +
    "3. View all characters \n" +
    "4. Update a character \n" + 
    "5. Delet a character \n" + 
    "6. Leave the app")

def Pause():
    print("Press enter to continue...")
    button = input()

def PrintCharacter(i):
    print(f"Name: {i.name} \n" +
        f"Class: {i.className} \n" +
        f"Level: {i.lvl} \n" +
        f"Race: {i.race} \n" + 
        f"Strength: {i.stng} \n" +
        f"Dexterity: {i.dex} \n" +
        f"Constitution: {i.cont} \n" + 
        f"Intelligence: {i.intl} \n" +
        f"Wisdom: {i.wisd} \n" +
        f"Charisma: {i.char} \n")

def NotFound():
    print("Not found")
