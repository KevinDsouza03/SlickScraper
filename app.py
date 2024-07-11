import subprocess
from flask import Flask, render_template, jsonify
import json
from slickdeals.slickdeals.spiders.scraper import recent_deals_result
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Home page for Slick Scraper</p>"

@app.route("/recentdeals")
def recentDeals():
    recent_deals_result()
    with open('output/recentdeals.json', encoding='utf-8') as f:
        scraped_content = json.load(f)
    return render_template("display.html", scraped_content=scraped_content)


