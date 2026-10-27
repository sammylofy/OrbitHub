from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/contact')
def contact():
    return render_template('contact_us.html')

@app.route('/healthz')
def health_check():
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=False)