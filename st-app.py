import streamlit as st
import main
import time

st.markdown("<h1 style='text-align: center; color: black;'>Loawa Filtering Project</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>This is a simple web application that scrapes data from Loawa to filter out top Lost Ark players on the Korean server based on user preferences</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: black;'>To get started, simply select your desired filters, and click the button below!</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: black;'>My apologies if the app is a bit sloppy. This is my first time working with streamlit and the streamlit library!</h5>", unsafe_allow_html=True)
st.markdown("")
#st.image("https://img.lostark.co.kr/armory/5/A2B03724B744254B587B4151B6D77F7C5497A9786E0EFC0E5FA670FAD68FB961.png?v=20230109051400", width=500)
st.markdown("<p style='text-align: center;'><img src='https://img.lostark.co.kr/armory/5/A2B03724B744254B587B4151B6D77F7C5497A9786E0EFC0E5FA670FAD68FB961.png?v=20230109051400' width='450' height='525'></p>", unsafe_allow_html=True)

#Function that goes through the whole filtering process
#Currently very hard to break this up into multiple functions, as each function pulled from main relies on the driver argument
#Will look into a way to maybe break this function down into smaller and more digestable functions
def class_filtering():
    class_selection = st.selectbox(label="Which class would you like to filter?", options=(main.list_of_classes))
    st.write('You selected:', class_selection)
    engraving_selection = st.selectbox(label="Which class engraving would you like to filter?", options=(main.class_engraving_dict[class_selection]))
    st.write('You selected:', engraving_selection)
    top_player_number = st.selectbox(label="For "+class_selection+", how many of the top KR players would you like to filter from?", options=(20, 40, 60, 80, 100, 120, 140, 160, 180, 200))
    st.write('You will filter from the top '+str(top_player_number)+' players')
    meta_engraving = st.multiselect(label="Which meta engraving are you looking for?", options=("Awakening", "Master Brawler", "Drops of Ether", "Vital Point Hit", "Ambush Master", "Master's Tenacity"
                       , "Raid Captain", "Barricade", "Super Charge", "Stabilized Status", "Ether Predator", "Keen Blunt Weapon", "Grudge"
                       , "Cursed Doll", "Spirit Absorption", "Heavy Armor", "Mass Increase", "Hit Master"
                       , "Adrenaline", "All-Out-Attack", "Expert"))
    #meta_engraving = st.selectbox(label="Which meta engraving are you looking for?", options=("Awakening", "Master Brawler", "Drops of Ether", "Vital Point Hit", "Ambush Master", "Master's Tenacity"
                       #, "Raid Captain", "Barricade", "Super Charge", "Stabilized Status", "Ether Predator", "Keen Blunt Weapon", "Grudge", "Cursed Doll", "Spirit Absorption", "Heavy Armor", "Mass Increase", "Hit Master"
                       #, "Adrenaline", "All-Out-Attack", "Expert"))
    st.write('You selected:', meta_engraving)

    filter_press = st.button(label="When you're ready, click here to filter!")
    if filter_press == True:
        st.write("Sit tight, this process will take some time!")
        driver = main.open_browser()
        main.class_selection(class_selection, main.translated_engravings[engraving_selection], driver)
        main.click_more(int((top_player_number - 20) / 20), driver)
        time.sleep(6)
        profiles = main.collect_profiles(driver)
        selection_dict = main.collect_character_info(profiles, meta_engraving, driver, "filter")
        dict1 = selection_dict[0]
        dict2 = selection_dict[1]
        st.write("For " + class_selection + ", out of the top " + str(top_player_number) + " players in KR, " + str(len(selection_dict[0])) + " use your selected engraving:")
        for i in dict1:
            st.write(f"""
            Name: [{dict2[i]}]({(i)})
            """)
            st.write(dict1[i])
        driver.quit()

def class_snapshot():
    class_selection = st.selectbox(label="Which class would you like to snapshot?", options=(main.list_of_classes))
    engraving_selection = st.selectbox(label="Which class engraving would you like to see?", options=(main.snapshot_engraving_dict[class_selection]))

    snapshot_button = st.button(label="When you're ready, click here to see a "+class_selection+" snapshot!")
    if snapshot_button == True:
        st.write("Sit tight, this process will take some time!")
        driver = main.open_browser()
        main.class_selection(class_selection, None, driver)
        main.click_more(4, driver)
        time.sleep(6)
        profiles = main.collect_profiles(driver)
        if main.translated_engravings[engraving_selection] in main.class_engraving_dict2:
            selection_dict = main.collect_character_info(profiles, main.translated_engravings[engraving_selection], driver, "snapshot")
        else:
            selection_dict = main.collect_character_info(profiles, engraving_selection, driver, "snapshot")
        #Maybe put the image of the class engraving here? Requires another dictionary in the main function
        st.write("For " + class_selection + ", out of the top 100 players in KR, " + str(len(selection_dict[0])) + " use " + engraving_selection)
        driver.quit()

#st.write("check out this [link](https://share.streamlit.io/mesmith027/streamlit_webapps/main/MC_pi/streamlit_app.py)")
user_choice = st.selectbox(label="What would you like to do?", options=("Filter Classes", "Get a Snapshot"))
##test_choice = st.multiselect(label='This is a test', options=("Awakening", "Master Brawler", "Drops of Ether", "Vital Point Hit", "Ambush Master", "Master's Tenacity"
                       #, "Raid Captain", "Barricade", "Super Charge", "Stabilized Status", "Ether Predator", "Keen Blunt Weapon", "Grudge", "Cursed Doll", "Spirit Absorption", "Heavy Armor", "Mass Increase", "Hit Master"
                       #, "Adrenaline", "All-Out-Attack", "Expert"), )
if user_choice == "Filter Classes":
    class_filtering()
if user_choice == "Get a Snapshot":
    class_snapshot()

