from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<hi>welcome to my personal website!</hi>
<h2>my name is martin kirimi</h2>
<p>i am a student at africa international university pursuing a degree in computer science .</p>
welcome to my portfolio website where you can find information about my projects, skills, and experiences. feel free to explore the different sections of the website to learn more about me and my work. thank you for visiting!</p>"""


if __name__ == "__main__":
    app.run(debug=True)
