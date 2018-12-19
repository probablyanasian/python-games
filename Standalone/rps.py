#For the non-tech people:
#Click "run" at the top of the page, then type in the console "help", self explanatory from there on.

import random
#Declaring some variables
x = ""
hs = 0
ms = 0
#ETGEN
tuno = 1
tdos = 2
tquatro = 4
etgen = 0 
#randomizer settings
rmin = 1
rmax = 450
rat = round(((rmax-(rmin-1))/3)+(rmin-1))
rbt = round(((rmax-(rmin-1))/3)*2+(rmin-1))
#check
#print(rbt)
mname = "Robo"
#testing vars
et = 0
ehw = 0
ehl = 0
hcr = 0
hcp = 0
hcs = 0
#Info, defining it makes it slightly smaller
def info():
    print("Recoded/Created by ProbablyanAsian out of boredom")
    print("Also made with input from people I know for variable names and default mname variable.")
info()
#Formatting
print("~"*25)
print("")
print("Type help for help")
while True:
    #Get user input
    inny = str.strip(str.lower(input("Choice:")))
    #reset temp vars
    tuno = 1
    tdos = 2
    tquatro = 4
#Entropy Gen
    if etgen < 10:
        etgen = etgen + 1
    if etgen == random.randint(1,12) or etgen == 10:
        tuno = 2
        tdos = 4
        tquatro = 8
    if random.randint(1,100) == random.randint(1,25):
        tuno = 4
        tdos = 8
        tquatro = 16
    else:
        tuno = 1
        tdos = 2
        tquatro = 4
        pass
    print("")
    #print(inny)
#Failsafe switch reset
    fss = 0
##Random Int gen
    iKON = random.randint(rmin,rmax)
    if iKON in range(rmin,rat):
        x = "p" ## Paper
    elif iKON in range(rat+1,rbt):
        x = "s" ## Scissors
    elif iKON in range(rbt+1,rmax):
        x = "r" ## Rock
    #Testing vars/Cheat remove "#" below to see what Randomizer will choose.
    #print(x)
    """
    print(rat,rbt)
    print(iKON)
    print(et, ehw, ehl)
    """
#User select rock
    if inny in ("rock", "r"):
        hcr = hcr + 1
        if rat < (rbt-tquatro):
          rat = rat + tdos
        if rbt < (rmax-tuno):
          rbt = rbt + tuno
        else:
            pass
        fss = 1
        if x in ("s"):
            ehw = ehw + 1
            print("You win!")
            hs = hs+1
            print("Try again?")
        elif x in ("p"):
            ehl = ehl+1
            print("You lost, try again?")
            ms = ms+1
        elif x in ("r"):
            et = et+1
            print("Tie, try again?")
#User select paper               
    elif inny in ("paper", "p"):
        hcp = hcp + 1
        if rat > rmin:
          rat = rat - tuno
        if rbt < (rmax-tuno):
          rbt = rbt + tuno
        else:
            pass
        fss = 1
        if x in ("r"):
            ehw = ehw + 1
            print("You win!")
            hs = hs+1
            print("Try again?")
        elif x in ("s"):
            ehl = ehl+1
            print("You lost, try again?")
            ms = ms+1
        elif x in ("p"):
            et = et+1
            print("Tie, try again?")
#User select scissors
    elif inny in ("scissors", "s", "scissor"):
        hcs = hcs + 1
        if rbt > (rat+tquatro):
            rbt = rbt-tdos
        if rat < (rbt - tquatro):
            rat = rat-tuno
        else:
            pass
        fss = 1
        if x in ("p"):
            ehw = ehw + 1
            print("You win!")
            hs = hs+1
            print("Try again?")
        elif x in ("r"):
            ehl = ehl+1
            print("You lost, try again?")
            ms = ms+1
        elif x in ("s"):
            et = et+1
            print("Tie, try again?")
#Quit
    if inny in ("quit", "q", "exit"):
        break
    else:
        pass
#Reset
    if inny in ("reset", "rst"):
        hs = 0
        ms = 0
        fss = 1
        print("Resetted")
        #Formatting
        print("")
        print("")
        continue
    else:
        pass
#Help
    if inny in ("help", "h"):
        print("'HtP' for How to Play")
        print("'Shortcuts' for Commands")
        print("'Info' for information")
        fss = 1
        continue
#Shortcuts
    if inny in ("shortcuts", "scs", "cmds", "commands"):
        #Formatting
        print("~"*25)
        print("Information: info")
        print("Help: h")
        print("Shortcut: scs")
        print("Commands: cmds")
        print("Reset Points: 'rst' or 'reset'")
        print("How to Play: htp")
        print("Quit: 'q' or 'exit'")
        print("Rock: r")
        print("Paper: p")
        print("Scissors: s")
        print("Rename Bot: 'rename', 'mname', or 'rname'")
        fss = 1
        continue
#How to Play
    if inny in ("How to play", "htp"):
        #Formatting
        print("~"*25)
        print("You choose either: Rock, Paper, or Scissors.")
        print("%s also chooses one of the three." % (mname))
        print("Rock beats Scissors, Paper beats Rock, and Scissors beats Paper")
        print("Pointage is automatically tracked")
        print("Reset points using 'reset'")
        print("View commands using 'cmds'")
        fss = 1
        continue
#MName customization
    if inny in ("rename", "mname", "rname"):
        namer = str.lower(input("New name:"))
        mname = ("%s" % (namer))
        fss = 1
        continue
    if inny in ("info", "information"):
        print("`~"*18)
        info()
        print("`~"*18)
        continue
#Failsafe
    if fss == 0:
        print("Type something in properly")
        continue
    #More Formatting
    print("")
    print("~"*25)
    lmao = abs(hs-ms) #Pt difference
    if ms>hs:
        who = ("%s is" % (mname))
    elif hs>ms:
        who = "You are"
    if lmao > 1:
        plur = "s"
    else:
        plur = ""
    if ms > 1:
        plurms = "s"
    else:
        plurms = ""
    if hs > 1:
        plurhs = "s"
    else:
        plurhs = ""
    print("Score: %s: %d pt%s   You: %d pt%s" % (mname, ms, plurms, hs, plurhs))
    if ms > hs or hs > ms:
        print("%s leading by %d point%s" % (who, lmao, plur))
        #Even more Formatting
        print("~"*25)
    else:
        print("No one is leading, Tie")
        #Yeah, formatting
        print("~"*25)
        pass
print("")
print("Times played: Rock: %d Paper: %d Scissors: %d" % (hcr, hcp, hcs))
print("Send above data to https://goo.gl/s7unZv \n")
print("Thanks for trying it out")
print("~ProbablyanAsian")
