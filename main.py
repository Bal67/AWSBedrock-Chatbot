import os
import boto3
import streamlit as st
from langchain.chains import ConversationChain
from langchain_community.chat_models import BedrockChat
from langchain.memory import ConversationBufferMemory

# Set up AWS credentials
os.environ["AWS_ACCESS_KEY_ID"] = ""
os.environ["AWS_SECRET_ACCESS_KEY"] = ""
os.environ["AWS_REGION"] = "us-east-1"


# Boto3 Bedrock Runtime client
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Claude 3 model 
llm = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    client=bedrock_client,
    model_kwargs={"temperature": 0.7, "max_tokens": 1024}
)

# Setup memory for the conversation
memory = ConversationBufferMemory(return_messages=True)

# LangChain ConversationChain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

# Streamlit interface
st.set_page_config(page_title="Claude 3 Chatbot", layout="wide")
st.title("Claude 3 Chatbot via AWS Bedrock")

# Initialize session history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])



context = "Paris is the capital of France. It is famous for the Eiffel Tower. Singapore is a city-state in Southeast Asia known for its cleanliness and modern architecture. The Great Wall of China is a historic fortification that stretches across northern China. The Amazon Rainforest is the largest tropical rainforest in the world, located in South America."

user_input = st.chat_input("Ask a question based on the context above...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
    You are a helpful assistant. Use the following context to answer the user's question.

    Context:
    {context}

    User's question: {user_input}

    Answer:
    """
    response = llm.invoke(prompt)
    answer = response.content 

    with st.chat_message("assistant"):
        st.markdown(answer)


    st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": answer})