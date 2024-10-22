from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
template = """
Answer the question below.

Here is the conversation history: {context}

Questions: {question}

Answer: 
"""

model = OllamaLLM(model="llama3")  # Replace OpenAI with your LLM if different
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    print("Welcome to the chatbot. How can I help you today? ")
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("AI: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"


if __name__ == "__main__":
    handle_conversation()