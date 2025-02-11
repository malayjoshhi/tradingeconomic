from flask import Flask, render_template, request
import requests
import plotly.express as px
import pandas as pd

app = Flask(__name__)

API_KEY = '5339c2ac890f4ee:mlrfl0swavc26r4'
BASE_URL = 'https://api.tradingeconomics.com/markets/index'

def fetch_data(country, indicator):
    """Fetch data for a given country and indicator (mock function)."""
  
    data = {
        "Nigeria": {"GDP": [100, 110, 120, 130], "Inflation": [5, 6, 7, 8]},
        "Ghana": {"GDP": [80, 85, 90, 95], "Inflation": [4, 5, 6, 7]},
    }
    return data.get(country, {}).get(indicator, [])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():

    country1 = request.form.get('country1')
    country2 = request.form.get('country2')
    indicator = request.form.get('indicator')


    data1 = fetch_data(country1, indicator)
    data2 = fetch_data(country2, indicator)


    table_data = {
        'Year': [2020, 2021, 2022, 2023],
        country1: data1,
        country2: data2,
    }
    df = pd.DataFrame(table_data)


    fig = px.line(df, x='Year', y=[country1, country2], title=f'{indicator} Comparison')
    chart = fig.to_html(full_html=False)

    return render_template('compare.html', table=df.to_html(index=False), chart=chart)

if __name__ == '__main__':
    app.run(debug=True)