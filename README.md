# K-Means Clustering App

An interactive web application built with **Streamlit** that performs K-Means clustering from scratch on Facebook Live dataset — without using sklearn's KMeans implementation.

---

## Project Structure

```
_K-Means/
├── app/
│   ├── app.py          # Streamlit web application
│   └── K_Mean.py       # Manual K-Means implementation using NumPy
├── dataset/
│   └── Live.csv        # Facebook Live posts dataset
├── model/              # Auto-created when app is run
│   ├── kmeans_model.pkl
│   └── scaler.pkl
├── notebook/
│   └── Model_Training_KMeans.ipynb  # Jupyter notebook for training & EDA
```

## Features

- Upload any compatible CSV file directly in the browser
- Visualizes the **Elbow Method** to help choose the optimal number of clusters
- Interactive slider to select number of clusters (k)
- Displays clustered data in a table
- Automatically saves the trained model and scaler to the `model/` folder

---

## How K-Means Works (Custom Implementation)

The algorithm in `K_Mean.py` is built purely with NumPy and follows these steps:

1. Randomly initialize `k` centroids from the data points
2. Compute Euclidean distances from each point to every centroid
3. Assign each point to the nearest centroid
4. Recompute centroids as the mean of assigned points
5. Repeat until centroids converge (no significant change)
6. Compute inertia (sum of squared distances) as the performance metric

---

## Dataset

The dataset used is the **Facebook Live Sellers in Thailand** dataset containing engagement metrics for Facebook posts.

**Key columns used for clustering:**

| Column | Description |
|---|---|
| `num_reactions` | Total reactions on the post |
| `num_comments` | Number of comments |
| `num_shares` | Number of shares |
| `num_likes` | Number of likes |
| `num_loves` | Number of love reactions |
| `num_wows` | Number of wow reactions |
| `num_hahas` | Number of haha reactions |
| `num_sads` | Number of sad reactions |
| `num_angrys` | Number of angry reactions |

---

## Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Install dependencies**
```bash
pip install streamlit pandas numpy scikit-learn matplotlib joblib
```

**3. Run the Streamlit app**
```bash
streamlit run app/app.py
```

**4. Open the notebook (optional)**
```bash
cd notebook
jupyter notebook Model_Training_KMeans.ipynb
```

## Tech Stack

- **Python 3.11**
- **Streamlit** — web interface
- **NumPy** — custom K-Means implementation
- **Pandas** — data handling
- **Scikit-learn** — StandardScaler only
- **Matplotlib** — Elbow Method plot
- **Joblib** — model serialization

---

## Notes
- The notebook (`Model_Training_KMeans.ipynb`) and the app both save models to the same `model/` folder
- sklearn's `KMeans` is **not used** — the clustering logic is fully custom
