from transformers import pipeline


# Load the Hugging Face pipeline for text generation

generator = pipeline("text-generation", model="Qwen/Qwen2.5-1.5B-Instruct")



def generate_content(topic: str):
    """Generate AI content using Hugging Face pipeline."""
    prompt = f"Create a detailed and engaging YouTube script about: {topic}"

    # Generate content
    generated_text = generator(prompt, max_length=2000, num_return_sequences=1, temperature=0.7, top_p=0.9)
    
    # Extract the generated text (it's a list of dicts)
    return generated_text[0]['generated_text']
