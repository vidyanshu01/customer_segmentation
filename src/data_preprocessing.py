import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    # Drop missing or irrelevant columns
    data = data.dropna()
    
    # Select numeric columns
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    
    # Scale data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)
    
    return scaled_data, data
