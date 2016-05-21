import random
browser = Region(967,9,245,105)
reg = Region(1080,181,798,478)
cat_attack_appear_area = Region(1222,458,207,187)
start_btn_area = Region(1502,529,372,124)
mission_complete_message_area = Region(1430,180,445,91)
supply_area = Region(1163,274,270,378)

notargetposition = Location(1179, 322)
nextspotbtnposition = Location(1372,425)
retreatbtnposition = Location(1586,428)
horzontalbtnposition = Location(1725,524)

def click_random_position(area, image, x1, x2, y1, y2):
    area.click(Pattern(image).targetOffset(random.randint(x1,x2),random.randint(y1,y2)))


def check_outline():
    if cat_attack_appear_area.exists("catattack.PNG",1):
        raise NameError

def restart_game():
    while not reg.exists("supply.PNG",2):
        while not start_btn_area.exists("gamestart-3.PNG", 5):
            browser.wait("1463297354648-1.png",2)
            browser.click(Pattern("1463297354648-1.png").targetOffset(59,0))
            sleep(random.randint(10,25))
        click_random_position(reg, "gamestart-3.PNG", -100, 100, -25 ,25)
        reg.exists("supply.PNG",15)
        
def autosupply():
    reg.wait("supply-1.PNG",3)
    click_random_position(reg, "supply-1.PNG", -25, 25, -25 ,25)
    sleep(random.randint(2,4)) 
    reg.wait("supplypage-2.PNG",5)
    click_random_position(supply_area, "allsupplybtn-3.PNG", -8, 8, -8, 8)        
    sleep(random.randint(2,4)) 
    reg.wait("gohomebtn.PNG",3)
    click_random_position(reg, "gohomebtn.PNG", -10, 10, -35 ,35)
    sleep(1)
    hover(Location(random.randint(1634,1725), random.randint(416,496))) 

def startmap1_5():
    try:
        hover(Location(random.randint(1634,1725), random.randint(416,496)))
        reg.wait("fight-4.PNG",10)
        click_random_position(reg, "fight-4.PNG", -50, 50, -40, 40)
        hover(Location(random.randint(1634,1725), random.randint(416,496)))
        sleep(random.randint(2,4)) 
        reg.wait("fight2-3.PNG",5)
        click_random_position(reg, "fight2-3.PNG", -85, 85, -85, 85)
        sleep(random.randint(2,4))
        reg.wait("map1nextbtn-1.PNG",5)
        click_random_position(reg, "map1nextbtn-1.PNG", -50, 50, -50, 50)
        hover(Location(random.randint(1504-30, 1504+30), random.randint(552-30, 552+30)))
        sleep(random.randint(2,4))
        reg.wait("map1-6.PNG",5)
        click_random_position(reg, "map1-6.PNG", -300, 200, -70, 30)
        sleep(random.randint(2,4))
        reg.wait("checkbtn-3.PNG",5)
        click_random_position(reg, "checkbtn-3.PNG", -40, 40, -17, 17)
        hover(Location(random.randint(1684-30,1684+30), random.randint(382-30,382+30)))        
        sleep(random.randint(2,4))
        reg.wait("startfightbtn-3.PNG",5)
        click_random_position(reg, "startfightbtn-3.PNG", -60, 60, -17, 17)
    except:
        pass

def edit_formation(formation = False): 
    formation_click_position_x = random.randint(1139, 1330) 
    formation_click_position_y = random.randint(242, 450)
    hover(Location(formation_click_position_x, formation_click_position_y))
     
    if formation == "vertical":
        pass
    elif formation == "horzontal":       
        while not reg.exists("formation_step.PNG"):
            if reg.exists("compass.PNG"): 
                click(Location(formation_click_position_x + random.randint(-20, 20), formation_click_position_y + random.randint(-20, 20))) 
            sleep(random.randint(2,5))
        click_random_position(reg, "1463762749519.png", -40, 40, 58, 80)
    else:
        pass

def attack_spot(last_spot = False):
    formation_click_position_x = random.randint(1139, 1330) 
    formation_click_position_y = random.randint(242, 450)
    hover(Location(formation_click_position_x, formation_click_position_y))
    if not last_spot:
        while not reg.exists("nextspotbtn.PNG"):
            if reg.exists("getoutspot.PNG"):
                click_random_position(reg, "getoutspot.PNG", -40, 40, -40, 40)
            else:             
                click(Location(formation_click_position_x + random.randint(-20, 20), formation_click_position_y + random.randint(-20, 20)))
                check_outline()
            sleep(random.randint(2,5))        
        click_random_position(reg, "nextspotbtn.PNG", -40, 40, -40, 40)
    else:
        while not reg.exists("1462985138674-1.png"):
            if reg.exists("getoutspot.PNG"):
                click_random_position(reg, "getoutspot.PNG", -40, 40, -40, 40)
            else:             
                click(Location(formation_click_position_x + random.randint(-20, 20), formation_click_position_y + random.randint(-20, 20)))
                check_outline()
            sleep(random.randint(2,5))  
        click_random_position(reg, "1462985138674-1.png", -40, 40, -40, 40)


def automap1_5_3():
    #autosupply()
    #sleep(random.randint(2,5)) 
    startmap1_5()
    sleep(random.randint(2,5)) 

    # 攻擊點 A
    edit_formation("horzontal")
    sleep(random.randint(2,5)) 
    attack_spot()
    sleep(random.randint(2,5)) 

    # 攻擊點 B
    edit_formation("horzontal")
    sleep(random.randint(2,5)) 
    attack_spot()
    sleep(random.randint(2,5)) 

    # 攻擊點 C
    edit_formation("horzontal")
    sleep(random.randint(2,5)) 
    attack_spot(True)
    sleep(random.randint(2,5)) 

def automap1_5_1():
    autosupply()
    sleep(random.randint(2,5)) 
    startmap1_5()
    sleep(random.randint(2,5)) 

    # 攻擊點 A
    edit_formation("horzontal")
    sleep(2)
    attack_spot(True)
    sleep(2)

automap1_5_3()

def loop_auto_attack(attack_count):    
    i = 0
    while i < attack_count :    
        try:
            automap1_5_3()
            i = i + 1
        except:
            restart_game()