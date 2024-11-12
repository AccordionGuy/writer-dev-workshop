import os
from dotenv import load_dotenv
import writer as wf
import writer.ai

# Load environment variables from .env file
load_dotenv()

# Set the API key
wf.api_key = os.getenv('WRITER_API_KEY')

# Initialize the state
wf.init_state({
    "conversation": writer.ai.Conversation(),
    "my_app": {
        "title": "CHAT ASSISTANT"
    },
})


def generate_completion(state, payload):
    print(f"Here's what the user entered: {payload['content']}")
    state["conversation"] += payload
    print(f"Conversation: {state['conversation'].messages}")
    try:
        for index, chunk in enumerate(state["conversation"].stream_complete()):
            print(f"Chunk {index}: {chunk}")
            if not chunk.get("content"):
                chunk["content"] = ""
            state["conversation"] += chunk
            
        print(f"state['conversation']:\n{state['conversation'].messages}")
    except Exception as e:
        print(f"Error during stream_complete: {e}")
