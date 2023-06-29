#import 
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from api.pinecone import pineconeRouter


import pinecone

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')


# Initialize Pinecone Connection
pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),  # find at app.pinecone.io
    environment=os.environ.get("PINECONE_ENVIRONMENT")  # next to api key in console
)

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(pineconeRouter,url_prefix='/api/pinecone')

@app.route("/")
def Home():
    return "This is the Homepage, This is the Homepage"

if __name__ == "__main__":
    app.run(threaded = True)
