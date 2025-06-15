from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from firebase_config import db
from dotenv import load_dotenv
import datetime
import os
import asyncio

# Load your .env file (to get API keys)
load_dotenv()

# Initialize LangChain model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash",
    temperature=0.7
)

# Prompt Template
prompt = PromptTemplate.from_template("User: {input}/nBot:")

# chat function
async def chat(user_input):
    formatted_prompt = prompt.format(input=user_input)
    response = await llm.ainvoke(formatted_prompt)

    # Get current date
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")

    # Save to: chat_history/{today}/messages/{random_id}

    db.collection("chat_history").document(today).collection("messages").add({
              "timestamp": datetime.datetime.utcnow(),
              "User": user_input,
              "Bot": response.content
       })


    return response.content
# View previous chats
def view_chat_history():
    chat_history = db.collection("chat_history").order_by("timestamp").stream()
    for entry in chat_history:
        data = entry.to_dict()
        print(f"🧑 User: {data['User']}")
        print(f"🤖 Bot : {data['Bot']}")
        print("-" * 30)

