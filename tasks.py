from crewai import Task
from agents import researcher, writer, reviewer, image_prompt_generator

# Research Task
research_task = Task(
    description=(
        "Research trends, key players, and news on {topic}. "
        "Identify the audience and make an outline with SEO keywords."
    ),
    expected_output="Content plan with outline, SEO keywords, and resources.",
    agent=researcher,
)

# Writing Task
writing_task = Task(
    description=(
        "Write a blog post on {topic} using the content plan. "
        "Include introduction, body, conclusion, and SEO keywords."
    ),
    expected_output="Markdown blog post with 2–3 paragraphs per section.",
    agent=writer,
)

# Review Task
review_task = Task(
    description="Review the blog post for grammar, clarity, and alignment with style guide.",
    expected_output="Final polished blog post in Markdown.",
    agent=reviewer,
)

# Image Prompt Task
image_prompt_generation_task = Task(
    description=(
        "Generate 2–3 descriptive image prompts based on the reviewed blog post."
    ),
    expected_output="Plain text image prompts including style and theme.",
    agent=image_prompt_generator,
)