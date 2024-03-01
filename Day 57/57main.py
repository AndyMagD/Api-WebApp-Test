from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

def get_current_year():
    return datetime.datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", year=get_current_year())


@app.route('/<string:name>')
def get_gender(name):
    response_gender = requests.get(url=f"https://api.genderize.io?name={name}")
    if response_gender.status_code == 200:
        gender_data = response_gender.json()
        gender = gender_data.get('gender')
    response_age = requests.get(url=f"https://api.agify.io?name={name}")
    if response_age.status_code == 200:
        age_data = response_age.json()
        age = age_data.get('age')
    return render_template("index.html", name=name, gender=gender, age=age, year=get_current_year())


if __name__ == "__main__":
    app.run(debug=True)
