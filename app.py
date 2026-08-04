import streamlit as st
import sys
import base64


# Page Setup
st.set_page_config(
    page_title="Climate Disaster AI Assistant",
    page_icon="🌍",
    layout="wide"
)


# Background Image

def set_background(image_path):

    with open(image_path, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:
            linear-gradient(
            rgba(220,245,255,0.88),
            rgba(220,245,255,0.88)
            ),
            url("data:image/jpg;base64,{encoded}");

            background-size: cover;
            background-position:center;
        }}


        .title {{
            text-align:center;
            color:#004c6d;
            font-size:45px;
            font-weight:bold;
        }}


        .subtitle {{
            text-align:center;
            color:#00334d;
            font-size:20px;
        }}


        .card {{
            background:rgba(255,255,255,0.75);
            padding:20px;
            border-radius:20px;
            text-align:center;
            box-shadow:0px 5px 15px #aaaaaa;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background("images/climate.jpg")



# Header

st.markdown(
"""
<div class="title">
🌍 Climate & Disaster Awareness Assistant 🌊
</div>

<div class="subtitle">
🌧 Flood | 🌊 Tsunami | 🌀 Cyclone | ☀️ Drought | 🌱 Climate Change
</div>

""",
unsafe_allow_html=True
)



# Disaster Cards

c1,c2,c3 = st.columns(3)


with c1:
    st.markdown(
    """
    <div class="card">
    🌧️
    <h3>Flood</h3>
    Emergency safety guidance
    </div>
    """,
    unsafe_allow_html=True
    )


with c2:
    st.markdown(
    """
    <div class="card">
    🌊
    <h3>Tsunami</h3>
    Coastal safety awareness
    </div>
    """,
    unsafe_allow_html=True
    )


with c3:
    st.markdown(
    """
    <div class="card">
    🌀
    <h3>Cyclone</h3>
    Disaster preparedness
    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")


# Agents connection

sys.path.append("agents")

from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer



# Chat Memory

if "messages" not in st.session_state:
    st.session_state.messages = []



# Display old messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# Chat Input Bar

user_question = st.chat_input(
    "Ask about climate change or disasters..."
)



if user_question:


    # User message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )


    with st.chat_message("user"):
        st.write(user_question)



    # AI response

    with st.chat_message("assistant"):


        with st.spinner("🤖 AI is thinking..."):


            category = route_question(user_question)


            context = retrieve_information(
                user_question
            )


            answer = generate_answer(
                user_question,
                context
            )


            st.info(
                f"Agent Category: {category}"
            )


            st.write(answer)



    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )