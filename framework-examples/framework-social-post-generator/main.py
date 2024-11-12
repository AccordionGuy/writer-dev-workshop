import os
import re
from dotenv import load_dotenv
import writer as wf
import writer.ai

# Load environment variables from .env file
load_dotenv()

# Set the API key
wf.api_key = os.getenv('WRITER_API_KEY')

# Initialize the state
wf.init_state({
    "topic": "writing",
    "message": "",
    "tags": {},
    "posts": "",
    "my_app": {
        "title": "SOCIAL POST GENERATOR"
    }
})


def generate_and_display_posts_and_tags(state):
    # Display message
    state["message"] = "% Generating social media posts and tags for you..."

    # Generate and display social posts
    prompt = f"You are a social media expert. Generate 5 engaging social media posts about {state['topic']}. Include emojis, and put a blank line between each post."
    state["posts"] = writer.ai.complete(prompt)

    # Generate and display hashtags
    prompt = f"You are a social media expert. Generate around 5 hashtags about {state['topic']}, delimited by spaces. For example, #dogs #cats #ducks #elephants #badgers"
    pattern = pattern = r"#\w+"
    hashtags = re.findall(pattern, writer.ai.complete(prompt))
    state["tags"] = {item: item for item in hashtags}

    # Hide message
    state["message"] = ""
