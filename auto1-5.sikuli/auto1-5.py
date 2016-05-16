reg = Region(1080,181,798,478)

notargetposition = Location(1179, 322)
nextspotbtnposition = Location(1372,425)
retreatbtnposition = Location(1586,428)
horzontalbtnposition = Location(1725,524)

def autosupply():    
    reg.wait("supply-3.PNG",10)
    reg.click("supply-3.PNG")
    reg.wait("supplypage-2.PNG",5)
    
    reg.click("allsupplybtn-2.PNG")
    sleep(1)
    reg.click("gohomebtn-3.PNG")
    sleep(1)
    hover(retreatbtnpostion)

def startmap1_5():
    reg.wait("fight-3.PNG",10)

    reg.click("fight-3.PNG")
    reg.wait("fight2-3.PNG",5)
    reg.click("fight2-3.PNG")
    reg.wait("map1nextbtn-1.PNG",5)
    reg.click("map1nextbtn-1.PNG")
    reg.wait("map1-6.PNG",5)
    reg.click("map1-6.PNG")
    reg.wait("checkbtn-3.PNG",5)
    reg.click("checkbtn-3.PNG")
    reg.wait("startfightbtn-3.PNG",5)
    reg.click("startfightbtn-3.PNG")    


def checkandclickhorzontalbtn(): 
    while not reg.exists("horzontalteam-6.PNG"):         
        hover(notargetposition)
        click(Button.LEFT)
        sleep(2)
    reg.wait("horzontalteam-6.PNG",10)
    reg.click("horzontalteam-6.PNG")    

def checkandclicknextspotbtn():    
    while not reg.exists("nextspotbtn.PNG"):
        if reg.exists("getoutspot.PNG"):
            reg.wait("getoutspot.PNG",10)
            reg.click("getoutspot.PNG")
        else:
            hover(notargetposition)
            click(Button.LEFT)
        sleep(2)
    reg.wait("nextspotbtn.PNG",10)
    reg.click("nextspotbtn.PNG")        

def checkandclickretreatbtn():
    while not reg.exists("1462985138674-1.png"):
        if reg.exists("getoutspot.PNG"):
            reg.wait("getoutspot.PNG",10)
            reg.click("getoutspot.PNG")
        else:
            hover(notargetposition)
            click(Button.LEFT)
        sleep(2)
    reg.wait("1462985138674-1.png",10)
    reg.click("1462985138674-1.png")    

def fightspot_next():
    checkandclickhorzontalbtn()
    sleep(2)
    checkandclicknextspotbtn()

def fightspot_last():
    checkandclickhorzontalbtn()
    sleep(2)
    checkandclickretreatbtn()


def automap1_5_3():
    autosupply()   
    sleep(2) 
    startmap1_5()
    sleep(5) 
    fightspot_next()
    sleep(2)
    fightspot_next()
    sleep(2)    
    fightspot_last()

def automap1_5_1():
    autosupply()   
    sleep(2) 
    startmap1_5()
    sleep(5)   
    fightspot_last()

automap1_5_3()