# Directory structure should be:
'''
Full-Stack-AI-Meme-Generator/
├── aimemegenerator/
│   ├── __init__.py
│   ├── generator.py  (renamed from paste.py)
│   └── wrapper.py
├── testit.py
└── memes/
'''




from aimemegenerator import AIMemeGenerator
import os
from dotenv import load_dotenv
load_dotenv()

# Make sure the memes directory exists
if not os.path.exists("memes"):
    os.makedirs("memes")

# Set your OpenAI API key
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
# Generate the meme
try:
    meme_path = AIMemeGenerator(
        "something funny with dogs and an elephant",
        openai_key=OPENAI_API_KEY  # Pass the API key directly
    )
    print(f"Meme saved at: {meme_path}")
except Exception as e:
    print(f"Error generating meme: {str(e)}")
    