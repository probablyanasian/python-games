def rps(inny):
    import random
    #Declaring some variables
    x = ""
    #randomizer settings
    rmin = 0
    rmax = 1000
    rat = round(((rmax-(rmin-1))/3)+(rmin-1))
    rbt = round(((rmax-(rmin-1))/3)*2+(rmin-1))
    while True:
    #Failsafe switch reset
        fss = 0
    ##Random integer generator
        mselect = random.randint(rmin,rmax)
        if mselect in range(rmin,rat):
            x = "p" # Paper
        elif mselect in range(rat+1,rbt):
            x = "s" # Scissors
        elif mselect in range(rbt+1,rmax):
            x = "r" # Rock
    #User selects rock
        if inny in ("rock", "r"):
            if x == "s":
                return "win"
            elif x == "p":
                return "loss"
            elif x == "r":
                return "tie"
    #User selects paper               
        elif inny in ("paper", "p"):
            if x == "r":
                return "win"    
            elif x == "s":
                return "loss"                
            elif x == "p":
                return "tie"
    #User selects scissors
        elif inny in ("scissors", "s", "scissor"):
            if x == "p":
                return "win"    
            elif x == "r":
                return "loss"
            elif x == "s":
                return "tie"
    #Failsafe
        if fss == 0:
            return "failedinput"
