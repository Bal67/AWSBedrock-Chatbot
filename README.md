# AWSBedrock-Chatbot

This repository contains a simple chatbot interface built with Streamlit and powered by Claude 3 Sonnet via AWS Bedrock. The chatbot answers questions based on user-provided context (e.g., a few sentences or a paragraph).

Features
Clean chat interface using Streamlit's st.chat_message

Custom context input via a text area

Claude 3 responses scoped to only the provided context

Easy integration with AWS Bedrock and Boto3

Stateless architecture for simplicity and transparency

Technologies Used
Streamlit for the UI

LangChain for Claude 3 invocation

AWS Bedrock for LLM access

Boto3 for AWS interaction

Installation
Clone the repository and install dependencies:

bash
Copy
Edit
git clone https://github.com/your-username/claude3-chatbot.git
cd claude3-chatbot
pip install -r requirements.txt
If requirements.txt does not exist, install manually:

bash
Copy
Edit
pip install streamlit boto3 langchain langchain-community
AWS Credentials
Ensure you have AWS credentials with the following permissions:

bedrock:InvokeModel

bedrock:ListFoundationModels

Credentials can be provided via environment variables:

bash
Copy
Edit
export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key
export AWS_REGION=us-east-1
Or use an AWS profile:

python
Copy
Edit
boto3.Session(profile_name="your-profile")
Usage
Run the Streamlit app using the CLI:

bash
Copy
Edit
streamlit run main.py
This launches a local web interface. You can input custom context and ask questions related to it. The chatbot only uses the context you provide; it does not have internet access or access to any other external information.

How It Works
The user provides a short block of context (e.g., "Paris is the capital of France. It is famous for the Eiffel Tower.")

The user then submits a natural language question

The application constructs a prompt that includes both the context and the question

Claude 3 via AWS Bedrock generates a response based solely on the input context

Example
Context:

csharp
Copy
Edit
Paris is the capital of France. It is famous for the Eiffel Tower.
Question:

csharp
Copy
Edit
What is Paris famous for?
Response:

csharp
Copy
Edit
Paris is famous for the Eiffel Tower.
Limitations
No internet access

No dynamic knowledge retrieval or search

Not integrated with file upload or document chunking

Context must be manually input each time

Future Improvements
Add file upload and automatic document parsing

Integrate a vector database for long-form contextual retrieval

Support follow-up questions with conversation memory

Enable streaming responses for a more natural feel

License
This project is licensed under the MIT License.

