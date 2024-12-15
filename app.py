import gradio as gr
from ai_generator import generate_content
from seo_optimizer import optimize_content

def generate_and_optimize_content(topic: str):
    # Generate content using Hugging Face model
    generated_content = generate_content(topic)
    
    # Optimize the content for SEO
    optimized_content = optimize_content(generated_content)
    
    # Return the optimized content and SEO details
    return optimized_content["content"], optimized_content["metadata"]["title"], optimized_content["metadata"]["description"]

# Gradio Interface
iface = gr.Interface(
    fn=generate_and_optimize_content,  # Function to call
    inputs=[gr.Textbox(label="Enter Topic", placeholder="Enter YouTube topic here...")],  # User input
    outputs=[
        gr.Textbox(label="Generated Content"),  # Generated content
        gr.Textbox(label="SEO Title"),  # SEO optimized title
        gr.Textbox(label="SEO Description")  # SEO optimized description
    ],
    live=True,  # Enable live mode for real-time output
    title="YouTube AI Content Generator",  # App title
    description="Generate SEO-optimized YouTube content on any topic using AI."
)

# Launch the interface
iface.launch()
