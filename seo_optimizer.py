import re

def optimize_content(content: str):
    """Optimize the generated content for SEO."""
    
    # Example: Simple SEO enhancements (can be customized for more complex logic)
    title = "SEO Optimized Title: " + content[:100] + "..."
    description = "SEO Optimized Description: " + content[:550] + "..."
    tags = re.findall(r'\b\w+\b', content.lower())[:10]  # Extract the first 10 words as tags
    
    return {
        "content": content,
        "metadata": {
            "title": title,
            "description": description,
            "tags": tags
        }
    }
