import streamlit as st
import requests
import json
from datetime import datetime

# --- Custom CSS for Dark Theme and Styling ---
st.markdown(
    """
    <style>
    body, .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3 {
        color: #bb86fc;
        font-weight: 700;
    }
    div.stTextInput > div > input, div.stDateInput > div > input {
        background-color: #1f1f1f;
        color: #e0e0e0;
        border: 1px solid #bb86fc;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    div.stButton > button {
        background-color: #bb86fc;
        color: #121212;
        font-weight: 700;
        padding: 12px 24px;
        border-radius: 12px;
        border: none;
        transition: background-color 0.3s ease;
        width: 100%;
        font-size: 18px;
        cursor: pointer;
        margin-top: 12px;
    }
    div.stButton > button:hover {
        background-color: #9a65db;
    }
    .plan-box {
        background-color: #1f1f1f;
        border: 1px solid #bb86fc;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        white-space: pre-wrap;
        font-size: 16px;
        color: #d0d0d0;
    }
    .main > div {
        max-width: 700px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar for API Key ---
with st.sidebar:
    st.header("🔑 API Authentication")
    api_key = st.text_input("Enter your OpenRouter API Key:", type="password", key="api_key")
    if not api_key:
        st.info("Please enter your API key to use the study planner.")

# --- Main Page ---
st.title("📘 AI Study Planner — Personalized Schedule Generator")
st.write(
    "Generate a personalized timetable for your studies. "
    "Just enter your subject, total study hours, and your deadline."
)

# --- User Inputs (Main Content) ---
subject = st.text_input("Subject:", key="subject")
total_hours = st.text_input("Total study hours required:", key="hours")
deadline = st.date_input("Deadline (YYYY-MM-DD):", key="deadline")

# --- Generate Study Plan Button ---
if st.button("Generate Study Plan"):
    if not api_key:
        st.warning("Please enter your OpenRouter API key in the sidebar.")
    elif not subject or not total_hours or not deadline:
        st.warning("Please fill in all fields!")
    else:
        try:
            total_hours_float = float(total_hours)
            if total_hours_float <= 0:
                raise ValueError
        except ValueError:
            st.warning("Please enter a valid, positive number for total study hours.")
            st.stop()

        deadline_str = deadline.strftime("%Y-%m-%d")
        user_prompt = (
            f"Create a personalized study plan for the subject '{subject}'.\n"
            f"The user wants to complete a total of {total_hours_float} hours before the deadline {deadline_str}.\n"
            "Distribute the hours effectively over the days and mention the daily time allocation.\n"
            "Also add breaks if needed and suggest tips to stay consistent."
        )

        payload = {
            "model": "meta-llama/llama-4-maverick:free",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a professional academic assistant who generates study timetables."
                },
                {"role": "user", "content": user_prompt}
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        API_URL = "https://openrouter.ai/api/v1/chat/completions"

        try:
            with st.spinner("Generating your personalized study plan..."):
                response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
                response.raise_for_status()
                result = response.json()
                reply = result["choices"][0]["message"]["content"].strip()

            st.subheader("📅 Your Personalized Study Plan:")
            st.markdown(
                f'<div class="plan-box">{reply}</div>',
                unsafe_allow_html=True
            )
        except requests.exceptions.HTTPError as http_err:
            st.error(f"HTTP error occurred: {http_err}")
            st.text(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")

# --- Optional: Helper text at the bottom of sidebar ---
with st.sidebar:
    st.markdown("---")
    st.caption("Your API key is only stored in your session and never sent elsewhere except to OpenRouter for generating your plan.")
