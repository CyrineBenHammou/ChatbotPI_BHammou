from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import nltk

# Create a FastAPI instance
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyse_text(text:str):
    return {"sujet":"vide","sentiment":[],"mot_clés":[]}

def generer_reponse(text:str):
    return {"reponse":"reponse"}

def formeter_reponse(text:str):
    return {"reponse_formater":"reponse vide formater"}

# Define a Pydantic model for the input data
class AnalyseTextInput(BaseModel):
    text: str

# Define a POST endpoint at the path "/analyse"
@app.post("/analyse")
def analyse_endpoint(analyse_input: AnalyseTextInput):
    # This function receives data from the client, validates it using Pydantic, and processes it
    print(analyse_input)
    return {"msg":analyse_input}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)