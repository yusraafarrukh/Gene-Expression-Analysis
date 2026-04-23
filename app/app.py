import streamlit as st
import pandas as pd
import numpy as np
import joblib
from K_Mean import run_kmeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

st.title("K-Means Clustering App")

# Upload CSV
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.write("### Preview of Dataset")
    st.dataframe(data.head())

    # Select numeric columns
    numeric_cols = [
        "num_reactions", "num_comments", "num_shares",
        "num_likes", "num_loves", "num_wows",
        "num_hahas", "num_sads", "num_angrys"
    ]
    data_numeric = data[numeric_cols].dropna()

    # Scale
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_numeric)

    # Elbow Method
    st.write("### Elbow Method")
    k_values = range(2, 11)
    inertias = []
    for k in k_values:
        _, _, inertia = run_kmeans(data_scaled, k=k)
        inertias.append(inertia)

    fig, ax = plt.subplots()
    ax.plot(k_values, inertias, marker='o')
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Inertia (WCSS)")
    ax.set_title("Elbow Method - Manual KMeans")
    st.pyplot(fig)

    # Choose k
    k = st.slider("Select number of clusters", 2, 10, 3)

    if st.button("Run KMeans"):
        centroids, labels, inertia = run_kmeans(data_scaled, k=k)
        st.success(f"KMeans completed with inertia: {inertia:.2f}")

        data["Cluster"] = labels
        st.write("### Clustered Data")
        st.dataframe(data.head())

        # Save model
        joblib.dump((centroids, labels), "kmeans_model.pkl")
        st.info("Model saved as kmeans_model.pkl")