import random

browser = Region(967,9,245,105)
reg = Region(1064,175,821,495)
cat_attack_appear_area = Region(1222,458,207,187)
start_btn_area = Region(1502,529,372,124)
mission_complete_message_area = Region(1430,180,445,91)
supply_area = Region(1163,274,270,378)

notargetposition = Location(1162, 308)
game_start_btn = Location(1672, 582)

def click_random_position(area, image, x1, x2, y1, y2):
    area.click(Pattern(image).targetOffset(random.randint(x1,x2),random.randint(y1,y2)))

def check_outline():
    if cat_attack_appear_area.exists("catattack.PNG",1):
        raise NameError

def check_current_page():
    if reg.exists("supply.PNG", 1):
        currentpage = "homepage"
    elif reg.exists("check_supply_page.PNG", 1):
        currentpage = "supplypage"
    elif reg.exists("1463311409151.png", 1):
        currentpage = "far_battle_page"
    else:
        currentpage = "not find"
    return currentpage


def restart_game():
    while not reg.exists("supply.PNG",2):
        while not start_btn_area.exists("gamestart-3.PNG", 5):
            browser.wait("1463297354648-1.png",2)
            browser.click(Pattern("1463297354648-1.png").targetOffset(59,0))
            sleep(random.randint(10,25))
        click_random_position(reg, "gamestart-3.PNG", -100, 100, -25 ,25)
        reg.exists("supply.PNG",15)

def go_home_page():
    hover(Location(random.randint(1634,1725), random.randint(416,496))) 
    currentpage = check_current_page()
    if currentpage == "homepage":
        sleep(random.randint(2,4))
    elif currentpage == "supplypage" or currentpage == "far_battle_page":
        reg.wait("gohomebtn.PNG",3)
        click_random_position(reg, "gohomebtn.PNG", -10, 10, -35 ,35)        
        sleep(random.randint(2,5))
        hover(Location(random.randint(1634,1725), random.randint(416,496))) 

def go_supply_page():
    hover(Location(random.randint(1634,1725), random.randint(416,496)))
    currentpage = check_current_page()
    if currentpage == "homepage":
        reg.wait("supply.PNG",3)
        click_random_position(reg, "supply.PNG", -25, 25, -25 ,25)
    elif currentpage == "far_battle_page":
        reg.wait("toolbox_supply_btn.PNG",3)
        click_random_position(reg, "toolbox_supply_btn.PNG", -16, 16, -20 ,20)
    else:
        pass

def go_far_battle_page():
    hover(Location(random.randint(1634,1725), random.randint(416,496)))
    reg.wait("fight-4.PNG",10)
    click_random_position(supply_area, "fight-4.PNG", -50, 50, -40, 40) 
    sleep(random.randint(2,5))
    reg.wait("farbettlebtn-1.PNG",10)   
    click_random_position(reg, "farbettlebtn-1.PNG", -80, 80, -80, 80) 
    
def finish_mission_complete_message():    
    x = 0
    click_position = Location(random.randint(1162,1162+400), random.randint(308,308+200))
    while x < 4:
        x = x + 1
        click(click_position)
        sleep(random.randint(4,7))
        check_outline()

def check_mission_complete_message():
    if mission_complete_message_area.exists("1463317363839.png", 2):
        finish_mission_complete_message()
        sleep(random.randint(2,5))
        if mission_complete_message_area.exists("1463317363839.png", 2):
            finish_mission_complete_message()

    else:
        current_page = check_current_page()
        if current_page == "homepage": 
            go_supply_page()
            sleep(random.randint(2,5))
            go_home_page()
            sleep(random.randint(2,5))
        if mission_complete_message_area.exists("1463317363839.png", 2):
            finish_mission_complete_message()
            sleep(random.randint(2,5))
            if mission_complete_message_area.exists("1463317363839.png", 2):
                finish_mission_complete_message()

def check_mission_state_and_supply(team_num):
    if team_num == 2:        
        click_random_position(supply_area, "edit_page_team2_btn.PNG", -8, 8, -8, 8)
        sleep(random.randint(1,3))
    elif team_num == 3:
        click_random_position(supply_area, "1463680035395.png", -8, 8, -8, 8)
        sleep(random.randint(1,3))
    elif team_num == 4:
        pass
    
    if supply_area.exists("far_battle_ing-1.PNG",2):
        team_state = "active"
    else:
        team_state = "stop"
        click_random_position(supply_area, "allsupplybtn-3.PNG", -8, 8, -8, 8)        
    
    return team_state

def start_mission(mission_id, team_num = 2):
           
    if mission_id == 2:        
        click_random_position(reg, "mission_id_2.PNG", -20, 200, -10, 10) 
    elif mission_id == 3:        
        click_random_position(reg, "mission_id_3.PNG", -20, 200, -10, 10) 
    elif mission_id == 5:               
        click_random_position(reg, "mission_id_5.PNG", -20, 200, -10, 10) 
    elif mission_id == 9:
        click_random_position(reg, "far_battle_btn_map2.PNG", -20, 20, -15, 15)
        sleep(random.randint(2,6))
        click_random_position(reg, "mission_id_5.PNG", -20, 200, -10, 10)
    sleep(random.randint(2,5))
        
    reg.wait("far_battle_check_btn.PNG",3)
    click_random_position(reg, "far_battle_check_btn.PNG", -40, 40, -15, 15)
    hover(Location(random.randint(1656, 1656 + 250), random.randint(241, 241 + 150)))
    sleep(random.randint(2,5))
    
    if team_num == 3:
        click_random_position(reg, "1463680950708.png", -8, 8, -8, 8)
        sleep(random.randint(2,5))
        pass
    elif team_num == 4:
        sleep(random.randint(2,5))
        pass   
    
    reg.wait("far_battle_start_btn.PNG",3)
    click_random_position(reg, "far_battle_start_btn.PNG", -65, 65, -15, 15)
    hover(Location(random.randint(1656, 1656 + 250), random.randint(241, 241 + 150)))
    sleep(random.randint(5,10))

def auto_far_battle(run_turn_min, run_total_count):
    i = 0 
    while i < run_total_count :
        i = i + 1
        try:
            go_home_page()
            check_mission_complete_message()
            go_supply_page()
            team2_state = False
            team3_state = False
            team4_state = False
            team2_state = check_mission_state_and_supply(2)
            team3_state = check_mission_state_and_supply(3)
            #team4_state = check_mission_state_and_supply(4)
            go_home_page()
            
            if team2_state == "stop" or team3_state == "stop" or team4_state == "stop":
                go_far_battle_page()
                if team2_state == "stop":
                    start_mission(5, 2)
                    team2_state = "active"
                if team3_state == "stop":
                    start_mission(2, 3)
                    team3_state = "active"
                if team4_state == "stop":                
                    start_mission(3, 4)
                    team4_state = "active"            
                go_home_page()
            else: 
                pass
            sleep(random.randint(run_turn_min, run_turn_min + 10) * 60 )
                            
        except:
            restart_game()
            
auto_far_battle(30, 6)
