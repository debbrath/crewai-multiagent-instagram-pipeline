# 🧠 CrewAI Blog Project with Image Generation

This project uses **CrewAI Agents** with **OpenAI (via LangChain)** to:
1. Research a topic
2. Write a blog post
3. Review the post
4. Generate AI image prompts
5. Create images with Stable Diffusion

---

## 🚀 Setup

```bash
git clone <your-repo>
cd crewai_blog_project
pip install -r requirements.txt
Create .env:

env
Copy code
OPENAI_API_KEY=your_key_here
OPENAI_BASE_URL=https://models.github.ai/inference
OPENAI_MODEL=gpt-4o


python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\activate
pip install -r requirements.txt
python main.py

(venv) PS F:\Python\crewai-multiagent-instagram-pipeline> pip install --upgrade torch    






crewai-multiagent-instagram-pipeline/
│── .env
│── requirements.txt
│── main.py
│── agents.py
│── tasks.py
│── image_gen.py
│── README.md