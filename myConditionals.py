import creatCharacter as creatCharacter
import viewCharacter as view
import mainProgram as main

def MainMenu(choice): #will handle the first decision made when entering the main menu
    if choice == "1":
        creatCharacter.CreateCharacter()
    elif choice == "2":
        view.ViewCharacterByName()
    elif choice == "3":
        view.ViewAllCharacters()
    elif choice == "4":
        return 4
    elif choice == "5":
        return 5
    elif choice == "6":
        return 6
    else:
        main.isRunning = False



