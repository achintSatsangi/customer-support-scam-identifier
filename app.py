from fastapi import FastAPI
from fastapi.responses import JSONResponse
from langchain_community.llms import GPT4All
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from json import loads

app = FastAPI()

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["text"],
    template="""
    In an e-commerce app, inside chat conversation, detect a fraud message,
    Answer only in RAW JSON format, with likeliness of message being a scam with no new line characters having fields 
    scam: boolean, 
    likeliness: float, where 0 being not a scam and 1 being a scam,
    description: Explaination,
    For the following question: Is this message a scam or phishing attempt: {text}.
    """
)

# Initialize the GPT4All language model
llm = GPT4All(model="./models/mistral-7b-openorca.gguf2.Q4_0.gguf")

# Create a LLMChain to handle the prompt
chain = LLMChain(llm=llm, prompt=prompt_template)

@app.get("/customerServiceScam")
async def generate_response(text: str):
    response = chain.invoke(text)
    data = loads(response["text"])
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
