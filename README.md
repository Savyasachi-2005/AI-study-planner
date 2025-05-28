# 📘 AI Study Planner — Personalized Schedule Generator

![AI Study Planner Banner](https://user-images.githubusercontent.com/your-banner-url.png)

A modern, beautiful Streamlit web app that generates a **personalized study plan** based on your subject, total study hours, and deadline. Powered by OpenRouter's AI models, it helps you break down your goals into actionable daily schedules — complete with breaks and tips to stay consistent.

---

## ✨ Features

- **Modern, dark-themed interface** for easy viewing any time of day.
- **Personalized study timetable:** Just enter your subject, required hours, and deadline.
- **AI-powered scheduling:** Uses OpenRouter API for smart daily hour allocations.
- **Copy-to-clipboard** one-click button for your generated plan.
- **Sidebar guidance:** Easy instructions to get your OpenRouter API key.
- **Secure:** Your API key is stored only in your session and used only to generate your plan.

---

## 🚀 Getting Started

### 1. **Clone the repository**

```bash
git clone https://github.com/Savyasachi-2005/AI-study-planner.git
cd AI-study-planner
```

### 2. **Install dependencies**

We recommend using a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. **Run the app**

```bash
streamlit run app.py
```

---

## 🛡️ How to Get Your OpenRouter API Key

1. Go to [OpenRouter API Keys page](https://openrouter.ai/keys) (log in or sign up if needed).
2. Click **“Create a new key”**.
3. Copy the generated key and paste it in the sidebar when prompted.

> Your API key is only stored in your session and sent directly to OpenRouter for generating your study plan.

---

## 🖥️ Usage

1. **Enter your OpenRouter API key** in the sidebar (see above).
2. **Enter the subject** you want to study.
3. **Enter total study hours required.**
4. **Pick your deadline** (the last day you want to study).
5. Click **Generate Study Plan**.
6. **Copy and use** your personalized plan!

---

## 🖌️ Customization

- **Themes & CSS:** The app uses custom CSS for a sleek, modern look. You can tweak colors and layout in `app.py`.
- **AI Model:** Uses `meta-llama/llama-4-maverick:free` via OpenRouter; you can change the model in the API call.
- **Plan Output:** The result is displayed in a visually enhanced, copy-friendly box.

---

## 📝 Example

![Example Screenshot](https://user-images.githubusercontent.com/your-screenshot-url.png)

---

## 💡 Why Use This?

- Stay consistent and organized in your studies
- Avoid burnout with planned breaks
- Make the most of your time before exams or deadlines

---

## ⚠️ Disclaimer

This planner is a tool to assist your study organization. Please review and adjust the plan as needed for your individual needs.

---

## 🤝 Contributing

Pull requests and suggestions welcome! Please open an issue or PR to discuss changes.

---

## 📄 License

[MIT](LICENSE)

---

**Made with ❤️ by [Savyasachi-2005](https://github.com/Savyasachi-2005)**
