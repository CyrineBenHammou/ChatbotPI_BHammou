from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
#from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
#import openai  

# Create a FastAPI instance
app = FastAPI()

app.mount("/frontend", StaticFiles(directory="../FRONTEND", html = True), name="frontend")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def analyse_text(texte:str):
    mot_cle=nltk.word_tokenize(texte)
    return {"sujet":"vide","sentiment":[],"mot_cles":mot_cle}

def generer_reponse(text:str):
    return {"reponse":"reponse"}

def formeter_reponse(text:str):
    return {"reponse_formater":"reponse vide formater"}


# Define a Pydantic model for the input data
class AnalyseTextInput(BaseModel):
    texte: str

@app.post("/query_openai")
def QueryOpenAI(query:str):
    
  #  openai.api_key = "#"
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a computer science university teacher"},
        {"role": "user", "content": query}
        ]   
    )   

    response= client['choices'][0]['message']['content']
    print(response)
    return response


@app.post("/analyse")
def analyse_endpoint(analyse_input: AnalyseTextInput):

    # Convert to lowercasewer()
    texte = analyse_input.texte.lower()

    # Tokenization
    tokens = nltk.word_tokenize(texte)

     # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    punctuation = set(string.punctuation)
    
    tokens = [word for word in tokens if word not in stop_words and word not in punctuation]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    print(lemmatized_words)

    # Add a space before the additional phrase
    query = " ".join(lemmatized_words) + " in context of computer science"

    response =QueryOpenAI(query)
    return {"msg": query}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

