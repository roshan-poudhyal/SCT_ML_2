# 📊 SCT_ML_2: Customer Segmentation using K-Means Clustering

This project performs customer segmentation using the K-Means clustering algorithm on the **Mall Customer Dataset**. It identifies distinct customer groups based on features like annual income and spending score.

---

## 📁 Project Structure

```
├── Mall_Customers.csv         # Dataset
├── main.py                    # Main script for data loading, training, and plotting
├── scaler.pkl                 # Saved StandardScaler for consistent preprocessing
├── kmeans_model.pkl           # Trained KMeans model
├── Untitled.ipynb             # Jupyter notebook with exploration and visualizations
└── model/                     # Optional folder for saved models/artifacts
```

---

## ⚙️ Features

- Data preprocessing with StandardScaler  
- Elbow Method to determine optimal number of clusters  
- KMeans clustering implementation  
- Customer segmentation visualization using matplotlib  
- Model & Scaler persistence using `joblib`

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

---

## 🚀 Run the Project

To train and visualize:

```bash
python main.py
```

---

## 📈 Output

- Scatter plot of customers grouped into clusters  
- Centroids of each cluster  
- Saved model and scaler for reuse

---

## 🧠 ML Algorithm Used

- **KMeans Clustering** from `sklearn.cluster`

---

## 📊 Dataset

- **Mall_Customers.csv**  
  - Features: `CustomerID`, `Gender`, `Age`, `Annual Income`, `Spending Score`  
  - Source: Public dataset for unsupervised learning

---

## 👨‍💻 Author

- [Roshan Poudhyal](https://github.com/roshan-poudhyal)

---

## 📝 License

This project is open-source and available under the MIT License.
