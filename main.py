import os
import re
from crewai import Crew
from tasks import research_task, writing_task, review_task, image_prompt_generation_task
from image_gen import generate_images
from dotenv import load_dotenv

load_dotenv()

def run_pipeline(topic: str):
    crew = Crew(
        agents=[research_task.agent, writing_task.agent, review_task.agent, image_prompt_generation_task.agent],
        tasks=[research_task, writing_task, review_task, image_prompt_generation_task],
        verbose=True,
    )

    result = crew.kickoff(inputs={"topic": topic})

    print("\n=== Final Blog Result ===")
    print(result)

    prompts = re.findall(r'"([^"]+)"', result)
    if prompts:
        print("\n=== Extracted Prompts ===")
        for i, p in enumerate(prompts, start=1):
            print(f"{i}: {p}\n")
        generate_images(prompts[:3])
    else:
        print("No prompts found.")

if __name__ == "__main__":
    topic = input("Enter your topic: ")
    run_pipeline(topic)