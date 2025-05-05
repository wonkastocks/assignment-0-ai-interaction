# Recipe Generator using Local AI Model
# This script uses Ollama's OpenAI-compatible API to generate detailed recipe instructions
# without requiring any external API keys.

from openai import OpenAI

# Initialize the OpenAI client to connect to Ollama's local endpoint
# Note: The 'api_key' parameter is just a placeholder - Ollama ignores it
client = OpenAI(
    base_url="http://localhost:11434/v1",   # Ollama's default API endpoint
    api_key="ollama"                        # Placeholder value
)

# Configure the model and recipe parameters
model = "llava:latest"  # Using LLAVA model for recipe generation
dish = "Chicken Caesar Salad"  # The dish we want to generate a recipe for

# Prepare the chat messages for the AI model
# The system message sets the context for the AI
# The user message specifies what we want to generate
messages = [
    {"role": "system", "content": "You are a world-class chef."},
    {"role": "user", "content": (
        f"Show me the ingredients, recipe and preparation method for {dish}. "
        "Organize the answer in clear, concise bullet points."
    )},
]

# Send the chat completion request to the model
# temperature=0 means we want the most deterministic response
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0,
)

# Extract and print the generated recipe
print(response.choices[0].message.content)
