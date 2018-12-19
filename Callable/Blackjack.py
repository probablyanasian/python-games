def blackjack(uinput): 
    while True:
        import random
        facecards = ["0", "A", "J", "Q", "K"]
        facevalues = ["10", "11", "10", "10", "10"]
        def randcard():
            return deck.pop(random.randint(0,len(deck)-1))

        def clear():
            global humanhand
            global humanvalue
            global humanhasa
            global machinehand
            global machinevalue
            global machinehasa
            humanhand = []
            humanvalue = 0
            humanhasa = 0
            machinehand = []
            machinevalue = 0
            machinehasa = 0

        def checkfora(hand):
            retval = 0
            for card in hand:
                if card[1] == "A":
                    retval += 1
            return retval

        def calcval(hand, numofa):
            retval = 0
            for card in hand:
                if card[1] not in facecards: retval += int(card[1])
                else: retval += int(facevalues[facecards.index(card[1])])
            while numofa >= 1:
                if retval > 21:
                    numofa -= 1
                    retval -= 10
                else: break
            return retval

        def ending(humanvalue, machinevalue):
            if humanvalue > 21:
                return ("busted", "loss")
            elif machinevalue > 21:
                return ("machine busted", "win")
            elif machinevalue > humanvalue:
                return ("machine won", "loss")
            elif humanvalue > machinevalue:
                return ("human won", "win")
            elif humanvalue == machinevalue:
                return ("tie game", "tie")

        def newdeck():
          suits='CSDH'; vals='A234567890JQK'
          deck=[suits[i//13]+vals[i%13] for i in range(52)]
          random.shuffle(deck)
          return deck
        #initializing things
        clear()
        if uinput == "clear":
            clear()
        if uinput == "deal":
            clear()
            deck = newdeck()*8
            for i in range(2):
                humanhand.append(randcard())
                humanhasa = checkfora(humanhand)
                humanvalue = calcval(humanhand, humanhasa)
            for i in range(2):
                machinehand.append(randcard())
                mahinehasa = checkfora(machinehand)
                machinevalue = calcval(machinehand, machinehasa)
        if uinput == "hit":
            humanhand.append(randcard())
            humanhasa = checkfora(humanhand)
            humanvalue = calcval(humanhand, humanhasa)
        if machinevalue < 17:
            machinehand.append(randcard())
            machinehasa = checkfora(machinehand)
            machinevalue = calcval(machinehand, machinehasa)
        if humanvalue > 21:
            print(ending(humanvalue, machinevalue))
        if uinput == "stand":
            print(ending(humanvalue, machinevalue))

        print(humanhand)
        print(humanvalue)
