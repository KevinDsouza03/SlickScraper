import subprocess
from flask import Flask,jsonify
import json
import logging
from slickdeals.slickdeals.spiders.recentdeals import recent_deals_result
from slickdeals.slickdeals.spiders.primeday import prime_day_result
from slickdeals.slickdeals.spiders.techdeals import tech_deals_result
app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Home page for Slick Scraper</p>"

@app.route("/recentdeals")
def recentDeals():
    try:
        recent_deals_result()
        return open('output/recentdeals.json', encoding='utf-8')
        # with open('output/recentdeals.json', encoding='utf-8') as f:
        #     scraped_content = json.load(f)
        # return render_template("display.html", scraped_content=scraped_content)
    except Exception as e:
        logging.error(f"Error loading scraped content: {e}")
        return jsonify({"error":"Failed to load scraped content"}), 500


@app.route("/primeday")
def primeDay():
    try:
        prime_day_result()
        return open('output/primeday.json', encoding='utf-8')
        # with open('output/recentdeals.json', encoding='utf-8') as f:
        #     scraped_content = json.load(f)
        # return render_template("display.html", scraped_content=scraped_content)
    except Exception as e:
        logging.error(f"Error loading scraped content: {e}")
        return jsonify({"error":"Failed to load scraped content"}), 500
    
@app.route("/techdeals")
def techdeals():
    try:
        prime_day_result()
        return open('output/techdeals.json', encoding='utf-8')
        # with open('output/recentdeals.json', encoding='utf-8') as f:
        #     scraped_content = json.load(f)
        # return render_template("display.html", scraped_content=scraped_content)
    except Exception as e:
        logging.error(f"Error loading scraped content: {e}")
        return jsonify({"error":"Failed to load scraped content"}), 500
