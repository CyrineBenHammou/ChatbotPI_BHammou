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

# Define a POST endpoint at the path "/analyse"
@app.post("/analyse")
def analyse_endpoint(analyse_input: AnalyseTextInput):

    print(analyse_input)
    #miniscule
    texte=(analyse_input.texte).lower()
    #ponctuation
    texte = ' '.join([char for char in texte if char not in string.punctuation])
    #texte.translate(str.maketrans("", "", string.punctuation))

    #erreur:Faute d'orthographe
    """blob = TextBlob(texte)
    texte = blob.correct()
    print(texte.words)
    print(type(texte.words))"""

    #tokenisation
    tokens=nltk.word_tokenize(texte)
    print(tokens)

    #stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    print(tokens)

    #Stemmer & Lemmatization
    
    #porter = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    #stemmed_words = [porter.stem(word) for word in tokens]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
    print(lemmatized_words)

    return {"msg": analyse_input}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

