"""
project0.py
----------------------------------------------
A friendly AI chatbot that helps with recipe recommendations and meal planning.

Prereqs:
    1. ollama serve          # in another terminal
    2. ollama pull llama2:latest
    3. pip install --upgrade openai   # inside your venv
    4. python3 project0.py

This script uses Ollama's OpenAI-compatible API to create a helpful recipe assistant.
"""

from openai import OpenAI
import json

# Connect to Ollama’s OpenAI-compatible endpoint
client = OpenAI(
    base_url="http://localhost:11434/v1",  # default Ollama port
    api_key="ollama",                      # dummy value; Ollama ignores it
)

model = "llama2:latest"  # Using a more ethical model

def get_recipe_recommendation(ingredients=None, dietary_restrictions=None):
    """Get recipe recommendations based on available ingredients and dietary restrictions."""
    system_prompt = """
    You are a helpful recipe assistant. Your job is to suggest delicious and healthy recipes.
    Always provide clear, step-by-step instructions.
    """
    
    user_prompt = """
    I need recipe suggestions. Please provide:
    1. A list of 3-5 recipe options
    2. For each recipe:
       - Ingredients needed
       - Cooking time
       - Difficulty level
       - Nutritional information
    """
    
    if ingredients:
        user_prompt += f"\nI have these ingredients: {', '.join(ingredients)}"
    
    if dietary_restrictions:
        user_prompt += f"\nI need to follow these dietary restrictions: {', '.join(dietary_restrictions)}"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content

def main():
    print("Welcome to Recipe Assistant!")
    print("-" * 40)
    
    ingredients = input("Enter ingredients you have (comma-separated): ").split(',')
    dietary_restrictions = input("Enter dietary restrictions (comma-separated): ").split(',')
    
    print("\nGenerating recipe recommendations...")
    print("-" * 40)
    
    recommendations = get_recipe_recommendation(ingredients, dietary_restrictions)
    print(recommendations)

if __name__ == "__main__":
    main()
