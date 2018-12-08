import deckfunct
    #Initialization of game, includes values, clearhand, and single use deck.anime music

deckfunct.clear()
deck = deckfunct.newdeck()
while True:
    uinput = str.lower(str.strip(input("DebugInput: ")))
    if uinput == "deal":
        print(deckfunct.randcard(deck))
        
