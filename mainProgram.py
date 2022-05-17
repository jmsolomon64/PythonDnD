import imp
import random
import PythonDnD.creatCharacter as creatCharacter
import myUserinterface
import myConditionals
#This file will act in the same way as my Program.cs file would

isRunning= True

myUserinterface.Welcome() #invoking methods from other files that perform certain things very well will keep this code clean (probably)

while isRunning:
    myUserinterface.MainMenu()

    choice = input() #Gaining the users decision, need to have a way to deal with user inputing an invalid option

    myConditionals.MainMenu(choice)
