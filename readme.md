# 🧠 CrewAI Multi-Agent Instagram Pipeline 

This project automates the end-to-end Instagram content pipeline using CrewAI multi-agent systems.
It can research a topic, write content, review drafts, generate image prompts, and finally produce AI images (via Segmind, Stable Diffusion, or Nano Banana).

This project uses **CrewAI Agents** with **OpenAI (via LangChain)** to:
1. Research a topic
2. Write a blog post
3. Review the post
4. Generate AI image prompts
5. Create images with Stable Diffusion


```
<br/>

## ✨ Features

- 🧠 Research Agent – finds insights on a given topic

- ✍️ Writer Agent – drafts engaging Instagram-style content

- ✅ Reviewer Agent – improves and fact-checks text

- 🎨 Image Prompt Agent – generates prompts for visuals

- 🖼️ Image Generator – creates final images via external APIs

---
📂 Project Structure

```
crewai-multiagent-instagram-pipeline/
│── .env                # API keys & secrets
│── requirements.txt    # Python dependencies
│── main.py             # Pipeline entry point
│── agents.py           # Multi-agent definitions
│── tasks.py            # Task orchestration
│── image_gen.py        # Image generation integration
│── README.md           # Documentation

```
```
<br/>

## ⚙️ Setup

- 1. Clone the repo:
     
```bash
git clone https://github.com/debbrath/crewai-multiagent-instagram-pipeline.git
cd crewai-multiagent-instagram-pipeline

- 2. Create and activate a virtual environment:

  # On Windows PowerShell
  python -m venv venv
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  venv\Scripts\activate
  
  On Linux/Mac
  python -m venv env
  source env/bin/activate
  
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  cd F:\Python\Multi-Tool-Medical-AIAgent
  .\.venv\Scripts\Activate.ps1
  
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt

-3. Install dependencies:
  pip install -r requirements.txt

- 4. Add a .env file:
  OPENAI_API_KEY=your_openai_key
  SERPAPI_API_KEY=your_serpapi_key
  IMAGERY_API_KEY=your_segmind_or_nanobanana_key
  OPENAI_MODEL=gpt-4o

```
<br/>

## ▶️ Run 

python main.py

Example:

Enter topic: AI in Healthcare


✅ The pipeline will:

Research the topic

Generate a caption + blog-style content

Create an AI image prompt

Generate images

Save outputs locally

```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/1.png)
```

```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/2.png)
```

```
![Screenshot](https://github.com/debbrath/crewai-multiagent-instagram-pipeline/blob/main/image/3.png)
```

```
<br/>

## 🛠 Technologies Used

Python 3.12+

CrewAI

LangChain

Segmind / Stable Diffusion API

SerpAPI

<br/>

---

✍️ Author

Debbrath Debnath

📫 [Connect on LinkedIn](https://www.linkedin.com/in/debbrathdebnath/)

🌐 [GitHub Profile](https://github.com/debbrath) 




