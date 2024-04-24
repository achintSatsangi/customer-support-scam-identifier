from langchain_community.llms import GPT4All
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="""
    Answer TRUE or FALSE with explaination in JSON format. result : BOOLEAN, description: Explaination. Is this message a scam or phishing attempt: {text}
    """
)

# Initialize the GPT4All language model
llm = GPT4All(
    model="./models/mistral-7b-openorca.gguf2.Q4_0.gguf"
)

# Create a LLMChain to handle the prompt
chain = LLMChain(llm=llm, prompt=prompt_template)

while True:
    # Get user input for the prompt
    user_prompt = input("Enter your prompt (or 'quit' to exit): ")

    if user_prompt.lower() == "quit":
        break

    # Generate response using the prompt template
    response = chain.invoke(user_prompt)
    print(response["text"])
