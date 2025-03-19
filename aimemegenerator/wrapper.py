from . import generator

def AIMemeGenerator(prompt, output_folder="memes", openai_key=None):
    """
    Generate a meme based on the given prompt.
    
    Args:
        prompt (str): Text prompt describing what kind of meme to generate
        output_folder (str): Name of the folder where memes will be saved (default: "memes")
        openai_key (str): OpenAI API key. If not provided, will try to get from environment
    
    Returns:
        str: Absolute path to the generated meme image
    """
    # Generate a single meme with default settings
    results = generator.generate(
        user_entered_prompt=prompt,
        meme_count=1,
        output_folder=output_folder,
        noUserInput=True,
        image_platform="openai",
        openai_key=openai_key
    )
    
    # Return just the file path of the generated meme
    if results and len(results) > 0:
        return results[0]["file_path"]
    return None