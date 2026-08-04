import streamlit as st
import sys


st.set_page_config(
    page_title="Climate Disaster AI Assistant",
    page_icon="🌍",
    layout="wide"
)


# ================= CSS DESIGN =================

st.markdown("""
<style>

.stApp {

background: linear-gradient(
135deg,
#023e8a,
#0077b6,
#90e0ef
);

}


/* Header */

.hero {

background: rgba(255,255,255,0.95);

padding:35px;

border-radius:25px;

text-align:center;

box-shadow:0px 8px 25px rgba(0,0,0,0.25);

}


.hero h1 {

color:#0077b6;

font-size:45px;

}


.hero p {

color:#023e8a;

font-size:20px;

}



/* Cards */


.card {

background:white;

padding:20px;

border-radius:20px;

text-align:center;

height:150px;

box-shadow:0px 5px 20px rgba(0,0,0,0.25);

}


.card h2 {

font-size:40px;

}


.card h3 {

color:#0077b6;

}



/* Chat box title */

.chat-title {

background:white;

padding:15px;

border-radius:15px;

text-align:center;

color:#0077b6;

font-size:24px;

font-weight:bold;

box-shadow:0px 5px 15px rgba(0,0,0,0.2);

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



# ================= DISASTER CARDS =================


c1,c2,c3,c4 = st.columns(4)


with c1:

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


with c2:

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


with c3:

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


with c4:

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



# ================= AGENT IMPORT =================


sys.path.append("agents")


from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer



# ================= CHAT SECTION =================


st.markdown(
"""
<div class="chat-title">

🤖 Ask Climate AI Assistant

</div>

<br>

""",
unsafe_allow_html=True
)



# Visible Chat Bar

question = st.text_input(
    "",
    placeholder="💬 Example: What should people do during floods?"
)



if question:


    # User message

    with st.chat_message("user"):

        st.write(question)



    with st.chat_message("assistant"):


        with st.spinner("🌍 AI is thinking..."):


            # Router Agent

            category = route_question(question)


            # Retrieval Agent

            context = retrieve_information(question)


            # LLM Agent

            answer = generate_answer(
                question,
                context
            )


            st.info(
                "Agent Category: " + category
            )


            st.write(answer)



            with st.expander("📄 Retrieved Documents"):

                st.write(context)