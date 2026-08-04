import streamlit as st
import sys


st.set_page_config(
    page_title="Climate Disaster AI Assistant",
    page_icon="🌍",
    layout="wide"
)


# Modern UI CSS

st.markdown("""
<style>

.stApp {

background: linear-gradient(
    120deg,
    #001f3f,
    #0077b6,
    #90e0ef
);

}


.block-container {

padding-top:2rem;

}


.hero {

background: rgba(255,255,255,0.15);

backdrop-filter: blur(12px);

border-radius:25px;

padding:35px;

text-align:center;

color:white;

box-shadow:0px 8px 30px rgba(0,0,0,0.3);

}


.hero h1 {

font-size:48px;

}



.hero p {

font-size:22px;

}



.card {

background:rgba(255,255,255,0.18);

backdrop-filter:blur(10px);

border-radius:20px;

padding:25px;

text-align:center;

color:white;

height:160px;

box-shadow:
0 8px 20px rgba(0,0,0,0.25);

}


.card h2 {

font-size:35px;

}



.chat-box {

background:white;

border-radius:20px;

padding:20px;

}



</style>

""", unsafe_allow_html=True)



# Hero Section

st.markdown(
"""
<div class="hero">

<h1>🌍 Climate & Disaster AI Assistant 🌊</h1>

<p>
Intelligent Agentic AI System for Climate Awareness
</p>

<p>
🌧 Flood | 🌊 Tsunami | 🌀 Cyclone | ☀️ Drought
</p>

</div>

<br>

""",
unsafe_allow_html=True
)



# Cards

a,b,c,d = st.columns(4)



with a:

    st.markdown(
    """
    <div class="card">

    <h2>🌧</h2>

    <h3>Flood</h3>

    Safety Actions

    </div>
    """,
    unsafe_allow_html=True
    )


with b:

    st.markdown(
    """
    <div class="card">

    <h2>🌊</h2>

    <h3>Tsunami</h3>

    Emergency Guide

    </div>
    """,
    unsafe_allow_html=True
    )


with c:

    st.markdown(
    """
    <div class="card">

    <h2>🌀</h2>

    <h3>Cyclone</h3>

    Preparedness

    </div>
    """,
    unsafe_allow_html=True
    )


with d:

    st.markdown(
    """
    <div class="card">

    <h2>☀️</h2>

    <h3>Drought</h3>

    Awareness

    </div>
    """,
    unsafe_allow_html=True
    )


st.write("")



# Agents

sys.path.append("agents")


from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer



# Chat Memory

if "messages" not in st.session_state:

    st.session_state.messages=[]



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# Chat Input

question = st.chat_input(
    "Ask your disaster related question..."
)



if question:


    st.session_state.messages.append(
        {
        "role":"user",
        "content":question
        }
    )


    with st.chat_message("user"):

        st.write(question)



    with st.chat_message("assistant"):


        with st.spinner("🌍 Searching knowledge base..."):


            category = route_question(question)


            context = retrieve_information(question)


            answer = generate_answer(
                question,
                context
            )


            st.info(
                "Agent Category: " + category
            )


            st.write(answer)



    st.session_state.messages.append(
        {
        "role":"assistant",
        "content":answer
        }
    )