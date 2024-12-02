import streamlit as st
import pandas as pd
import plotly.express as px

# Judul
st.title("Bike Sharing Data Visualization")

# Gathering Data
day_df = pd.read_csv(r"C:\Users\ACER\Submission\Bike Sharing\Data\day.csv")

# Rename Kolom
day_df = day_df.rename(columns={
    "weathersit": "weather",
    "yr": "year",
    "mnth": "month",
    "hum": "humidity",
    "cnt": "count"
})

# Drop kolom yg tidak dipakai
day_df = day_df.drop(columns=['dteday', 'instant', 'year'])

# ubah kolom menjadi kategori
cols = ['season', 'month', 'holiday', 'weekday', 'workingday', 'weather']
for col in cols:
    day_df[col] = day_df[col].astype('category')

# ganti angka musim dengan nama musim
day_df['season'] = day_df['season'].map({
    1: "spring",
    2: "summer",
    3: "fall",
    4: "winter"
})

# ganti bulan angka dengan nama bulan
day_df["month"] = day_df["month"].map({
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember"
})

# Buat Filter di Sidebar
st.sidebar.header("Filter Data")
filter_choice = st.sidebar.radio("Choose the filter:", ("Bulan", "Musim"))

# Filter berdasarkan bulan atau musim
if filter_choice == "Bulan":
    selected_month = st.sidebar.selectbox("Select a Month", ["All"] + list(day_df["month"].unique()))
    filtered_df = day_df if selected_month == "All" else day_df[day_df["month"] == selected_month]
    labels = {"count": "Jumlah Pengguna", "month": "Bulan"}
    x_axis = "month"
    color = "month"  
else:
    selected_season = st.sidebar.selectbox("Select a Season", ["All"] + list(day_df["season"].unique()))
    filtered_df = day_df if selected_season == "All" else day_df[day_df["season"] == selected_season]
    labels = {"count": "Jumlah Pengguna", "season": "Musim"}
    x_axis = "season"
    color = "season" 

# Header filter
st.header(f"Jumlah Pengguna Sepeda Berdasarkan {filter_choice}")

# Visualisasi
fig = px.bar(
    filtered_df,
    x=x_axis,  # Dynamically selected x-axis
    y="count",
    color=color,  # Dynamically selected color (based on month or season)
    title=f"Jumlah Pengguna Sepeda Berdasarkan {filter_choice}",
    labels=labels,  # Dynamic labels
    barmode="group"
)

# Display the plot
st.plotly_chart(fig)

st.write(day_df.head())
