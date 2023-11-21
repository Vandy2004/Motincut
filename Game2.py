import time

def introduction():
    print("Welcome to the Enchanted Forest Adventure!")
    time.sleep(1)
    print("You find yourself at the edge of a magical forest with towering trees and sparkling fireflies.")
    time.sleep(1)
    print("A mysterious figure, the Guardian of the Forest, appears before you.")
    time.sleep(1)
    return input("The Guardian offers you a choice: 1.'Brave the Dark Woods' or 2.'Follow the Whispering Wind'. What do you choose? 1 or 2 : ")

def brave_dark_woods():
    print("You decide to brave the Dark Woods, where ancient secrets and eerie creatures reside.")
    time.sleep(1)
    print("As you journey deeper, you encounter a mystical creature with riddles.")
    time.sleep(1)
    return input("Do you want to answer its riddles? (yes/no): ").lower()

def follow_whispering_wind():
    print("You choose to follow the Whispering Wind, a gentle breeze that guides you through the forest.")
    time.sleep(1)
    print("The wind leads you to a hidden glade where fairies dance under the moonlight.")
    time.sleep(1)
    return input("The fairies offer you a magical potion. Do you drink it? (yes/no): ").lower()

def dark_woods_encounter():
    riddle_choice = brave_dark_woods()
    if riddle_choice == "yes":
        print("You decide to answer the mystical creature's riddles.")
        time.sleep(1)
        print("The creature is pleased with your answers and grants you a magical amulet.")
        time.sleep(1)
        print("With the amulet, you can now communicate with the ancient spirits of the forest.")
    else:
        print("You choose not to answer the riddles and continue through the Dark Woods.")
        time.sleep(1)
        print("You stumble upon a hidden cave filled with glowing mushrooms.")
        time.sleep(1)
        print("Inside, you find a mysterious artifact that grants you the power of invisibility.")

def whispering_wind_encounter():
    potion_choice = follow_whispering_wind()
    if potion_choice == "yes":
        print("You drink the magical potion offered by the fairies.")
        time.sleep(1)
        print("The potion grants you the ability to understand and communicate with the creatures of the forest.")
        time.sleep(1)
        print("As you explore further, you encounter a wise old owl that shares ancient knowledge with you.")
    else:
        print("You decide not to drink the potion and continue following the Whispering Wind.")
        time.sleep(1)
        print("The wind leads you to a mystical waterfall that reveals a hidden path to the heart of the forest.")

def heart_of_forest():
    print("You arrive at the heart of the enchanted forest, where the magic is most potent.")
    time.sleep(1)
    print("The Guardian of the Forest appears once again, offering you a final choice.")
    time.sleep(1)
    return input("You can either 1.'Embrace the Magic' or 2.'Return to the Human Realm'. What do you choose? 1 or 2 :")

def embrace_the_magic():
    print("You choose to embrace the magic of the enchanted forest.")
    time.sleep(1)
    print("The forest responds to your decision, and you become a guardian of its secrets.")
    time.sleep(1)
    print("You are granted the ability to shape-shift into any creature of the forest at will.")
    time.sleep(1)
    print("Congratulations, you are now a true inhabitant of the enchanted forest!")

def return_to_human_realm():
    print("You decide to return to the human realm, carrying the memories of your magical adventure.")
    time.sleep(1)
    print("As you step out of the forest, time seems to have stood still.")
    time.sleep(1)
    print("You realize that the enchanted forest exists in a realm where time flows differently.")
    time.sleep(1)
    print("You return home with newfound wisdom and tales of your enchanting journey.")

# Main game flow
initial_choice = introduction()

if initial_choice == "1":
    dark_woods_encounter()
    final_choice = heart_of_forest()
    if final_choice == "1":
        embrace_the_magic()
    elif final_choice == "2":
        return_to_human_realm()
    else:
        print("Invalid choice. The adventure ends.")
elif initial_choice == "2":
    whispering_wind_encounter()
    final_choice = heart_of_forest()
    if final_choice == "1":
        embrace_the_magic()
    elif final_choice == "2":
        return_to_human_realm()
    else:
        print("Invalid choice. The adventure ends.")
else:
    print("Invalid choice. The adventure ends.")
