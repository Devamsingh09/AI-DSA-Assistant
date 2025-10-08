

## 🚀 STEP-BY-STEP: Deploy Project to GitHub

### 🧩 1. Initialize Git in your project folder

Open the terminal in the root of your project (where `.gitignore` and `requirements.txt` are):

```bash
git init
```

This creates a local Git repository.

---

### 🧹 2. Add all files (except the ones in `.gitignore`)

```bash
git add .
```

---

### 📝 3. Commit the code

```bash
git commit -m "Initial commit - AI DSA Assistant"
```

---

### 🌐 4. Create a new GitHub repository

Go to 👉 [https://github.com/new](https://github.com/new)

* Repository name: `AI-DSA-Assistant`
* Description: “An AI-powered DSA code assistant using Gemini and FAISS”
* Keep it **Public**
* Don’t add a README (we’ll push ours)

Click **Create repository**.

---

### 🔗 5. Connect your local repo to GitHub

After creating it, GitHub shows some commands — use these:

```bash
git remote add origin https://github.com/<your-username>/AI-DSA-Assistant.git
git branch -M main
git push -u origin main
```

Example:

```bash
git remote add origin https://github.com/Devamsingh09/AI-DSA-Assistant.git
git branch -M main
git push -u origin main
```

---

### ✅ 6. Confirm

Go to your GitHub repo URL — your files should now appear there!

---

## ⚙️ Optional but Recommended

### Add README.md

Create a simple `README.md` at the project root:

````markdown
# 💡 AI DSA Assistant

A RAG-based DSA code generator using LangChain, Gemini, and FAISS.  
Uploads DSA PDFs, indexes them, and generates structured solutions (Brute Force → Improved → Optimal).

### 🛠️ Tech Stack
- Python 3.10+
- Streamlit
- LangChain
- Google Gemini API
- FAISS

### ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app/main.py
````

### ⚡ Environment Variables

```
GOOGLE_API_KEY=your_api_key_here
```

````

---

### To push updates later
Whenever you make new changes:

```bash
git add .
git commit -m "Updated main logic / UI"
git push
````
