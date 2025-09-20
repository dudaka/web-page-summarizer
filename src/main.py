from dotenv import load_dotenv
from openai import OpenAI

from website import Website

load_dotenv()

system_prompt = """
You are a helpful assistant that analyzes the contents of a website and provides a short summary,
ignoring text that might be navigation related.
Response in markdown.
"""

def user_prompt_for(website: Website):
    user_prompt = f"You are looking at the website titled {website.title}.\n"
    user_prompt += """
    The content of the website is as follows;
    please provide a short summary of this website in markdown.
    If it includes news or announcements, then summarize those as well.
    """
    user_prompt += website.text
    return user_prompt
    

def message_for(website: Website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]


def summarize(url: str) -> str:
    client = OpenAI()
    website = Website(url)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message_for(website)
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    url = 'https://edwarddonner.com/'
    print(summarize(url))