from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the landing home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about info page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact info page."""
    return render_template('contact.html')

if __name__ == '__main__':
    # Run application on local port 5000 with interactive debugger enabled
    app.run(debug=True, port=5000)