browser = Region(967,9,245,105)
reg = Region(1064,175,821,495)

notargetposition = Location(1162, 308)
homepagebtn = "gohomebtn-3.PNG"

def checkcurrentpage():
    if reg.exists("supply-3.PNG", 1):
        currentpage = "homepage"
        
    elif reg.exists("supplypage-2.PNG", 1):
        currentpage = "supplypage"
    elif reg.exists("1463311409151.png", 1):
        currentpage = "farbettlepage"
    else:
        currentpage = "not find"
    return currentpage

def check_outline_state():
    if exists("catattack.PNG",2):
        resetstep = 0
        return resetstep
   
def restart_game():
    if exists("catattack.PNG",2):
        while not reg.exists("gamestart.PNG",2):
            if reg.exists("catattack-1.PNG"):
                browser.wait("1463297354648.png",2)
                browser.click(Pattern("1463297354648.png").targetOffset(59,0))
    
            sleep(5)
        while not reg.exists("supply-4.PNG"):
            reg.click("gamestart.PNG")
            sleep(5)
    else:
        sleep(1)

def check_mission_complete_message():
    hover(notargetposition) 
    if exists("1463317363839.png", 2):
        x = 0
        while x < 5:        
            doubleClick(notargetposition)
            sleep(3)
            x = x + 1            
    else:
        sleep(2)
def gohomepage(): 
    currentpage = checkcurrentpage()
    if currentpage == "homepage":
        sleep(2)
        check_mission_complete_message()        
    elif currentpage == "supplypage" or currentpage == "farbettlepage":
        wait(homepagebtn,3)
        click(homepagebtn)
        sleep(2)
        check_mission_complete_message()        

     
def go_far_battle_page():
    hover(notargetposition)
    reg.wait("fight-3.PNG",10)

    reg.click("fight-3.PNG")
    reg.wait("farbettlebtn.PNG",10)

    reg.click("farbettlebtn.PNG")

def autosupply(team = 1):       
    reg.click("supply-4.PNG")        
    reg.wait("supplypage-3.PNG",5) 
    if team == 1:
        reg.click("allsupplybtn-2.PNG")
    elif team == 2:
        reg.wait("team2btn.PNG",2)
        reg.click("team2btn.PNG") 
        sleep(1)
        reg.wait("allsupplybtn-2.PNG",2)
        reg.click()        
    elif team == 3:
        reg.wait("team3btn.PNG",2)
        reg.click("team3btn.PNG")         
        reg.wait("allsupplybtn-2.PNG",2)
        reg.click("allsupplybtn-2.PNG")                    
    elif team == 5:       
        reg.wait("allsupplybtn-2.PNG",2)
        reg.click("allsupplybtn-2.PNG")    
        sleep(2)
        reg.wait("team2btn.PNG",2)
        reg.click("team2btn.PNG") 
        sleep(2)
        reg.wait("allsupplybtn-2.PNG",2)
        reg.click("allsupplybtn-2.PNG")    
        sleep(2) 
        reg.wait("team3btn.PNG",2)
        reg.click("team3btn.PNG")    
        sleep(2)
        reg.wait("allsupplybtn-2.PNG",2)
        reg.click("allsupplybtn-2.PNG")    
    sleep(2)
    reg.click("gohomebtn-3.PNG")
    sleep(2)
    hover(notargetposition)

def checkmissionstate(target): 
    if target == 2:
        reg.wait("farbettlemession2-1.PNG",3)
        reg.click("farbettlemession2-1.PNG")
        sleep(1)
    elif target == 3:     
        reg.wait("farbettlemession5.PNG",3)
        reg.click("farbettlemession5.PNG")
        sleep(1)
    if reg.exists("farbattlestopbtn.PNG",2):
        missionstate = "active"
    elif reg.exists("farbettlecheckbtn.PNG",2):
        missionstate = "stop"  
    return missionstate

def start_mission(team):
    
    if team == 2:
        reg.wait("farbettlemession2-1.PNG",3)
        reg.click("farbettlemession2-1.PNG")
    elif team == 3:     
        reg.wait("farbettlemession5.PNG",3)
        reg.click("farbettlemession5.PNG")
    reg.wait("farbettlecheckbtn.PNG",3)
    reg.click("farbettlecheckbtn.PNG")
    reg.wait("farbettlestartbtn.PNG",3)
    reg.click("farbettlestartbtn.PNG")



step = 1
while (step <= 5):
    if step == 0:
        restart_game()
        step = 1
    elif step == 1:    
        gohomepage()
        step = 2
        if exists("catattack.PNG",3):
            step = 0
            continue
                
    elif step == 2:
        go_far_battle_page()
        if exists("catattack.PNG",3):
            step = 0
            continue
        team_mission_state = checkmissionstate(3)
        if team_mission_state == "stop":
            gohomepage()
            if exists("catattack.PNG",3):
                step = 0
                continue
            autosupply(2)
            go_far_battle_page()
            if exists("catattack.PNG",3):
                step = 0
                continue            
            sleep(2)
            start_mission(3)
            if exists("catattack.PNG",3):
                step = 0
                continue            
            sleep(3)
            gohomepage()
            if exists("catattack.PNG",3):
                step = 0
                continue            
            sleep(120)
            step = 1
        else:
            sleep(3)
            gohomepage()
            if exists("catattack.PNG",3):
                step = 0
                continue
            sleep(120)
            step = 1