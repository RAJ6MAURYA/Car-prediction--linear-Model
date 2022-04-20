from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)
car = pd.read_csv("Cleaned_Car.csv")


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_type=fuel_type)


if __name__ == "__main__":
    app.run(debug=True)
