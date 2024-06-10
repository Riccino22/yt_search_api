from flask import Flask
import scraping

app = Flask("Api")

@app.route("/")
def home():
    return scraping.get_videos("What is LLM")

app.run(debug=True)