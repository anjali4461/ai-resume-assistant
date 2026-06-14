
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🚀 AI Resume Assistant")
st.markdown("Generate ATS-friendly resume content interactively.")

api_key = st.secrets["MISTRAL_API_KEY"]

# ---------------------------------
# LLM SETUP
# ---------------------------------

llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=api_key,
    temperature=0.7
)

# ---------------------------------
# SESSION STATE
# ---------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_mode" not in st.session_state:
    st.session_state.resume_mode = None

if "last_mode" not in st.session_state:
    st.session_state.last_mode = None

# ---------------------------------
# SIDEBAR
# ---------------------------------

with st.sidebar:

    st.header("📄 Resume Assistant")

    selected_option = st.radio(
        "Choose Section",
        [
            "Professional Summary",
            "Skills Section",
            "Project Section"
        ]
    )

    # Set Mode
    if selected_option == "Professional Summary":
        st.session_state.resume_mode = "summary"

    elif selected_option == "Skills Section":
        st.session_state.resume_mode = "skills"

    elif selected_option == "Project Section":
        st.session_state.resume_mode = "project"

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.session_state.last_mode = None
        st.rerun()

# ---------------------------------
# ASK QUESTION WHEN MODE CHANGES
# ---------------------------------

if st.session_state.resume_mode != st.session_state.last_mode:

    if st.session_state.resume_mode == "summary":

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "👋 Please enter your target role.\n\nExample: GenAI Engineer, Data Scientist, ML Engineer"
            }
        )

    elif st.session_state.resume_mode == "skills":

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "👋 Please enter your domain.\n\nExample: GenAI, Data Science, Machine Learning, Web Development"
            }
        )

    elif st.session_state.resume_mode == "project":

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "👋 Please enter your project name."
            }
        )

    st.session_state.last_mode = st.session_state.resume_mode

# ---------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------------
# CHAT INPUT
# ---------------------------------

user_input = st.chat_input(
    "Enter your role, domain, or project name..."
)

# ---------------------------------
# PROCESS INPUT
# ---------------------------------

if user_input:

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # ---------------------------------
    # PROFESSIONAL SUMMARY
    # ---------------------------------

    if st.session_state.resume_mode == "summary":

        prompt = f"""
Write a professional ATS-friendly resume summary for:

Role: {user_input}

Requirements:
- 4 to 6 lines
- Strong professional tone
- ATS optimized
- Highlight key strengths
- Suitable for resume
"""

        with st.spinner("Generating Summary..."):
            answer = llm.invoke(prompt).content

    # ---------------------------------
    # SKILLS SECTION
    # ---------------------------------

    elif st.session_state.resume_mode == "skills":

        prompt = f"""
Generate a professional ATS-friendly resume skills section.

Domain:
{user_input}

Requirements:
- Categorize skills
- Include tools
- Include frameworks
- Include programming languages
- Resume format
"""

        with st.spinner("Generating Skills Section..."):
            answer = llm.invoke(prompt).content

    # ---------------------------------
    # PROJECT SECTION
    # ---------------------------------

    elif st.session_state.resume_mode == "project":

        prompt = f"""
Generate 5 ATS-friendly resume bullet points for:

Project Name:
{user_input}

Requirements:
- Use strong action verbs
- Resume-ready language
- Quantify impact where possible
- Professional tone
"""

        with st.spinner("Generating Project Points..."):
            answer = llm.invoke(prompt).content

    else:

        answer = (
            "Please select an option from the sidebar first."
        )

    # Save AI Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()

# ---------------------------------
# DOWNLOAD LATEST AI RESPONSE
# ---------------------------------

latest_ai_response = ""

for msg in reversed(st.session_state.messages):

    if msg["role"] == "assistant":
        latest_ai_response = msg["content"]
        break

if latest_ai_response:

    st.download_button(
        label="📥 Download Latest Resume Content",
        data=latest_ai_response,
        file_name="resume_content.txt",
        mime="text/plain"
    )

