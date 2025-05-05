# Food Recipe Assistant
# This interactive script helps users find recipes for various dishes using local AI models

import os
import subprocess
import sys
from pathlib import Path

def setup_environment():
    """Set up virtual environment and install dependencies."""
    venv_path = Path("venv")
    requirements_file = Path("requirements.txt")
    
    # Create virtual environment if it doesn't exist
    if not venv_path.exists():
        print("\nSetting up virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)])
    
    # Activate virtual environment
    activate_script = venv_path / "bin" / "activate"
    if not activate_script.exists():
        print("\nError: Could not find virtual environment activation script.")
        sys.exit(1)
    
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
    client = OpenAI(
        base_url="http://localhost:11434/v1",   # Ollama's default API endpoint
        api_key="ollama"                        # Placeholder value
    )

    # Configure the model
    model = "llama2-uncensored:latest"  # Using Llama2 uncensored model for recipe generation

    # Define system message to focus on food-related queries
    system_message = """
You are a food recipe assistant. You only respond to questions about food dishes and recipes.
If asked about non-food topics, respond with: "I can only help with food and recipe questions."
"""

    # Prepare the chat messages
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": (
            f"Show me the ingredients, recipe and preparation method for {dish}. "
            "Organize the answer in clear, concise bullet points."
        )},
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
    setup_environment()
    main()

# Initialize the OpenAI client to connect to Ollama's local endpoint
client = OpenAI(
    base_url="http://localhost:11434/v1",   # Ollama's default API endpoint
    api_key="ollama"                        # Placeholder value
)

# Configure the model
model = "llama2-uncensored:latest"  # Using Llama2 uncensored model for recipe generation

# Define system message to focus on food-related queries
system_message = """
You are a food recipe assistant. You only respond to questions about food dishes and recipes.
If asked about non-food topics, respond with: "I can only help with food and recipe questions."
"""

# Main function to get and process user input
def get_recipe(dish):
    # Prepare the chat messages
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": (
            f"Show me the ingredients, recipe and preparation method for {dish}. "
            "Organize the answer in clear, concise bullet points."
        )},
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

# Main program loop
if __name__ == "__main__":
    print("Welcome to the Food Recipe Assistant!")
    print("-" * 50)
    print("I can help you find recipes for any food dish.")
    print("Just type the name of the dish you'd like to prepare.\n")

    # Get dish name from command line argument or user input
    import sys
    if len(sys.argv) > 1:
        dish = sys.argv[1]
    else:
        dish = input("What food dish would you like to prepare? ")
    
    # Run the recipe generator once
    get_recipe(dish)
    print("\nThank you for using the Food Recipe Assistant!")
