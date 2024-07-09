import subprocess
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Home page for Slick Scraper</p>"

@app.route("/recentdeals")
def recentDeals():
    scraped_content = open('output/recent-deals.html')
    return render_template("display.html", scraped_content=scraped_content)

@app.route("/recentdeals/refresh")
def refresh():
    subprocess.run(['scrapy', 'crawl', 'recentdeals'])

    with open('output/recent-deals.html', 'r') as f:
        data = f.read()
    return data
