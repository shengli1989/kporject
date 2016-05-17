browser = Region(967,9,245,105)
reg = Region(1080,181,798,478)
cat_attack_appear_area = Region(1222,458,207,187)
notargetposition = Location(1179, 322)
nextspotbtnposition = Location(1372,425)
retreatbtnposition = Location(1586,428)
horzontalbtnposition = Location(1725,524)


def check_outline():
    if cat_attack_appear_area.exists("catattack.PNG",1):
        raise NameError

def restart_game():
    while not reg.exists("gamestart-1.PNG", 5):
        browser.wait("1463297354648.png",2)
        browser.click(Pattern("1463297354648.png").targetOffset(59,0))
        sleep(10)
    while not reg.exists("supply-5.PNG", 3):
        reg.click(game_start_btn)
        sleep(5)

def autosupply():
    reg.wait("supply-3.PNG",10)
    reg.click("supply-3.PNG")
    reg.wait("supplypage-2.PNG",5)
    reg.click("allsupplybtn-2.PNG")
    sleep(1)
    reg.click("gohomebtn-3.PNG")
    sleep(1)
    hover(notargetposition)

def startmap1_5():
    try:
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
    except:
        pass



def edit_formation(formation = "vertical"):
    hover(notargetposition)
    if formation == "vertical":
        pass
    elif formation == "horzontal":
        while not reg.exists("horzontalteam-6.PNG"):
            sleep(2)
            click(Button.LEFT)
            check_outline()
        sleep(2)
        reg.click("horzontalteam-6.PNG")
    else:
        pass


def attack_spot(last_spot = False):
    hover(notargetposition)
    if not last_spot:
        while not reg.exists("nextspotbtn.PNG"):
            if reg.exists("getoutspot.PNG"):
                sleep(2)
                reg.click("getoutspot.PNG")
            sleep(2)
            click(Button.LEFT)
            check_outline()
        sleep(2)
        reg.click("nextspotbtn.PNG")
    else:
        while not reg.exists("1462985138674-1.png"):
            if reg.exists("getoutspot.PNG"):
                sleep(2)
                reg.click("getoutspot.PNG")
            sleep(2)
            click(Button.LEFT)
            check_outline()
        sleep(2)
        reg.click("1462985138674-1.png")


def automap1_5_3():
    autosupply()
    sleep(2)
    startmap1_5()
    sleep(5)

    # 攻擊點 A
    edit_formation("horzontal")
    sleep(2)
    attack_spot()
    sleep(2)

    # 攻擊點 B
    edit_formation("horzontal")
    sleep(2)
    attack_spot()
    sleep(2)

    # 攻擊點 C or D
    edit_formation("horzontal")
    sleep(2)
    attack_spot(True)

def automap1_5_1():
    autosupply()
    sleep(2)
    startmap1_5()
    sleep(5)

    # 攻擊點 A
    edit_formation("horzontal")
    sleep(2)
    attack_spot(True)
    sleep(2)

attack_count = 0
while attack_count < 5 :    
    try:
        automap1_5_1()
        attack_count = attack_count + 1
    except:
        restart_game()