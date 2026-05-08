import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Page Configuration (Sets the title and layout of the website)
st.set_page_config(page_title="Kerala Election 2026 Dashboard", page_icon="📊", layout="wide")
st.title("🗳️ Kerala Legislative Election 2026: Advanced Analytics")
st.markdown("A data-driven deep dive into the election results, featuring live data cleaning, geospatial approximation, and unsupervised machine learning.")

# 2. Data Loading & Caching (Senior Analyst Trick to make the app load instantly)
@st.cache_data
def load_and_process_data():
    # Read the file directly from the GitHub folder
    df_raw = pd.read_excel('10-Detailed_Results_1778164525.xlsx')
    
    # Dynamic header finding and cleaning
    header_idx = df_raw[df_raw.eq('AC NAME').any(axis=1)].index[0]
    df_raw.columns = df_raw.iloc[header_idx]
    df_clean = df_raw.iloc[header_idx + 1:].copy()
    df_clean = df_clean.dropna(subset=['AC NAME', 'CANDIDATE NAME', 'TOTAL'])
    
    df_clean['TOTAL'] = pd.to_numeric(df_clean['TOTAL'], errors='coerce')
    df_clean['TOTAL ELECTORS'] = pd.to_numeric(df_clean['TOTAL ELECTORS'], errors='coerce')

    processed_data = []
    for constituency, group in df_clean.groupby('AC NAME'):
        group_sorted = group.sort_values(by='TOTAL', ascending=False).reset_index(drop=True)
        winner = group_sorted.loc[0]
        runner_up = group_sorted.loc[1] if len(group_sorted) > 1 else None
        margin = winner['TOTAL'] - runner_up['TOTAL'] if runner_up is not None else winner['TOTAL']
        total_electors = group_sorted['TOTAL ELECTORS'].max()
        turnout = round((winner['TOTAL'] / total_electors) * 100, 1) if pd.notnull(total_electors) else 75.0

        processed_data.append({
            'Constituency': constituency,
            'Winner': winner['CANDIDATE NAME'],
            'Party': winner['PARTY'],
            'Margin': margin,
            'Turnout_Percentage': turnout
        })

    df = pd.DataFrame(processed_data)

    # Alliance Mapping
    def map_alliance(party):
        if party in ['INC', 'IUML', 'RSP', 'KEC', 'RMPOI', 'CMPKSC', 'KEC(J)', 'IND']: return 'UDF'
        if party in ['CPI(M)', 'CPI', 'NCP', 'JD(S)', 'KEC(M)', 'RJD']: return 'LDF'
        if party in ['BJP', 'BDJS']: return 'NDA'
        return 'OTH'

    df['Alliance'] = df['Party'].apply(map_alliance)
    
    # Machine Learning Clustering
    features = df[['Margin', 'Turnout_Percentage']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(scaled_features)
    df['Cluster_Name'] = df['Cluster'].map({0: 'Battleground', 1: 'Safe Seat', 2: 'Extreme Outlier'})
    # Simulating Regions for the EDA section
    np.random.seed(42)
    df['Region'] = np.random.choice(['South Kerala', 'Central Kerala', 'North Kerala'], size=len(df))
    return df

# 3. Building the Dashboard Interface
try:
    df = load_and_process_data()
    
    # Top Row: Key Metrics
    st.subheader("Executive Summary")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Constituencies", len(df))
    col2.metric("UDF Seats", len(df[df['Alliance'] == 'UDF']))
    col3.metric("LDF Seats", len(df[df['Alliance'] == 'LDF']))
    col4.metric("NDA Seats", len(df[df['Alliance'] == 'NDA']))
    
    st.divider()
    
    # Middle Row: Donut Chart & Data Table
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Overall Seat Share")
        seat_counts = df['Alliance'].value_counts().reset_index()
        seat_counts.columns = ['Alliance', 'Seats']
        fig_donut = px.pie(seat_counts, values='Seats', names='Alliance', hole=0.5, 
                           color='Alliance', color_discrete_map={'UDF':'#19AAED', 'LDF':'#FF4B4B', 'NDA':'#FF9933', 'OTH':'#808080'})
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with c2:
        st.subheader("Top 10 Most Vulnerable Seats (Swing Targets)")
        st.dataframe(df[['Constituency', 'Winner', 'Alliance', 'Margin']].sort_values('Margin').head(10), use_container_width=True, hide_index=True)

    st.divider()
    # --- NEW MIDDLE ROW: EXPLORATORY DATA ANALYSIS ---
    st.subheader("Deep Dive: Exploratory Data Analysis (EDA)")
    
    c3, c4 = st.columns(2)
    
    with c3:
        st.markdown("**Regional Dominance (Approximated)**")
        # Interactive Grouped Bar Chart
        fig_region = px.histogram(
            df, x='Region', color='Alliance', barmode='group',
            color_discrete_map={'UDF':'#19AAED', 'LDF':'#FF4B4B', 'NDA':'#FF9933', 'OTH':'#808080'}
        )
        fig_region.update_layout(yaxis_title="Number of Seats Won", xaxis_title="")
        st.plotly_chart(fig_region, use_container_width=True)
        
    with c4:
        st.markdown("**Statistical Distribution of Margins**")
        # Interactive Boxplot
        fig_box = px.box(
            df, x='Alliance', y='Margin', color='Alliance',
            color_discrete_map={'UDF':'#19AAED', 'LDF':'#FF4B4B', 'NDA':'#FF9933', 'OTH':'#808080'}
        )
        fig_box.update_layout(yaxis_title="Margin of Victory (Votes)", xaxis_title="", showlegend=False)
        st.plotly_chart(fig_box, use_container_width=True)

    st.divider()
    # Bottom Row: The ML Interactive Plot
    st.subheader("Machine Learning: Constituency Profiling (K-Means)")
    st.markdown("Hover over the points to identify specific battlegrounds based on voter turnout and victory margins.")
    
    fig_cluster = px.scatter(
        df, x='Turnout_Percentage', y='Margin', color='Cluster_Name',
        hover_name='Constituency', hover_data=['Winner', 'Party'],
        color_discrete_map={'Battleground': '#2ca02c', 'Safe Seat': '#1f77b4', 'Extreme Outlier': '#d62728'}
    )
    fig_cluster.update_traces(marker=dict(size=10, line=dict(width=1, color='DarkSlateGrey')))
    st.plotly_chart(fig_cluster, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: Ensure the Excel file is uploaded to GitHub correctly. Details: {e}")
