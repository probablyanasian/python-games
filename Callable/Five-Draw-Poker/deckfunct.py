import random
def newdeck():
  suits='CSDH'; vals='A1234567890JQK'
  deck=[suits[i//13]+vals[i%13] for i in range(52)]
  random.shuffle(deck)
  return deck

def randcard(deck, num):
    retval = []
    for _ in range(num):
        retval.append(deck.pop(random.randint(0,len(deck)-1)))
    return retval

    
