from flask import Flask, request, render_template
from src.data_preprocessing import load_and_preprocess_data
from src.kmeans_model import train_kmeans
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    file_path = "uploaded.csv"
    file.save(file_path)

    data_scaled, raw_data = load_and_preprocess_data(file_path)
    model, clusters = train_kmeans(data_scaled)
    raw_data['Cluster'] = clusters
    raw_data.to_csv("clustered_output.csv", index=False)

    return "✅ Segmentation complete! Download the clustered_output.csv file."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

