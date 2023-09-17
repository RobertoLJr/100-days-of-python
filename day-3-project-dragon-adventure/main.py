print('''

                 )       \   /      (
                /|\\      )\_/(     /|\\
*              / | \\    (/\\|/\\)   / | \\             *
|`.___________/__|__o____\\`|'/___o__|__\\__________.'|
|                  '^`    \\|/   '^`                 |
|                          V                        |
|                                                   |
|                                                   |
| ._______________________________________________. |
|'      l    /\ /     \\\            \\ /\\   l       `|
*       l  /   V       ))            V   \\ l        *
        l/            //                  \\I
                      V

''')
print("Welcome to the Sword Coast.")
print("Your mission is to find and slay the dragon.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
dir_choice = input(
    "You're a swordsman at a crossword, escorting a convoy. The path to the right seems a bit off. "
    "Where do you want to go? Type \"left\" or \"right\".\n").lower()

if dir_choice == "left":
    goblins_choice = input(
        "Goblins ambush the convoy, though they are disorganized and in few numbers. What do you do? Type \"fight\" "
        "or \"run\".\n").lower()

    if goblins_choice == "fight":
        dragon_choice = input(
            "A wild green dragon appears. She attacks you with a poison breath. What do you do? Type \"roll\" to "
            "avoid the poisonous gas or \"advance\" to go through the attack against the beast.\n").lower()
        if dragon_choice == "roll":
            attack_choice = input(
                "You outmaneuver the attack. Push forward with a technique. Type \"head\", \"tail\" or \"heart\" to "
                "pick your target.\n").lower()

            if attack_choice == "heart":
                print("You slay the dragon in awesome fashion. The convoy is saved. You Win!")
            elif attack_choice == "head":
                print("The dragon is faster and gores you with her treacherous horns. Game Over.")
            else:
                print("The dragon is faster and hits you violently with her tail. Game Over.")
        else:
            print("You inhale poisonous gas from the smoke and your journey ends. Game Over.")
    else:
        print("You run with your life, but the goblins slay everyone and rob the cargo. Game Over.")
else:
    print("The Redbrand bandits ambushes you and the convoy. You are outmatched. Game Over.")
