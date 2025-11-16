import time
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from secret_key import GEMINI_API_KEY

# Gemini model setup
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",  # Latest model
    google_api_key=GEMINI_API_KEY,
    temperature=0.7,
)

# Prompt template
prompt_template = PromptTemplate.from_template("""
You are an expert script writer who generates creative, impactful, and engaging scripts for influencers and creators.

Do not ask for additional info like target audience, personality, or tone. Just write a compelling script based on the prompt.

User Input: {user_prompt}
""")

chain = prompt_template | llm

def generate_script(user_prompt):
    for attempt in range(4):
        try:
            result = chain.invoke({"user_prompt": user_prompt})
            return result.content if hasattr(result, "content") else result
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(4)
    return "❌ Failed to generate script after multiple attempts."
