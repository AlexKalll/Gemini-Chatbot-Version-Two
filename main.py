import os 
import streamlit as st

import google.generativeai as genai

# loading the invironment variables
from dotenv import load_dotenv
load_dotenv()

my_api_key = os.getenv("GOOGLE_API_KEY")

# configure the generative ai model with the retrieved api key
genai.configure(api_key = my_api_key)

# define out desired model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history = [])

# define a fuction that gemini will respond through \
def get_gemini_response(question):
    response = chat.send_message(question, stream = True)
    return response

# create the streamlit app
st.set_page_config(page_title = 'Gemini Chatbot', page_icon = '🤖')
st.title('Gemini Chat Application')

# initilize the session state if chat history is empty using st.session_state 
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# create input field for user questions
with st.form(key = "input", clear_on_submit = True):
    user_quest = st.text_input('Enter your question in the space provided below, then click the *send* button.', placeholder = 'Type here...' )
    submit_button = st.form_submit_button('Send')

if submit_button and not user_quest:
    st.info(f'Please enter your question and click the **Send** button below')

if user_quest and submit_button:
    # add user question to the chat_history
    st.session_state.chat_history.append(("You: ", user_quest))

    # let's get the respose 
    response = get_gemini_response(user_quest)
    # display the responses
    st.subheader('Answer:')
    answer = ''
    for chunk in response:
        answer += chunk.text
    
    st.write(answer)

    # add the response to the session state as well
    st.session_state.chat_history.append(('Gemini: ', answer))

# Display the whole chat history in all reruns
if len(st.session_state['chat_history']) > 0:
    st.subheader('Chat History:')
    
    for role, text in st.session_state.chat_history:
        st.markdown(f'<span style = "font-weight: bold; font-size: 1.3em;">{role}</span> {text}', unsafe_allow_html = True) 
else:
    st.markdown('<div style="height: 250px;"></div>', unsafe_allow_html=True) 
    st.info('This bot uses the Google\'s Generative AI model, gemini-1.5-flash, developed by Kaletsidik. The model generates text based on the given input. What makes this project cool is it can track chat history and user friedly. If you need help with a specific issue, feel free to ask.')
    st.markdown('---')
    st.success("Made By Kaletsidik ©2024")