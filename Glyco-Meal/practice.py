import streamlit as st
import anthropic

api_key = st.secrets["anthropic_api_key"]

def Response(api_key, Fasting_level, Pre_meal_level, Post_meal_level,dietary_prefrences):
    client = anthropic.Anthropic(api_key=api_key)

    prompt = (f"Fasting Sugar Level : {Fasting_level}",
              f"Pre Meal Sugar Level : {Pre_meal_level}",
              f"Post Meal Sugar Level : {Post_meal_level}",
              f"Dietary Prefrences : {dietary_prefrences}",
              "Give me a proper food plan so that I can be healthy.")

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=600,
        system = """ You are World Class Nutritionist, You are trained to give a proper and healthy diet plan according to all th given inputs:

                    1) Firstly tell the user warmly not to take tension and dont be sad as it is a curable diasease.
                    2) Anlyze the inputs carefully as you are dealing with a patient answer according to the inputs very carefully.
                    3) Give according to the prefrences as it has very high impact on the user life.
                    4) Dont give a very difficult plan that it unable to foolow.
                    5) Also give the precautions that should be taken to avoid this disease.
                    6) At last also advice the patient not to be sad and if he will follow the following diet plan this will lead to a healthy and a great life.
                    7) Give a good look to your generated content as you can give proper headings that the reader should read and understand properly.
                    8) Talk like a professional nutritionist but dont use complex terms.
                    9) Give the content below the heading to give a good look.
        """,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{prompt}"
                    }
                ]
            }
        ]
    )
    ans = message.content[0].text
    return ans 


st.title("GlycoMeal - Your Personal Diet Planner")
st.write("-----------------------------------------------------------------------------------------------------------")
st.write("Your personalized diabetes diet guide—input your glucose levels and get tailored meal plans.")
st.write("-----------------------------------------------------------------------------------------------------------")

st.sidebar.image("/diet.jpg", use_column_width=True)
st.sidebar.header("Enter Your Details")
st.markdown("""
        <style>
        body {
            background-color: #f0f4f8;
            color: #333333;
        }
        .stApp {
            background-color: #f0f4f8;
        }
        h1 {
            color: #4CAF50;
        }
        </style>
        """, unsafe_allow_html=True)

fasting_level = st.sidebar.number_input("Fasting Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
pre_meal_level = st.sidebar.number_input("Pre-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
post_meal_level = st.sidebar.number_input("Post-Meal Sugar Levels (mg/dL)", min_value=0, max_value=500, step=1)
dietary_preferences = st.sidebar.text_input("Dietary Preferences (e.g., vegetarian, low-carb)")

def getresponse(api_key, fasting_level, pre_meal_level, post_meal_level, dietary_preferences):
    response = Response(api_key, fasting_level, pre_meal_level, post_meal_level, dietary_preferences)
    return response

if st.sidebar.button("Give Diet Plan"):

    if api_key and fasting_level and pre_meal_level and post_meal_level and dietary_preferences:
        ans = getresponse(api_key, fasting_level, pre_meal_level, post_meal_level, dietary_preferences)
        st.write(ans)

    else:
        st.write("Please first enter the values to get diet plan ..... ")
