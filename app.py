# This project is based on the work by Julia Nikulski: https://github.com/julianikulski/portfolio-website

from flask import Flask, render_template, request, redirect

# Configure application
app = Flask(__name__)

@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    greeting = 'Featured Projects'
    title_text = "Project management professional and aspiring quant. Graduate in Data Science and Electrical " \
                 "Engineering. Hobby programmer particularly interested in the intersection of code, data and finance."

    return render_template('/index.html',
                           greeting=greeting,
                           title_text=title_text,
                           title="CODE, DATA & FINANCE",
                           id="index")


@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():
    # get all projects from the database
    # zipped = helper.get_portfolio_content(lang)
    zipped = []

    # get the title content for the portfolio page
    # title_text = helper.get_title_content('portfolio', lang)
    title_text = "A compilation of personal and collaborative data science and machine learning projects. " \
                 "The collection includes apps, dashboards and visualizations as well as a number of works in " \
                 "classification, network analysis and natural language processing."

    return render_template('/portfolio.html',
                           title_text=title_text,
                           title="PROJECT PORTFOLIO",
                           id="portfolio",
                           projects=zipped)

@app.route('/about', methods=['POST', 'GET'])
def about():

    title_text = "I have used code from Computer Architecture to AI, in generating digital circuits, processing signals, " \
                 "deploying apps and building machine learning models. My eclectic profile combines a technical background" \
                 " in electrical engineering and data science with professional experience in construction management."
    skills = "skills"

    return render_template('/about.html',
                            title_text=title_text,
                            title="ABOUT",
                            id="about",
                           skills=skills)

# if __name__ == '__main__':
#     app.run()
