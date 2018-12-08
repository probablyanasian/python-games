import random
def newdeck():
  suits='CSDH'; vals='A1234567890JQK'
  deck=[suits[i//13]+vals[i%13] for i in range(52)]
  random.shuffle(deck)
  return deck

def randcard(deck):
    return deck.pop(random.randint(0,len(deck)-1))

def clear():
    global humanvalues
    global machinevalues
    global humanhand
    global machinehand
    humanvalues = [0, 0, 0]
    machinevalues = [0, 0, 0]
    humanhand = []
    machinehand = []
