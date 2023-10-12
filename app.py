from flask import Flask,request
from PyPDF2 import PdfFileReader
from flask_cors import CORS
import PyPDF2
from flask import jsonify
import assemblyai as aai

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/pdf", methods=['POST'])
def read_pdf():
    pdf_content=request.files['pdf']
    

    pdf_reader = PyPDF2.PdfReader(pdf_content)
    print(pdf_reader)
        
    total_pages = len(pdf_reader.pages)
    
    for page_number in range(total_pages):
        page = pdf_reader.pages[page_number]
        page_content = page.extract_text()
        print(page_content)

    p=jsonify(page_content)
    return p


@app.route("/audio", methods=['POST'])
def read_audio():
    print("hii")

    aai.settings.api_key = "3074dae4f6b74249bc9026edcb61bf09"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")

    text = (transcript.text)

    return jsonify(text)
    


if __name__ == '__main__':
    CORS(app)
    CORS(app, origins='*')
    app.run()
