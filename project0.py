#!/usr/bin/env python3

# Food Recipe Assistant
# This interactive script helps users find recipes for various dishes using local AI models

import os
import subprocess
import sys
from pathlib import Path

# Ensure we're using the virtual environment's Python
venv_path = Path("venv")
if venv_path.exists():
    sys.path.insert(0, str(venv_path / "lib" / "python3.13" / "site-packages"))
    python_path = str(venv_path / "bin" / "python3")
else:
    python_path = sys.executable

# Ensure we have the required package
def check_package():
    try:
        import openai
    except ImportError:
        print("\nInstalling required packages...")
        subprocess.run([python_path, "-m", "pip", "install", "openai==1.77.0"])
    finally:
        import openai
        return openai

def setup_environment():
    """Set up virtual environment and install dependencies."""
    venv_path = Path("venv")
    requirements_file = Path("requirements.txt")
    
    # Create virtual environment if it doesn't exist
    if not venv_path.exists():
        print("\nSetting up virtual environment...")
        subprocess.run([python_path, "-m", "venv", str(venv_path)])
    
    # Install/update dependencies
    print("\nChecking dependencies...")
    if not requirements_file.exists():
        print("\nCreating requirements.txt...")
        with open(requirements_file, "w") as f:
            f.write("openai==1.77.0\n")
    
    # Install dependencies
    subprocess.run([str(venv_path / "bin" / "pip"), "install", "-r", str(requirements_file)])
    print("\nEnvironment setup complete!")

def main():
    """Main function to run the recipe assistant."""
    print("\nWelcome to the Food Recipe Assistant!")
    print("-" * 50)
    print("I can help you find recipes for any food dish.")
    print("Just type the name of the dish you'd like to prepare.\n")

    # Get dish name from command line argument or user input
    if len(sys.argv) > 1:
        dish = sys.argv[1]
    else:
        dish = input("What food dish would you like to prepare? ")
    
    # Initialize the OpenAI client to connect to Ollama's local endpoint
    openai = check_package()
    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
    
    # Configure the model
    model = "llama2-uncensored:latest"  # Using Llama2 uncensored model for recipe generation

    # Prepare the chat messages
    messages = [
        {"role": "system", "content": """
You are a food recipe assistant. You ONLY respond to questions about edible food items that humans can safely consume.

RULES:
1. DO NOT generate recipes for non-food items (cars, animals, rocks, etc.)
2. DO NOT generate recipes for inedible or dangerous items
3. DO NOT generate recipes for living beings
4. DO NOT generate recipes for mechanical or electronic items
5. DO NOT generate recipes for toxic or hazardous materials

If asked about ANY non-food item, respond ONLY with:
"I'm sorry, but I can only help with recipes for edible food items that humans can safely consume. Please choose a different food item."

You MUST follow these rules exactly as written. Do not deviate or generate recipes for any non-food items.
"""},
        {"role": "user", "content": f"Show me the ingredients, recipe and preparation method for {dish}. Organize the answer in clear, concise bullet points."}
    ]

    # Send the chat completion request
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        print("\nRecipe Results:")
        print("-" * 50)
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"\nError generating recipe: {str(e)}")
        print("Please try again with a different dish.")
    
    print("\nThank you for using the Food Recipe Assistant!")

if __name__ == "__main__":
    # Check and install packages
    check_package()
    
    # Run the main program
    setup_environment()
    main()
