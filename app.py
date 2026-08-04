import streamlit as st
import sys


# Page Configuration
st.set_page_config(
    page_title="Climate & Disaster Awareness Assistant",
    page_icon="🌍",
    layout="centered"
)


# Custom UI Design
st.markdown("""
<style>

.stApp {
    background-color: #e6f7ff;
}

.main-title {
    text-align: center;
    color: #005b96;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #003f5c;
    font-size: 20px;
}

.info-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)



# Header
st.markdown(
"""
<div class="main-title">
🌍 Climate & Disaster Awareness Assistant 🌊
</div>

<div class="subtitle">
🌧 Flood | 🌊 Tsunami | 🌀 Cyclone | ☀️ Drought | 🌱 Climate Change
</div>

<br>
""",
unsafe_allow_html=True
)



# Welcome Card
st.markdown(
"""
<div class="info-card">

<h3>🌎 Welcome</h3>

<p>
AI assistant that provides climate change and disaster awareness information.
</p>

<ul>
<li>🌧 Flood safety guidelines</li>
<li>🌊 Tsunami preparedness</li>
<li>🌀 Cyclone awareness</li>
<li>☀️ Drought information</li>
<li>🌱 Climate change knowledge</li>
</ul>

</div>
""",
unsafe_allow_html=True
)



# Connect Agents Folder
sys.path.append("agents")


from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer



# User Question

st.write("")

question = st.text_input(
    "💬 Enter your question:"
)



if question:


    # Router Agent

    category = route_question(question)


    st.info(
        f"🤖 Agent Category: {category}"
    )



    # Retrieval Agent

    context = retrieve_information(question)



    # LLM Agent

    answer = generate_answer(
        question,
        context
    )



    # Answer

    st.subheader("🤖 AI Answer")

    st.write(answer)



    # Documents

    st.subheader("📄 Retrieved Information")


    with st.expander("View Retrieved Documents"):

        st.write(context)



# Footer

st.markdown(
"""
<br><br>

<center>
🌍 Climate Disaster AI Assistant  
<br>
Powered by RAG + Agentic AI + Groq
</center>

""",
unsafe_allow_html=True
)