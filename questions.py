import streamlit as st
import time
import json

st.set_page_config(page_title="Fun Friend Icebreaker", page_icon="💬")

st.title("💬 Fun Friend Icebreaker — Ultimate Version")
st.write("Fun, interactive & anonymous mode included 😄✨")

# ---- Anonymous Mode ----
st.subheader("🕵️ Anonymous Mode")
anonymous = st.checkbox("Enable Anonymous Mode (hide your name)")

st.markdown("---")

progress = st.progress(0)
completed = 0
total_questions = 20  # update if you add/remove questions

def update_progress():
    global completed
    completed += 1
    progress.progress(int((completed / total_questions) * 100))


# ---- BASIC INFO ----
st.header("✨ Basic Info")

name = st.text_input("What name do you like being called?")
if name:
    update_progress()
    if not anonymous:
        st.write(f"Nice! I’ll call you **{name}** 😎")
    else:
        st.write("Keeping it anonymous... mysterious 😏")

birthday = st.text_input("When is your birthday?")
if birthday:
    update_progress()

sign = st.text_input("What is your star sign?")
if sign:
    update_progress()
    st.write(f"Oooh a **{sign}**… I see your vibe 🌌")


# ---- PREFERENCES ----
st.markdown("---")
st.header("🎨 Likes & Preferences")

color = st.text_input("Favorite color & why?")
if color:
    update_progress()
    st.write(f"**{color}** is actually such a mood 🎨")

music_genre = st.text_input("Favorite music genre?")
if music_genre:
    update_progress()
    st.write(f"Respect. **{music_genre}** listeners are built different 🎧🔥")

fav_song = st.text_input("All-time favorite song?")
if fav_song:
    update_progress()
    st.write(f"Bet you’ve played **{fav_song}** at least 100 times 😂")

movie_genre = st.text_input("Favorite movie genre?")
if movie_genre:
    update_progress()
    st.write(f"Ah yes… **{movie_genre}** fans = elite taste 🎬🔥")

top_movies = st.text_area("Top 3 movies or TV shows?")
if top_movies:
    update_progress()

cuisine = st.text_input("Favorite cuisine (Italian, Chinese, desi, etc.)?")
if cuisine:
    update_progress()
    st.write(f"Food choice: **{cuisine}** = respectable 🍽️🔥")

cooking = st.text_input("Do you cook? Go-to dish?")
if cooking:
    update_progress()
    st.write("Chef mode activated 👩‍🍳🔥")


fruit = st.text_input("Favorite fruit?")
if fruit:
    update_progress()

vegetable = st.text_input("Favorite vegetable?")
if vegetable:
    update_progress()

drink = st.radio("Tea or Coffee?", ["Tea", "Coffee", "Both", "None"])
update_progress()
if drink == "Tea":
    st.write("Tea squad ☕ calm but powerful energy.")
elif drink == "Coffee":
    st.write("Coffee warriors ☕🔥 full send mode.")
elif drink == "Both":
    st.write("Balanced people are dangerous 😆")
else:
    st.write("No caffeine?? Natural energy 😳")


pets = st.text_input("Cats, dogs, or other animals?")
if pets:
    update_progress()
    st.write(f"🧡 A **{pets}** person — cute choice!")

travel = st.text_input("Dream travel destination?")
if travel:
    update_progress()
    st.write(f"✈️ Manifesting **{travel}** for you!")


# ---- LIFESTYLE ----
st.markdown("---")
st.header("🏡 Lifestyle")

location = st.text_input("City person or small-town?")
if location:
    update_progress()

season = st.text_input("Favorite season & why?")
if season:
    update_progress()

routine = st.text_input("Morning person or night owl?")
if routine:
    update_progress()
    if "night" in routine.lower():
        st.write("Night owls 🤝 creativity at 2AM")
    elif "morn" in routine.lower():
        st.write("Morning people = secretly superheroes ☀️")

reading = st.text_input("Do you read? Last book?")
if reading:
    update_progress()

sports = st.text_input("Any sports you follow or play?")
if sports:
    update_progress()

hobby = st.text_input("Favorite hobby or way to relax?")
if hobby:
    update_progress()

superpower = st.text_area("If you could have one superpower, what would it be and why?")
if superpower:
    update_progress()


st.markdown("---")

# ---- SAVE ANSWERS ----
if st.button("💾 Save My Answers"):
    filename = "your_icebreaker_answers.txt"
    answers = {
        "Anonymous Mode": anonymous,
        "Name": name if not anonymous else "Anonymous User",
        "Birthday": birthday,
        "Star Sign": sign,
        "Favorite Color": color,
        "Music Genre": music_genre,
        "Favorite Song": fav_song,
        "Movie Genre": movie_genre,
        "Top Movies/Shows": top_movies,
        "Cuisine": cuisine,
        "Cooking": cooking,
        "Fruit": fruit,
        "Vegetable": vegetable,
        "Drink": drink,
        "Pets": pets,
        "Travel": travel,
        "Location Type": location,
        "Season": season,
        "Routine": routine,
        "Reading": reading,
        "Sports": sports,
        "Hobby": hobby,
        "Superpower": superpower
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(answers, f, indent=4)

    st.download_button(
        label="Download Answers File 📁",
        data=json.dumps(answers, indent=4),
        file_name="answers.txt",
        mime="text/plain"
    )

    st.success("Your answers have been saved! 🎉")


# ---- FINAL BUTTON ----
if st.button("✨ Generate Fun Summary"):
    st.subheader("🎉 Your Fun Personality Summary")

    summary = f"""
    **Name:** {name if not anonymous else 'Anonymous 👀'}  
    **Star Sign:** {sign or 'Unknown energy'}  
    **Fav Color:** {color or '???'}  
    **Music Taste:** {music_genre or 'Undefined'}  
    **Fav Song:** {fav_song or 'No theme song yet'}  
    **Movie Genre:** {movie_genre or 'All types 😆'}  
    **Hobby:** {hobby or 'Chilling 😌'}  
    **Superpower Wish:** {superpower or 'A mysterious superhuman'}  
    """

    st.info(summary)
    st.success("Thanks for playing! This was fun 😄")
