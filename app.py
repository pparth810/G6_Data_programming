from flask import Flask, render_template
from pymongo import MongoClient
import pandas as pd

app = Flask(__name__)

# Replace with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017/')
db = client['Data_Programming']  # Replace with your database name
collection = db['Crime']

def get_data_from_mongodb():
    data = list(collection.find())
    df = pd.DataFrame(data)
    df.drop('_id', axis=1, inplace=True)
    return df

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/visualization')
def visualization():
    df = get_data_from_mongodb()
    data_records = df.to_dict(orient='records')
    return render_template('visualization.html', data=data_records)

@app.route('/about_us')
def about_us():
    return render_template('AboutUs.html')

if __name__ == '__main__':
    app.run(debug=True)
