from flask import Flask, render_template

app = Flask(__name__)

# Route to serve the main donation page
@app.route("/")
def home():
    return render_template("index.html")  # The HTML file is saved as 'templates/index.html'

# Route for the "Donate Now" button
@app.route("/donate")
def donate():
    return "<h1>Thank you for considering a donation!</h1><p>You can donate through our secure payment gateway. More details coming soon!</p>"

# Route for the "Support Veterans" button
@app.route("/learn")
def learn():
    return "<h1>Learn More</h1><p>Here, you can find resources and articles about the ongoing efforts in Ukraine.</p>"

# Route for the "Learn More" button
@app.route("/volunteer")
def volunteer():
    return "<h1>Volunteer Opportunities</h1><p>We welcome your support! Sign up to volunteer and help the cause.</p>"

if __name__ == "__main__":
    app.run(debug=True)
