#  Customer Segmentation using K-Means Clustering

This project identifies different customer groups based on purchasing behavior using **K-Means Clustering**. It helps businesses understand their customers and design better marketing strategies.

---

##  Project Overview
- Collected and preprocessed customer sales data.
- Applied **K-Means Clustering** to identify distinct customer groups.
- Visualized clusters using **Seaborn** and **Matplotlib**.
- Developed a simple **Flask Web App** to upload CSV and view segmented results.

---

## Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Framework:** Flask  
- **Deployment:** Render / Railway / Localhost  

---

##  Folder Structure
customer_segmentation/
│
├── data/
│ ├── Mall_Customers.csv
│
├── notebooks/
│ ├── EDA_and_Model.ipynb
│
├── src/
│ ├── data_preprocessing.py
│ ├── kmeans_model.py
│
├── app/
│ ├── templates/
│ │ ├── index.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore