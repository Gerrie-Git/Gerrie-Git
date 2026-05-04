from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from openai import OpenAI
#from langgraph.prebuilt import create_react_agent
#from langgraph.checkpoint.memory import MemorySaver
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
cv_text = open("cv.txt").read()
job_description = open("job.txt").read()


def generate_cover_letter(client, cv, job_description):
    prompt = f"""
    You are a professional career assistant.

    Write a tailored cover letter based on:
    1. The candidate's CV
    2. The job description

    Requirements:
    - Be specific and relevant to the job
    - Highlight matching skills and experience
    - Keep it concise (max 400 words)
    - Use a professional tone

    CV:
    {cv}

    Job Description:
    {job_description}

    Only use information explicitly present in the CV.
    Do not invent experience.
    Limit words to 1000

    Return your response as JSON:
    {{
    "critique": [...],
    "improvements": [...],
    "revised_letter": "..."
    }}
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text



def review_cover_letter(client, cv, job_description, cover_letter):
    prompt = f"""
    You are a strict and detail-oriented hiring manager.

    Review the following cover letter.

    Evaluate:
    1. Relevance to the job description
    2. Use of information from the CV
    3. Clarity and structure
    4. Strength of arguments
    5. Specificity vs generic language

    Provide:
    - Bullet-point critique
    - Concrete suggestions for improvement
    - A revised version of the cover letter

    CV:
    {cv}

    Job Description:
    {job_description}

    Cover Letter:
    {cover_letter}

    Only use information explicitly present in the CV.
    Do not invent experience.
    Limit words to 1000

    Return your response in letter formatting
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
    )

    return response.output_text

@mcp.tool()
def cover_letter_generator():
    cover_letter = generate_cover_letter(client, cv_text, job_description)

    review = review_cover_letter(client, cv_text, job_description, cover_letter)

    print("=== COVER LETTER ===")
    print(cover_letter)

    print("\n=== REVIEW ===")
    print(review)

    with open("cover_letter.txt", "w", encoding="utf-8") as f:
        f.write(cover_letter)

    with open("review.txt", "w", encoding="utf-8") as f:
        f.write(review)


if __name__ == "__main__":
    mcp.run(transport="stdio")