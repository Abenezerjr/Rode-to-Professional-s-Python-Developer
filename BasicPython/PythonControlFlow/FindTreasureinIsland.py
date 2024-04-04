print("Welcome to Treasure Island Your mission is to fond The treasure")
print("""                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\Island/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
""")
direction = input('you are in the island of the treasure Where to go Left or Right: ').lower()

if direction == 'right':
    print("Fall into a Hole")
    print("-----Game Over--------")
elif direction == 'left':
    print('You face the Ocean')
    ocean = input("do you went to 'Swim' or 'Wait': ").lower()
    if ocean == 'swim':
        print("attack by Shark🦈")
        print('------Game Over-------')
    elif ocean == 'wait':
        print('you wait the ocean open the gate')
        door = input('which door you went to go? Red , Blue or Yellow: ').lower()

        if door == 'yellow':
            print("you found the treasure🪙")
        elif door == 'red':
            print('Burned by fire 🔥')
            print('------Game Over-------')
        elif door == 'blue':
            print("Eaten by beasts")
        else:
            print('------Game Over-------')
    else:
        print('------Game Over-------')
else:
    print('------Game Over-------')
