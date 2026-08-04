import streamlit as st
import sys


st.set_page_config(
    page_title="Climate Disaster AI Assistant",
    page_icon="🌍",
    layout="wide"
)


# ================= UI DESIGN =================

st.markdown("""
<style>

.stApp {

background: linear-gradient(
135deg,
#e0f7ff,
#caf0f8,
#ade8f4
);

}


/* Main Hero */

.hero {

background:white;

padding:35px;

border-radius:25px;

text-align:center;

box-shadow:0px 8px 25px rgba(0,0,0,0.12);

}


.hero h1 {

color:#0077b6;

font-size:45px;

}


.hero p {

color:#023e8a;

font-size:20px;

}



/* Disaster Cards */


.card {

background:white;

padding:25px;

border-radius:20px;

text-align:center;

height:150px;

box-shadow:0px 5px 20px rgba(0,0,0,0.12);

}


.card h2 {

font-size:35px;

}


.card h3 {

color:#0077b6;

}



</style>
""", unsafe_allow_html=True)



# ================= HEADER =================


st.markdown(
"""
<div class="hero">

<h1>
🌍 Climate & Disaster Awareness Assistant 🌊
</h1>

<p>
AI Powered Disaster Safety Information System
</p>

<p>
🌧 Flood | 🌊 Tsunami | 🌀 Cyclone | ☀️ Drought | 🌱 Climate Change
</p>

</div>

<br>

""",
unsafe_allow_html=True
)



# ================= CARDS =================


col1,col2,col3,col4 = st.columns(4)


with col1:

    st.markdown(
    """
    <div class="card">

    <h2>🌧️</h2>

    <h3>Flood</h3>

    Safety Guidelines

    </div>
    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
    <div class="card">

    <h2>🌊</h2>

    <h3>Tsunami</h3>

    Emergency Actions

    </div>
    """,
    unsafe_allow_html=True
    )


with col3:

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


with col4:

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



# ================= AGENTS =================


sys.path.append("agents")


from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer



# ================= CHAT MEMORY =================


if "messages" not in st.session_state:

    st.session_state.messages = []



# Show previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])



# ================= CHAT BAR =================


question = st.chat_input(
"💬 Ask about flood, tsunami, cyclone or climate change..."
)



if question:


    # User message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )


    with st.chat_message("user"):

        st.write(question)



    # AI message


    with st.chat_message("assistant"):


        with st.spinner("🤖 AI is searching..."):


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