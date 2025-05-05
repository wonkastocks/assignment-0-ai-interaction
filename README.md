# Food Recipe Assistant

An interactive Python script that helps users find recipes for various food dishes using local AI models via Ollama.

## Features

- Generate recipes for any food dish
- Uses local AI model via Ollama API
- Input validation for food items
- Typo detection for common food items
- Error handling for non-food and non-edible items
- Interactive command-line interface
- Clean and user-friendly output formatting

## Input Validation Rules

The tool validates input based on these rules:

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

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Ollama is running:
```bash
ollama run llama2-uncensored
```

## Usage

Run the script with a dish name:
```bash
python project0.py "chicken-salad"
```

Or run without arguments to enter interactive mode:
```bash
python project0.py
```

## Requirements

- Python 3.13
- Ollama with llama2-uncensored model
- openai package (version 1.77.0) for Ollama's OpenAI-compatible API

## How It Works
The script:
1. Validates user input according to the rules above
2. Connects to your local Ollama endpoint
3. Uses the Llama2 Uncensored model to generate recipe content
4. Ensures only food-related queries are processed
5. Formats the output in a clear, organized way
6. Displays ingredients, preparation method, and cooking instructions

## Setup Instructions
1. Install Ollama
   ```bash
   brew install ollama
   ```

2. Start Ollama server
   ```bash
   ollama serve
   ```

3. Pull the required model (Llama2 Uncensored)
   ```bash
   ollama pull llama2-uncensored:latest
   ```

4. Run the script
   ```bash
   python3 project0.py
   ```
   or with a specific dish name:
   ```bash
   python3 project0.py "chicken-fried-rice"
   ```
4. No spaces at the beginning or end

## How It Works
The script:
1. Validates user input according to the rules above
2. Connects to your local Ollama endpoint
3. Uses the Llama2 Uncensored model to generate recipe content
4. Ensures only food-related queries are processed
5. Formats the output in a clear, organized way
6. Displays ingredients, preparation method, and cooking instructions

## Usage
Run the script and it will prompt you to enter a dish name. The script will validate your input and:
- If valid, generate a recipe for the dish
- If invalid, show the validation rules and ask for a valid dish name again

You can also run the script with a dish name as a command line argument:
```bash
python3 project0.py "chicken-salad"
```
