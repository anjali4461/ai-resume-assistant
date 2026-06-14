# 🚀 AI Resume Assistant

An AI-powered Resume Assistant built with **Streamlit**, **LangChain**, and **Mistral AI** that helps users generate ATS-friendly resume content including professional summaries, skills sections, and project descriptions.

---

## 📌 Features

### 🎯 Professional Summary Generator

Generate concise and ATS-friendly resume summaries based on a target job role.

### 🛠️ Skills Section Generator

Create categorized technical skills sections tailored to a specific domain such as:

* Generative AI
* Data Science
* Machine Learning
* Web Development
* Software Engineering

### 📌 Project Section Generator

Generate professional, ATS-optimized project bullet points using strong action verbs and measurable impact statements.

### 💬 Interactive Chat Interface

* User-friendly chat-based interaction
* Dynamic prompts based on selected resume section
* Real-time AI-generated responses

### 📥 Download Generated Content

Download the latest generated resume content as a text file for future use.

---

## 🏗️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Mistral AI**
* **python-dotenv**

---

## 📂 Project Structure

```text
AI-Resume-Assistant/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Assistant.git

cd AI-Resume-Assistant
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser at:

```text
http://localhost:8501
```

---

## 🚀 How It Works

### Professional Summary

1. Select **Professional Summary** from the sidebar.
2. Enter your target role.
3. The assistant generates an ATS-friendly resume summary.

---

### Skills Section

1. Select **Skills Section** from the sidebar.
2. Enter your domain.
3. The assistant generates a categorized skills section.

---

### Project Section

1. Select **Project Section** from the sidebar.
2. Enter your project name.
3. The assistant generates ATS-friendly project bullet points.

---

## 📸 Application Workflow

```text
Sidebar Selection
        │
        ▼
User Input
(Role / Domain / Project)
        │
        ▼
Mistral AI
        │
        ▼
Generated Resume Content
        │
        ▼
Download Output
```

---

## 🎯 ATS Optimization

The generated content is designed to:

* Use professional language
* Include relevant keywords
* Improve ATS compatibility
* Follow industry-standard resume formatting
* Highlight skills and achievements effectively

---

## 📦 Required Packages

```txt
streamlit
langchain
langchain-mistralai
python-dotenv
```

---

## 🔮 Future Enhancements

* Resume PDF generation
* Resume scoring and ATS analysis
* Experience section generator
* Education section generator
* Cover letter generation
* LinkedIn profile optimization
* Multiple resume templates
* Export to PDF and DOCX

---

## 👨‍💻 Author

Developed as an AI-powered resume-building assistant using Streamlit and Mistral AI.

---

## 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute it for educational and personal projects.

Website Link: https://ai-resume-assistant-gtdb7kbnaukpjxftjzwtac.streamlit.app/
