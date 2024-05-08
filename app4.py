import requests
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import squarify

# Function to load data, with download support
@st.cache_data
def load_data():
    # Path to save the downloaded file
    dataset_path = "2019-Nov.csv"
    # Google Drive download URL with your file ID
    download_url = "https://drive.google.com/uc?export=download&id=1IYV7FA4p_-0JPGxyDFneiIn336HvBPTy"

    # Check if the file is present locally
    try:
        with open(dataset_path, "r"):
            pass
    except FileNotFoundError:
        st.info("Downloading the dataset from Google Drive...")
        # Download the file
        response = requests.get(download_url)
        response.raise_for_status()  # Ensure the request succeeded

        # Write the downloaded content to a local file
        with open(dataset_path, "wb") as f:
            f.write(response.content)
        st.success("Dataset downloaded successfully!")
        
    # List the columns that should be used
    available_columns = pd.read_csv(dataset_path, nrows=0).columns.tolist()
    required_columns = ["event_time", "category_code", "price", "user_id"]
    
    # Only use columns that exist in the dataset
    usecols = [col for col in required_columns if col in available_columns]

    # Read the CSV file into a DataFrame
    df = pd.read_csv(dataset_path, usecols=["event_time", "category_code", "price", "user_id"])
    df['event_time'] = pd.to_datetime(df['event_time'])
    df['total_price'] = df['price']
    return df

# Function to aggregate customer data
@st.cache_data
def aggregate_customer_data(df):
    user_id_spend = df.groupby('user_id').agg(
        total_price=('price', 'sum'),
        frequency=('event_time', 'count')
    ).reset_index()
    return user_id_spend

# Function to apply KMeans clustering
@st.cache_resource
def apply_kmeans_clustering(data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    data['cluster'] = kmeans.fit_predict(data[['total_price', 'frequency']])
    return data

# Load data
df = load_data()
user_id_spend = aggregate_customer_data(df)

# Streamlit layout and main title
st.markdown("<h1 style='text-align: center;'>E-Commerce Customer Analysis</h1>", unsafe_allow_html=True)

# Visualization 1: Static Tree Map Title
st.markdown("<h3 style='text-align: center;'>Static Customer Segmentation Tree Map</h3>", unsafe_allow_html=True)

# Visualization 1: Static Tree Map (Matplotlib + Squarify)
fig, ax = plt.subplots(figsize=(10, 7))
squarify.plot(sizes=user_id_spend['total_price'][:20], label=user_id_spend['user_id'][:20], alpha=0.8, ax=ax)
ax.axis('off')
ax.set_title('Customer Segmentation Tree Map (Static)', fontsize=16)
st.pyplot(fig)

# Apply clustering with the updated data
num_clusters = st.slider('Select Number of Clusters', 2, 10, value=4)
user_id_spend = apply_kmeans_clustering(user_id_spend, num_clusters)

# Visualization 2: Interactive Tree Map Title
st.markdown("<h3 style='text-align: center;'>Interactive Customer Segmentation Tree Map with Clustering</h3>", unsafe_allow_html=True)

# Visualization 2: Interactive Tree Map
fig1 = px.treemap(
    user_id_spend.head(20),
    path=[px.Constant('all'), 'cluster', 'user_id'],
    values='total_price',
    color='cluster',
    color_continuous_scale='Viridis',
    title='Customer Segmentation Tree Map with Clustering (Top 20 Customers)'
)
fig1.update_traces(
    textinfo='label+value+percent entry',
    hovertemplate='<b>User ID:</b> %{label}<br><b>Total Price:</b> %{value}<br><b>Cluster:</b> %{color}<br>'
)
fig1.update_layout(margin=dict(l=10, r=10, t=40, b=10))
st.plotly_chart(fig1)

# Visualization 3: Predictive Lifetime Value Scatter Plot Title
st.markdown("<h3 style='text-align: center;'>Predictive Lifetime Value (LTV) Scatter Plot</h3>", unsafe_allow_html=True)

# Visualization 3: Predictive Lifetime Value Scatter Plot
df_ltv = df.groupby('user_id').agg(
    frequency=('event_time', 'count'),
    monetary_value=('price', 'sum')
).reset_index()
freq_min, freq_max = st.slider('Filter Purchase Frequency', 1, int(df_ltv['frequency'].max()), (1, 100))
monetary_min, monetary_max = st.slider('Filter Monetary Value', 1, int(df_ltv['monetary_value'].max()), (1, 10000))
marker_opacity = st.slider('Adjust Marker Transparency', 0.1, 1.0, 0.7)

filtered_df = df_ltv[
    (df_ltv['frequency'] >= freq_min) & (df_ltv['frequency'] <= freq_max) &
    (df_ltv['monetary_value'] >= monetary_min) & (df_ltv['monetary_value'] <= monetary_max)
]

fig2 = px.scatter(
    filtered_df,
    x='frequency',
    y='monetary_value',
    log_x=True,
    log_y=True,
    opacity=marker_opacity,
    title='Predictive Lifetime Value (LTV) Scatter Plot (Log Scales)',
    labels={'frequency': 'Purchase Frequency', 'monetary_value': 'Monetary Value'}
)
st.plotly_chart(fig2)

# Visualization 4: Total Sales by Product Category Bar Chart Title
st.markdown("<h3 style='text-align: center;'>Top Product Categories by Sales</h3>", unsafe_allow_html=True)

# Visualization 4: Total Sales by Product Category Bar Chart
agg_sales = df.groupby('category_code')['price'].sum().reset_index()
top_n = st.slider('Select Top N Product Categories', 5, 50, value=20)
top_n_df = agg_sales.sort_values('price', ascending=False).head(top_n)

fig3 = px.bar(
    top_n_df,
    x='category_code',
    y='price',
    color='category_code',
    title=f'Top {top_n} Product Categories by Sales',
    labels={'category_code': 'Category Code', 'price': 'Total Sales'},
    text='price',
    log_y=True
)
fig3.update_layout(
    xaxis_tickangle=-45,
    coloraxis_colorbar=dict(title='Category')
)
st.plotly_chart(fig3)
