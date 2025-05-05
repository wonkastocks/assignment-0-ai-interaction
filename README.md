# Assignment 0 - AI Interaction

This repository contains the work for Assignment 0 of the Lonely Octopus Bootcamp, focusing on AI Interaction.

## Project Description
A Python script that uses local AI models (via Ollama) to generate detailed recipe instructions for various dishes. The script connects to a local Ollama endpoint and uses the OpenAI-compatible API to interact with AI models without requiring any API keys.

## Features
- Generates detailed recipes with ingredients and preparation methods
- Uses local AI models for faster response times
- No API keys or external services required
- Clean and organized output format
- Supports multiple dish types
- Easy to modify for different recipe types

## Setup Instructions
1. Install Ollama
   ```bash
   brew install ollama
   ```

2. Start Ollama server
   ```bash
   ollama serve
   ```

3. Pull the required model (LLAVA)
   ```bash
   ollama pull llava:latest
   ```

4. Run the script
   ```bash
   python3 project0.py
   ```

## Requirements
- Python 3.7+
- Ollama installed and running locally
- openai package (for Ollama's OpenAI-compatible API)

## How It Works
The script:
1. Connects to your local Ollama endpoint
2. Uses the LLAVA model to generate recipe content
3. Formats the output in a clear, organized way
4. Displays ingredients, preparation method, and cooking instructions

## Usage
Simply run the script and it will generate a recipe for Chicken Caesar Salad by default. You can modify the `dish` variable in the code to generate recipes for different dishes.

## Note
This project uses Ollama's OpenAI-compatible API endpoint, which does not require any API keys. The `api_key` parameter is just a placeholder and is ignored by Ollama.
