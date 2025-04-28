import google.generativeai as genai

# Configure the Gemini API
API_KEY = 'AIzaSyBr7G_IRheqrZi0oWzuB6ZLOJb875ryfts'
genai.configure(api_key=API_KEY)

def get_llm_response(prompt):
    """
    Function to interact with Google Gemini model
    """
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel('gemini-2.0-flash')

        # Generate content from the model
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    test_prompt = "Explain diabetes in simple terms."
    print(get_llm_response(test_prompt))
