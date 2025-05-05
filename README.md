# Food Recipe Assistant

An interactive Python script that helps users find recipes for various food dishes using local AI models via Ollama.

## Features
- Interactive command-line interface for entering dish names
- Strict input validation to ensure only valid food item names are accepted
- Generates detailed recipes with ingredients and preparation methods
- Uses local AI models for faster response times
- No API keys or external services required
- Clean and organized output format
- Validates input against special characters, numbers, and invalid formats

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

## Requirements
- Python 3.13+
- Ollama installed and running locally
- openai package (for Ollama's OpenAI-compatible API)

## Input Validation Rules
The script validates dish names according to these rules:
1. Only letters and hyphens (-) are allowed
2. No numbers, special characters, or punctuation
3. Hyphens must be part of a word (e.g., 'chicken-fried-rice' is okay)
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
