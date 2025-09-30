from crewai import Agent
from langchain_openai import ChatOpenAI
import os

# Load from environment
openai_llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
    model=os.getenv("OPENAI_MODEL", "gpt-4o")
)

# Research Agent
researcher = Agent(
    role="Content Researcher",
    goal="Research engaging and factually accurate content on {topic}",
    backstory=(
        "You're working on researching a blog article about the topic: {topic}. "
        "You collect information that helps the audience learn something "
        "and make informed decisions."
    ),
    allow_delegation=False,
    verbose=True,
    llm=openai_llm,
)

# Writer Agent
writer = Agent(
    role="Content Writer",
    goal="Write insightful and factually accurate opinion pieces about {topic}",
    backstory=(
        "You're crafting a new opinion piece about {topic}. "
        "You base your work on the researcher's findings."
    ),
    allow_delegation=False,
    verbose=True,
    llm=openai_llm,
)

# Reviewer Agent
reviewer = Agent(
    role="Reviewer",
    goal="Review, edit, and approve the blog post to align with writing standards.",
    backstory=(
        "You ensure the content is clear, professional, and avoids unnecessary controversy."
    ),
    allow_delegation=False,
    verbose=True,
    llm=openai_llm,
)

# Image Prompt Generator Agent
image_prompt_generator = Agent(
    role="Image Prompt Generator",
    goal=(
        "Transform blog content into descriptive prompts suitable for AI image generation."
    ),
    backstory=(
        "You generate creative but neutral image prompts that support the article’s themes."
    ),
    allow_delegation=False,
    verbose=True,
    llm=openai_llm,
)