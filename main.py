import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


#----------Class engraving translations----------
translated_engravings = {"Rage Hammer":"분노의 망치", "Gravity Training":"중력 수련", "Mayhem":"광기", "Berserker's Technique":"광전사의 비기", "Lone Knight":"고독한 기사", "Combat Readiness":"전투 태세", "Judgement":"심판자",
                         "Blessed Aura":"축복의 오라", "Energy Overflow":"세맥타통", "Robust Spirit":"역천지체", "Esoteric Skill Enhancement":"오의 강화", "First Intention":"초심", "Deathblow":"일격필살", "Esoteric Flurry":"오의난무",
                         "Ultimate Skill: Taijutsu":"극의: 체술", "Shock Training":"충격 단련", "Pinnacle":"절정", "Control":"절제", "Time to Hunt":"사냥의 시간", "Peacemaker":"피스메이커", "Enhanced Weapon":"강화 무기", "Pistoleer":"핸드거너",
                         "Barrage Enhancement":"포격 강화", "Firepower Enhancement":"화력 강화", "Arthetinean Technology":"아르데타인의 기술", "Evolutionary Legacy":"진화의 유산", "Loyal Companion":"두 번째 동료", "Death Strike":"죽음의 습격",
                         "Desperate Salvation":"절실한 구원", "True Courage":"진실된 용맹", "Communication Overflow":"넘치는 교감", "Master Summoner":"상급 소환사", "Igniter":"점화", "Reflux":"환류", "Order of the Emperor":"황제의 칙령",
                         "Empress' Grace":"황후의 은총", "Demonic Impulse":"멈출 수 없는 충동", "Perfect Suppression":"완벽한 억제", "Hunger":"갈증", "Lunar Voice":"달의 소리", "Surge":"버스트", "Remaining Energy":"잔재된 기운"}

#----------Dictionary that ties classes to their class specific engravings----------
##-----The "None" option is there if the user wants to see both class engravings, not for if they want to see NO class engravings
###----Very misleading, so I'll need to change that to something else in the future
class_engraving_dict = {'*Destroyer':["Rage Hammer","Gravity Training", None],'Berserker':["Mayhem","Berserker's Technique", None],'Gunlancer':["Lone Knight","Combat Readiness", None],'Paladin':["Judgement","Blessed Aura", None]
                        ,'Soulfist':["Energy Overflow","Robust Spirit", None],'Wardancer':["Esoteric Skill Enhancement","First Intention", None],'Striker':["Deathblow","Esoteric Flurry", None]
                        ,'Scrapper':["Ultimate Skill: Taijutsu","Shock Training",None],'*Glaivier':["Pinnacle","Control",None],'Gunslinger':["Time to Hunt","Peacemaker",None],'Deadeye':["Enhanced Weapon","Pistoleer",None]
                        ,'Artillerist':["Barrage Enhancement","Firepower Enhancement",None],'*Machinist':["Arthetinean Technology","Evolutionary Legacy",None],'Sharpshooter':["Loyal Companion","Death Strike", None]
                        ,'Bard':["Desperate Salvation","True Courage",None],'*Summoner':["Communication Overflow","Master Summoner",None], 'Sorceress':["Igniter","Reflux",None]
                        ,'*Arcanist':["Order of the Emperor","Empress' Grace",None],'Shadowhunter':["Demonic Impulse","Perfect Suppression",None],'*Reaper':["Hunger","Lunar Voice",None],'Deathblade':["Surge","Remaining Energy",None]}

#----------Dictionary for the snapshot function in st-app.py----------
snapshot_engraving_dict = {'*Destroyer':["Rage Hammer","Gravity Training"],'Berserker':["Mayhem","Berserker's Technique"],'Gunlancer':["Lone Knight","Combat Readiness"],'Paladin':["Judgement","Blessed Aura"]
                        ,'Soulfist':["Energy Overflow","Robust Spirit"],'Wardancer':["Esoteric Skill Enhancement","First Intention"],'Striker':["Deathblow","Esoteric Flurry"]
                        ,'Scrapper':["Ultimate Skill: Taijutsu","Shock Training"],'*Glaivier':["Pinnacle","Control"],'Gunslinger':["Time to Hunt","Peacemaker"],'Deadeye':["Enhanced Weapon","Pistoleer"]
                        ,'Artillerist':["Barrage Enhancement","Firepower Enhancement"],'*Machinist':["Arthetinean Technology","Evolutionary Legacy"],'Sharpshooter':["Loyal Companion","Death Strike"]
                        ,'Bard':["Desperate Salvation","True Courage"],'*Summoner':["Communication Overflow","Master Summoner"], 'Sorceress':["Igniter","Reflux"]
                        ,'*Arcanist':["Order of the Emperor","Empress' Grace"],'Shadowhunter':["Demonic Impulse","Perfect Suppression"],'*Reaper':["Hunger","Lunar Voice"],'Deathblade':["Surge","Remaining Energy"]}

#----------Dictionary that is used for searching up engravings with the snapshot functions----------
class_engraving_dict2 = {"분노의 망치":"Rage Hammer", "중력 수련":"Gravity Training", "절정":"Pinnacle", "절제":"Control",  "아르데타인의 기술":"Arthetinean Technology", "진화의 유산":"Evolutionary Legacy", "넘치는 교감":"Communication Overflow",
                         "상급 소환사":"Master Summoner", "황제의 칙령":"Order of the Emperor", "황후의 은총":"Empress' Grace", "갈증":"Hunger", "달의 소리":"Lunar Voice"}

#----------Dictionary is used here since the wording is different for some engravings when directly translated
##-----However, some of the engravings translate properly, making some entries in this dictionary redundant and not needed
###----We'll look into a way to reduce the amount of entries in this dictionary
meta_engraving_dict = {"Awakening":"Awakening", "Master Brawler":"Master Brawler", "Drops of Ether":"Drops of Ether", "Vital Point Hit": "Vital Point Strike", "Ambush Master":"Master of Ambush", "Master's Tenacity":"Champion's Tenacity"
                       , "Raid Captain":"Raid Captain", "Barricade":"Barricade", "Super Charge":"Super Charge", "Stabilized Status":"Stabilized Status", "Ether Predator":"Ether Enhancement", "Keen Blunt Weapon":"Keen Blunt Weapon"
                       , "Grudge":"Grudge", "Cursed Doll":"Cursed Doll", "Spirit Absorption":"Spirit Absorption", "Heavy Armor":"Heavy Armor Equipment", "Mass Increase":"Mass Gain", "Hit Master":"Master of Strikes"
                       , "Adrenaline":"Adrenaline", "All-Out-Attack":"Fast Speed", "Expert":"Specialist"}

"""
Keeping the dictionary below here in case something above breaks
The dictionary works fine, but displays korean to the user. The above dictionaries were made to translate the class engravings to display in english
"""
#class_engraving_dict = {'*Destroyer':["분노의 망치","중력 수련", None],'Berserker':["광기","광전사의 비기", None],'Gunlancer':["고독한 기사","전투 태세", None],'Paladin':["심판자","축복의 오라", None],'Soulfist':["세맥타통","역천지체", None]
                        #,'Wardancer':["오의 강화","초심", None],'Striker':["일격필살","오의난무", None],'Scrapper':["극의: 체술","충격 단련",None],'*Glaivier':["절정","절제",None],'Gunslinger':["사냥의 시간","피스메이커",None]
                        #,'Deadeye':["강화 무기","핸드거너",None],'Artillerist':["포격 강화","화력 강화",None],'*Machinist':["아르데타인의 기술","진화의 유산",None],'Sharpshooter':["두 번째 동료","죽음의 습격", None],'Bard':["절실한 구원","진실된 용맹",None]
                        #,'*Summoner':["넘치는 교감","상급 소환사",None], 'Sorceress':["점화","환류",None], '*Arcanist':["황제의 칙령","황후의 은총",None],'Shadowhunter':["멈출 수 없는 충동","완벽한 억제",None],'*Reaper':["갈증","달의 소리",None]
                        ##,'Deathblade':["버스트","잔재된 기운",None]}

list_of_classes = ['*Destroyer','Berserker','Gunlancer','Paladin','Soulfist','Wardancer','Striker','Scrapper','*Glaivier','Gunslinger','Deadeye','Artillerist','*Machinist','Sharpshooter','Bard','*Summoner',
                   'Sorceress', '*Arcanist','Shadowhunter','*Reaper','Deathblade']

#-----Initial opening of Loawa, as well as translating the page to english-----
def open_browser():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    s = Service(PATH)
    options = uc.ChromeOptions() #used to be "webdriver" instead of "uc"
    #options.add_experimental_option("detach", True)
    driver = uc.Chrome(options=options, service=s) ##used to be "webdriver" instead of "uc"
    driver.get("https://loawa.com/rank")

    lang = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-default.btn-sm.dropdown-toggle")))
    lang.click()

    english = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,"EN")))
    time.sleep(1)
    english.click()
    return driver

#-----Takes the user's selected class and class engraving and selects them on the webpage-----
def class_selection(user_class, engraving, web_browser):
    driver = web_browser
    try:
        Selected_class = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + user_class +"')]")))
        Selected_class.click()
    except:
        driver.quit()

    if engraving != None:
        specific_imprint = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), '" + engraving + "')]")))
        specific_imprint.click()

#-----For loop that scrolls down to the bottom of the page to load more characters. Amount is based on the range-----
def click_more(num_profiles, web_browser):
    driver = web_browser
    for i in range(num_profiles):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        more = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='d-grid']/button[@class='btn btn-default']")))
        more.click()

#-----Function that scrapes the hyperlinks of characters for the user's desired filters-----
# Some lines of code inside are commented out, but still left in for future bug testing
def collect_profiles(web_browser):
    driver = web_browser
    names = driver.find_elements(By.XPATH, "//tbody/tr/td[@class='d-lg-none d-xl-none']/a")
    profile_list=[]

    for name in names:
        profile_list.append(name.get_attribute("href"))

    #-----The process below is a workaround to the issue of our code looping through the first 20 characters twice
    #-----We still have yet to fully solve why that happens, but this solution works for now
    profile_dict = dict.fromkeys(profile_list)
    new_profile_list = list(profile_dict)
    return (new_profile_list)

#-----Function that scrapes the engravings of the characters from the scraped hyperlinks-----
def collect_character_info(profiles, choice_engraving, web_browser, action):
    driver = web_browser
    #This dictionary will have the key as the hyperlink and the value as a list of the equipped engravings
    filtered_classes = {}
    profile_names = {}
    if action == "filter":
        for i in range(len(choice_engraving)):
            choice_engraving[i] = meta_engraving_dict[choice_engraving[i]]

    for character in profiles:
        driver.get(character)
        try:
        # ----------This gets me the basic stats of the profile. Currently not being used----------
            #character_stats = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "qul-box-wrap" )))
        # ----------This gets me the engravings of the profile----------
            engravings = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "row.char-equip-engrave")))
            engravings_string = str(engravings.text)
            engravings_split = engravings_string.split('\n') #Turns the engravings into a list
            character_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "char-title")))
            character_string = str(character_name.text) #We finally got the character name as a string
            starting_num = 0
            if action == "filter":
                for i in choice_engraving:
                    if i in engravings_string:
                        starting_num += 1
                if starting_num == len(choice_engraving):
                    filtered_classes[character] = engravings_split
                    profile_names[character] = character_string

            if action == "snapshot":
                if choice_engraving in engravings_string:
                    filtered_classes[character] = engravings_split
                    profile_names[character] = character_string
        except:
            driver.quit()
    return(filtered_classes, profile_names)