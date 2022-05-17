import PythonDnD.creatCharacter as creatCharacter;

def MainMenu(choice): #will handle the first decision made when entering the main menu
    if choice == "1":
        creatCharacter.CreateCharacter()
    elif choice == "2":
        return 2
    elif choice == "3":
        return 3
    elif choice == "4":
        return 4
    elif choice == "5":
        return 5
    elif choice == "6":
        return 6
    else:
        quit()



