import os
import google.generativeai as genai

def list_models():
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    models = genai.list_models()
    print("Available models:")
    for model in models:
        print(f"- {model.name} (supports: {model.supported_generation_methods})")

if __name__ == "__main__":
    list_models()
