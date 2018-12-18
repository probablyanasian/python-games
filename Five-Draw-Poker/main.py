import deckfunct
#Initialization of game, includes values, clearhand, and single use deck.anime music
def clear():
    global humanvalues
    global machinevalues
    global humanhand
    global machinehand
    global deck
    humanvalues = [0, 0, 0]
    machinevalues = [0, 0, 0]
    humanhand = []
    machinehand = []
    deck = deckfunct.newdeck()
clear()
while True:
    uinput = str.lower(str.strip(input("DebugInput: ")))
    if uinput == "deal":
        humanhand = humanhand + deckfunct.randcard(deck, 5)

    if uinput == "clear":
        clear()

    print(humanhand)

