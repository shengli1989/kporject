browser = Region(967,9,245,105)
reg = Region(1064,175,821,495)

notargetposition = Location(1162, 308)
homepagebtn = "gohomebtn-4.PNG"
game_start_btn = Location(1672, 582)

def checkcurrentpage():
    if reg.exists("supply-6.PNG", 1):
        currentpage = "homepage"
        
    elif reg.exists("supplypage-4.PNG", 1):
        currentpage = "supplypage"
    elif reg.exists("1463311409151.png", 1):
        currentpage = "farbettlepage"
    else:
        currentpage = "not find"
    return currentpage
   
def restart_game():
    while not reg.exists("gamestart-1.PNG", 5):
        browser.wait("1463297354648.png",2)
        browser.click(Pattern("1463297354648.png").targetOffset(59,0))
        sleep(10)
    while not reg.exists("supply-5.PNG", 3):
        reg.click(game_start_btn)
        sleep(5)

def check_mission_complete_message():
    hover(notargetposition) 
    if exists("1463317363839.png", 2):
        x = 0
        while x < 5:        
            x = x + 1  
            doubleClick(notargetposition)
            sleep(3)           
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
    reg.wait("fight-4.PNG",10)

    reg.click("fight-4.PNG")
    reg.wait("farbettlebtn-1.PNG",10)

    reg.click("farbettlebtn-1.PNG")

def autosupply(team = 1):       
    reg.click("supply-5.PNG")        
    reg.wait("supplypage-5.PNG",5) 
    if team == 1:
        reg.click("allsupplybtn-3.PNG")
    elif team == 2:
        reg.wait("team2btn-1.PNG",2)
        sleep(1)
        reg.click("team2btn-1.PNG") 
        sleep(1)
        reg.wait("allsupplybtn-3.PNG",2)
        sleep(1)
        reg.click()        
    elif team == 3:
        reg.wait("team3btn-1.PNG",2)
        sleep(1)
        reg.click("team3btn-1.PNG")
        sleep(1)
        reg.wait("allsupplybtn-3.PNG",2)
        sleep(1)
        reg.click("allsupplybtn-3.PNG")                    
    elif team == 5:       
        reg.wait("allsupplybtn-3.PNG",2)
        sleep(1)
        reg.click("allsupplybtn-3.PNG")    
        sleep(2)
        reg.wait("team2btn-1.PNG",2)
        sleep(1)
        reg.click("team2btn-1.PNG") 
        sleep(2)
        reg.wait("allsupplybtn-3.PNG",2)
        sleep(1)
        reg.click("allsupplybtn-3.PNG")    
        sleep(2) 
        reg.wait("team3btn-1.PNG",2)
        sleep(1)
        reg.click("team3btn-1.PNG")    
        sleep(2)
        reg.wait("allsupplybtn-3.PNG",2)
        sleep(1)
        reg.click("allsupplybtn-3.PNG")    
    sleep(2)
    reg.click("gohomebtn-4.PNG")
    sleep(2)
    hover(notargetposition)

def checkmissionstate(target): 
    if target == 2:
        reg.wait("farbettlemession5-1.PNG",3)
        sleep(1)
        reg.click("farbettlemession5-1.PNG")
        sleep(1)
    elif target == 3:     
        reg.wait("map3btn.PNG",3)
        sleep(1)
        reg.click("map3btn.PNG")
        reg.wait("mission21.PNG",3)
        sleep(1)
        reg.click("mission21.PNG")   
        sleep(1)
    if reg.exists("farbattlestopbtn-1.PNG",2):
        missionstate = "active"
    elif reg.exists("farbettlecheckbtn-1.PNG",2):
        missionstate = "stop"  
    return missionstate

def start_mission(team):
    
    if team == 2:
        reg.wait("farbettlemession5-1.PNG",3)
        sleep(1)
        reg.click("farbettlemession5-1.PNG")
        sleep(1)
    elif team == 3:     
        reg.wait("map3btn.PNG",3)
        sleep(1)
        reg.click("map3btn.PNG")
        sleep(1)
        reg.wait("mission21.PNG",3)
        sleep(1)
        reg.click("mission21.PNG")
        sleep(1)   
    reg.wait("farbettlecheckbtn-1.PNG",3)
    sleep(1) 
    reg.click("farbettlecheckbtn-1.PNG")
    sleep(1)
    if team == 3:
        reg.wait("far_battle_team_btn_3.PNG",3)
        sleep(1)
        reg.click("far_battle_team_btn_3.PNG")             
    reg.wait("farbettlestartbtn-1.PNG",3)
    sleep(1)
    reg.click("farbettlestartbtn-1.PNG")
    sleep(1)

while True:
    try:
        gohomepage()             
        team_target = 2
        while team_target < 4:        
            go_far_battle_page()
            team_mission_state = checkmissionstate(team_target)
            if team_mission_state == "stop":
                sleep(3)            
                gohomepage()
                autosupply(team_target)
                go_far_battle_page()         
                sleep(2)
                start_mission(team_target)         
                sleep(5)
                gohomepage()               
            else:
                sleep(3)
                gohomepage()
            team_target = team_target + 1
            sleep(5)
        sleep(1200)
    except:
        restart_game()