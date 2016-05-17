browser = Region(967,9,245,105)
reg = Region(1064,175,821,495)
cat_attack_appear_area = Region(1222,458,207,187)
start_btn_area = Region(1502,529,372,124)
far_battle_detail_area = Region(1637,471,239,183)
mission_complete_message_area = Region(1510,182,367,89)


notargetposition = Location(1162, 308)
homepagebtn = "gohomebtn-4.PNG"
game_start_btn = Location(1672, 582)

def check_outline():
    if cat_attack_appear_area.exists("catattack-6.PNG",1):
        raise NameError

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
    game_start_btn = Location(1672, 582) 
    while not reg.exists("supply-9.PNG",2):
        while not start_btn_area.exists("gamestart-3.PNG", 5):
            browser.wait("1463297354648-1.png",2)
            browser.click(Pattern("1463297354648-1.png").targetOffset(59,0))
            sleep(10)
        click(game_start_btn)
        reg.exists("supply-10.PNG",15)

def check_mission_complete_message():
    hover(notargetposition) 
    if mission_complete_message_area.exists("1463317363839.png", 2):
        x = 0
        while x < 5:        
            x = x + 1  
            doubleClick(notargetposition)
            sleep(3)
            check_outline()
    else:
        sleep(2)
def gohomepage(): 
    currentpage = checkcurrentpage()
    if currentpage == "homepage":
        sleep(2)
        check_mission_complete_message()        
    elif currentpage == "supplypage" or currentpage == "farbettlepage":
        reg.wait(homepagebtn,3)
        reg.click(homepagebtn)
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
        reg.click(Pattern("allsupplybtn-3.PNG").targetOffset(60,-1))
        sleep(2)
        reg.click("allsupplybtn-3.PNG")
    elif team == 3:
        reg.click(Pattern("allsupplybtn-3.PNG").targetOffset(88,0))
        sleep(2)        
        reg.click("allsupplybtn-3.PNG")
    elif team == 5:       
        reg.click("allsupplybtn-3.PNG")    
        sleep(2)
        reg.click(Pattern("allsupplybtn-3.PNG").targetOffset(60,-1))
        sleep(2)
        reg.click("allsupplybtn-3.PNG")
        sleep(2) 
        reg.click(Pattern("allsupplybtn-3.PNG").targetOffset(88,0))
        sleep(2)        
        reg.click("allsupplybtn-3.PNG")  
    sleep(2)
    reg.click(homepagebtn)
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
    if far_battle_detail_area.exists("farbattlestopbtn-1.PNG",2):
        missionstate = "active"
    elif far_battle_detail_area.exists("farbettlecheckbtn-1.PNG",2):
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
    far_battle_detail_area.wait("farbettlecheckbtn-1.PNG",3)
    sleep(1) 
    far_battle_detail_area.click("farbettlecheckbtn-1.PNG")
    sleep(1)
    if team == 3:
        reg.wait("far_battle_team_btn_3.PNG",3)
        sleep(1)
        reg.click("far_battle_team_btn_3.PNG")             
    far_battle_detail_area.wait("farbettlestartbtn-1.PNG",3)
    sleep(1)
    far_battle_detail_area.click("farbettlestartbtn-1.PNG")
    sleep(1)

def auto_far_battle():
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
auto_far_battle()