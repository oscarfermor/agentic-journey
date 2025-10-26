import os
from google import genai
from dotenv import load_dotenv
import time
import asyncio

load_dotenv()
GEMINI_API_TOKEN = os.getenv("GEMINI_API_TOKEN")
client = genai.Client(api_key=GEMINI_API_TOKEN)


async def generate_content(prompt: str) -> str:
    response = await client.aio.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text.strip()


async def parallel_tasks():
    topic = "a friendly robot exploring a jungle"
    prompts = [
        f"Write a short, adventurous story idea about {topic}.",
        f"Write a short, funny story idea about {topic}.",
        f"Write a short, mysterious story idea about {topic}.",
    ]
    # Run tasks concurrently and gather results
    start_time = time.time()
    tasks = [generate_content(prompt) for prompt in prompts]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

    print("\n--- Individual Results ---")
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}\n")

    # Aggregate results and generate final story
    story_ideas = "\n".join(
        [f"Idea {i+1}: {result}" for i, result in enumerate(results)]
    )
    aggregation_prompt = f"Combine the following three story ideas into a single, cohesive summary paragraph:{story_ideas}"
    aggregation_response = await client.aio.models.generate_content(
        model="gemini-2.5-flash", contents=aggregation_prompt
    )
    return aggregation_response.text


result = asyncio.run(parallel_tasks())
print(f"\n--- Aggregated Summary ---\n{result}")
