import streamlit as st
import requests
import json
from datetime import datetime,date

# --- Custom CSS for Dark Theme and Styling ---
st.markdown(
    """
    <style>
    /* ... [existing CSS] ... */
    .plan-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-top: 32px;
        margin-bottom: 4px;
    }
    .plan-box-enhanced {
        background: linear-gradient(135deg, #26243e 0%, #1f1f1f 100%);
        border: 2px solid #bb86fc;
        border-radius: 18px;
        box-shadow: 0 4px 24px 0 rgba(187,134,252,0.10);
        padding: 28px 22px 28px 22px;
        margin-top: 12px;
        margin-bottom: 12px;
        font-size: 17px;
        line-height: 1.7;
        color: #f3eefd;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        transition: box-shadow 0.2s;
    }
    .plan-box-enhanced strong {
        color: #bb86fc;
        font-weight: 700;
    }
    .copy-btn {
        background-color: #bb86fc;
        color: #121212;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        font-size: 16px;
        margin-top: 10px;
        cursor: pointer;
        transition: background 0.2s;
    }
    .copy-btn:hover {
        background: #9a65db;
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

    st.markdown("---")
    st.markdown(
        """
        ### ℹ️ How to get your OpenRouter API Key

        1. [Go to OpenRouter API Keys page](https://openrouter.ai/keys) (log in or sign up if needed).
        2. Click **“Create a new key”**.
        3. Copy the generated key and paste it above.

        Your API key is **only stored in your session** and sent directly and securely to OpenRouter.

        <span style="font-size: 0.94em; color: #bb86fc;">
            Need help? See the <a href="https://openrouter.ai/docs" target="_blank" style="color:#bb86fc; text-decoration:underline;">OpenRouter Docs</a>.
        </span>
        """,
        unsafe_allow_html=True,
    )

st.title("📘 AI Study Planner — Personalized Schedule Generator")
# --- User Inputs (Main Content) ---
subject = st.text_input("Subject:", key="subject")
total_hours = st.text_input("Total study hours required:", key="hours")
deadline = st.date_input("Deadline (YYYY-MM-DD):", key="deadline")


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

        today = date.today()
        days_left = (deadline - today).days + 1  # +1 to include today, remove +1 if exclusive

        if days_left <= 0:
            st.warning("The deadline must be after today. Please select a valid date.")
            st.stop()

        deadline_str = deadline.strftime("%Y-%m-%d")
        today_str = today.strftime("%Y-%m-%d")
        user_prompt = f"Create a personalized study plan for the subject '{subject}'. Provide a brief overview or key information about the subject '{subject}' to give some context. The user wants to complete a total of {total_hours_float} hours before the deadline {deadline_str}. Today is {today_str}. Distribute the hours effectively from today to the deadline and mention the daily time allocation. Also add breaks if needed and suggest tips to stay consistent."



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
