#!/usr/bin/env python3

"""
Food Recipe Assistant

This interactive script helps users find recipes for various food dishes using local AI models via Ollama.
It validates user input to ensure only valid food item names are processed and generates detailed recipes.
"""

import os
import subprocess
import sys
from pathlib import Path

# Ensure we're using the virtual environment's Python
# This allows the script to use the correct Python version and packages
venv_path = Path("venv")
if venv_path.exists():
    sys.path.insert(0, str(venv_path / "lib" / "python3.13" / "site-packages"))
    python_path = str(venv_path / "bin" / "python3")
else:
    python_path = sys.executable

# Ensure we have the required package
def check_package():
    """
    Check if the required Python packages are installed.
    If not, install them and return the openai module.
    """
    try:
        import openai
    except ImportError:
        print("\nInstalling required packages...")
        subprocess.run([python_path, "-m", "pip", "install", "openai==1.77.0"])
    finally:
        import openai
        return openai

def validate_dish_name(dish):
    """
    Validate that the dish name contains only letters and hyphens,
    with hyphens only allowed as part of words.
    Also checks if the dish name appears to be a real food item using a more comprehensive approach.
    
    Returns True if the dish name is valid and appears to be a real food item, False otherwise.
    
    Validation Rules:
    1. Format Validation:
       - Only letters and hyphens (-) are allowed
       - No numbers, special characters, or punctuation
       - Hyphens must be part of a word (e.g., 'chicken-fried-rice' is okay)
       - No spaces at the beginning or end
    
    2. Food Item Recognition:
       - Checks against a comprehensive list of known food items
       - Handles common typos (e.g., "kali" for "kale")
       - Recognizes both single ingredients and complete dishes
       - Validates compound food items with hyphens
    
    3. Non-Edible Item Detection:
       - Detects and rejects non-food items (e.g., cars, computers, animals)
       - Provides specific error messages for non-edible items
       - Lists examples of non-edible categories
    """
    # Remove spaces at the beginning and end
    dish = dish.strip()
    
    # Check if dish is empty after stripping
    if not dish:
        return False
    
    # Check for invalid characters
    if any(char in dish for char in "0123456789!@#$%^&*()_+=|}{[]\\\"':;?/>.<,~`"):
        return False
    
    # Check for hyphens at start or end
    if dish.startswith('-') or dish.endswith('-'):
        return False
    
    # Check for double hyphens
    if '--' in dish:
        return False
    
    # Check for hyphens not between letters
    for i, char in enumerate(dish):
        if char == '-' and (i == 0 or i == len(dish) - 1 or not dish[i-1].isalpha() or not dish[i+1].isalpha()):
            return False
    
    # Check if the dish name appears to be a real food item
    # First check against common food words
    common_food_words = set("""
    pizza pasta salad sandwich soup burger steak chicken beef pork lamb fish
    rice noodles pasta bread cake cookies pie ice-cream smoothie shake
    salad sandwich wrap taco burrito enchilada lasagna macaroni spaghetti
    meatballs meatloaf roast stew chili omelette frittata quiche tofu
    tempeh falafel hummus tabbouleh baba-ganoush dolma kebab shawarma
    kale spinach broccoli carrots tomatoes cucumbers lettuce zucchini
    bell-peppers onions garlic ginger lemon lime orange apple banana
    strawberry blueberry raspberry blackberry peach plum apricot
    coconut almonds walnuts cashews peanuts pistachios
    yogurt cheese butter milk cream eggs
    """.split())
    
    # Convert dish to lowercase and split into words
    dish_words = set(dish.lower().split('-'))
    
    # Check if any of the words are common food words
    if any(word in common_food_words for word in dish_words):
        return True
    
    # Check for common typos in food words
    typo_corrections = {
        'kali': 'kale',
        'kalee': 'kale',
        'kalea': 'kale',
        'spinnach': 'spinach',
        'spinnage': 'spinach',
        'spinech': 'spinach',
        'broccli': 'broccoli',
        'broccoli': 'broccoli',
        'carots': 'carrots',
        'carrotts': 'carrots',
        'tomatos': 'tomatoes',
        'tomatoes': 'tomatoes',
        'cucumbers': 'cucumbers',
        'lettuse': 'lettuce',
        'lettus': 'lettuce',
        'zuchini': 'zucchini',
        'zucchini': 'zucchini',
        'peppers': 'peppers',
        'garlic': 'garlic',
        'ginger': 'ginger',
        'lemon': 'lemon',
        'lime': 'lime',
        'orange': 'orange',
        'apple': 'apple',
        'banana': 'banana',
        'strawberry': 'strawberry',
        'blueberry': 'blueberry',
        'raspberry': 'raspberry',
        'blackberry': 'blackberry',
        'peach': 'peach',
        'plum': 'plum',
        'apricot': 'apricot',
        'coconut': 'coconut',
        'almonds': 'almonds',
        'walnuts': 'walnuts',
        'cashews': 'cashews',
        'peanuts': 'peanuts',
        'pistachios': 'pistachios',
        'yogurt': 'yogurt',
        'cheese': 'cheese',
        'butter': 'butter',
        'milk': 'milk',
        'cream': 'cream',
        'eggs': 'eggs'
    }
    
    # Check if the input is a typo of a known food item
    if dish.lower() in typo_corrections:
        return True
    
    # Check if it's a non-edible item
    non_edible_items = set("""
    car cars automobile automobile parts engine transmission
    battery tires wheels brakes suspension steering
    computer laptop desktop monitor keyboard mouse
    phone mobile smartphone tablet camera television
    furniture chair table couch bed dresser wardrobe
    clothing shirt pants jeans jacket dress shoes
    tools hammer drill screwdriver saw wrench pliers
    animals dog cat bird fish reptile insect
    plants tree flower grass bush cactus
    electronics circuit board motherboard processor
    chemicals acid base poison toxic hazardous
    machinery engine motor generator compressor
    building house apartment building structure
    vehicle motorcycle truck bus train plane
    """.split())
    
    # If it contains any non-edible words, reject it
    if any(word in non_edible_items for word in dish_words):
        print(f"\nError: {dish} is not an edible food item.")
        print("Examples of non-edible items include: cars, computers, animals, and chemicals.")
        print("Please enter a real food item name.")
        return False
    
    # If it's not a common food word and not a non-edible item,
    # let the AI decide if it's a valid food item
    return True

def setup_environment():
    """
    Set up the virtual environment and install required dependencies.
    Creates a virtual environment if it doesn't exist and installs the required packages.
    """
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
    """
    Main function that runs the recipe assistant.
    Handles user input, validates dish names, and generates recipes.
    """
    print("\nWelcome to the Food Recipe Assistant!")
    print("-" * 50)
    print("I can help you find recipes for any food dish.")
    print("Just type the name of the dish you'd like to prepare.\n")

    # Get valid dish name from command line argument or user input
    dish = None
    if len(sys.argv) > 1:
        dish = sys.argv[1]
        if not validate_dish_name(dish):
            print(f"\nInvalid dish name '{dish}'. Please run the script with a valid dish name.")
            print("Examples: pizza, chicken-salad, spaghetti-bolognese")
            return
    else:
        while dish is None:
            dish = input("What food dish would you like to prepare? ").strip()
            if not validate_dish_name(dish):
                print("\nInvalid dish name. Please enter a real food item.")
                print("Examples: pizza, chicken-salad, spaghetti-bolognese")
                print("\nRules:")
                print("1. Only letters and hyphens (-) are allowed")
                print("2. No numbers, special characters, or punctuation")
                print("3. Hyphens must be part of a word (e.g., 'chicken-fried-rice' is okay)")
                print("4. No spaces at the beginning or end")
                print("\nPlease try again with a valid dish name.")
                dish = None
                continue

    # Initialize the OpenAI client to connect to Ollama's local endpoint
    openai = check_package()
    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
    
    # Configure the model
    model = "llama2-uncensored:latest"  # Using Llama2 uncensored model for recipe generation

    # Prepare the chat messages with strict system prompt
    messages = [
        {"role": "system", "content": """
You are a food recipe assistant. You ONLY respond to questions about edible food items that humans can safely consume.

RULES:
1. DO NOT generate recipes for non-food items (cars, animals, rocks, etc.)
2. DO NOT generate recipes for inedible or dangerous items
3. DO NOT generate recipes for living beings
4. DO NOT generate recipes for mechanical or electronic items
5. DO NOT generate recipes for toxic or hazardous materials
6. DO NOT generate recipes for non-existent food items
7. DO NOT make up recipes for random strings or gibberish

If asked about ANY non-food item or non-existent food item, respond ONLY with:
"I'm sorry, but I can only help with recipes for edible food items that humans can safely consume. Please choose a different food item."

You MUST follow these rules exactly as written. Do not deviate or generate recipes for any non-food items or non-existent food items.
"""},
        {"role": "user", "content": f"Show me the ingredients, recipe and preparation method for {dish}. Organize the answer in clear, concise bullet points."}
    ]

    # Send the chat completion request and validate the response
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0,
        )
        
        # Get the response content
        response_content = response.choices[0].message.content
        
        # Check if the response indicates an invalid food item
        if "I'm sorry" in response_content.lower() or "not a food item" in response_content.lower():
            print("\nInvalid food item. Please enter a real food item name.")
            print("Examples: pizza, chicken-salad, spaghetti-bolognese")
            return
            
        print("\nRecipe Results:")
        print("-" * 50)
        print(response_content)
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
