import subprocess
from flask import Flask, render_template, jsonify
import json
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Home page for Slick Scraper</p>"

@app.route("/recentdeals")
def recentDeals():
    with open('output/recentdeals.json', encoding='utf-8') as f:
        scraped_content = json.load(f)
    return render_template("display.html", scraped_content=scraped_content)

@app.route("/recentdeals/refresh")
def refresh():
    subprocess.run(['scrapy', 'crawl', 'recentdeals'])

    with open('output/recentdeals.json', encoding='utf-8') as f:
        data = json.load(f)
    return data
