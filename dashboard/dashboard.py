import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Analisis Data Penyewaan Sepeda")
# Load kedua dataset
def load_data(option):
    if option == "Data Harian (day.csv)":
        df = pd.read_csv("bike_data/day.csv")
    else:
        df = pd.read_csv("bike_data/hour.csv")
    return df

# Pilihan dataset

df = load_data("bike_data/hour.csv")

# Konversi tanggal menjadi datetime
if 'dteday' in df.columns:
    df['dteday'] = pd.to_datetime(df['dteday'])

# Pilih rentang tanggal
if 'dteday' in df.columns:
    min_date, max_date = df['dteday'].min().date(), df['dteday'].max().date()
    start_date, end_date = st.slider("Pilih Rentang Tanggal:", 
                                     min_value=min_date, 
                                     max_value=max_date, 
                                     value=(min_date, max_date))
    df = df[(df['dteday'].dt.date >= start_date) & (df['dteday'].dt.date <= end_date)]
    
# Pilih musim
season_mapping = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
df['season_label'] = df['season'].map(season_mapping)
selected_season = st.multiselect("Pilih Musim:", df['season_label'].unique(), default=df['season_label'].unique())
df = df[df['season_label'].isin(selected_season)]

# Pilih cuaca
weathersit_mapping = {1: "Cerah", 2: "Berawan", 3: "Hujan", 4: "Salju"}
df['weathersit_label'] = df['weathersit'].map(weathersit_mapping)
selected_weathersit = st.multiselect("Pilih Cuaca:", df['weathersit_label'].unique(), default=df['weathersit_label'].unique())
df = df[df['weathersit_label'].isin(selected_weathersit)]

# Tampilkan dataset yang dipilih
st.header(f"Dataset: Bike Sharing")
st.write(df.head())

st.header("Pengaruh Suhu terhadap Penyewaan")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='temp', y='cnt', palette="coolwarm", alpha=0.5, ax=ax)
ax.set_xlabel("Temperatur")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

#Analisis histogram
st.header("Distribusi Variabel Kategorikal")
cat_cols = ["season", "weathersit", "workingday"]
for col in cat_cols:
    fig, ax = plt.subplots()
    sns.countplot(x=df[col], ax=ax)
    ax.set_title(f"Distribusi {col}")
    st.pyplot(fig)

# Explanatory Data Analysis (EDA)
st.header("Exploratory Data Analysis (EDA)")

# Statistik Deskriptif
st.write("### Statistik Deskriptif")
st.write(df.describe())

# Korelasi antar variabel (hanya kolom numerik)
st.write("### Korelasi Antar Variabel Numerik")
hour_df = pd.read_csv("bike_data/hour.csv")
numerical_columns = ["holiday", "weekday", "workingday", "weathersit", "temp", "atemp", "season", "windspeed", "cnt"]
correlation = hour_df[numerical_columns].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
ax.set_title("Heatmap Korelasi Antar Variabel Numerik")
st.pyplot(fig)

# Perbandingan Jumlah Penyewa dan Kecepatan Angin Berdasarkan Musim
st.write("### Perbandingan Jumlah Penyewa dan Kecepatan Angin Berdasarkan Musim")
season_labels = {1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"}
hour_df["season_label"] = hour_df["season"].map(season_labels)
season_grouped = hour_df.groupby("season_label")[["cnt", "windspeed"]].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x="season_label", y="cnt", data=season_grouped, color="skyblue", label="Jumlah Penyewa", ax=ax)
ax2 = ax.twinx()
sns.lineplot(x="season_label", y="windspeed", data=season_grouped, marker="o", color="red", label="Kecepatan Angin", ax=ax2)
ax.set_ylabel("Rata-rata Jumlah Penyewa Sepeda")
ax2.set_ylabel("Rata-rata Kecepatan Angin")
ax.set_xlabel("Musim")
ax.set_title("Perbandingan Jumlah Penyewa dan Kecepatan Angin Berdasarkan Musim")
ax.legend(loc="upper left")
st.pyplot(fig)

# Visualisasi jumlah penyewaan berdasarkan suhu
st.header("Pengaruh Suhu terhadap Penyewaan")
plt.figure(figsize=(12,6))
sns.scatterplot(x=df['temp'], y=df['cnt'], hue=df['weathersit'], palette="coolwarm")
plt.title("Hubungan Suhu dan Faktor Cuaca terhadap Jumlah Penyewaan Sepeda")
plt.xlabel("Suhu")
plt.ylabel("Jumlah Penyewaan")
plt.legend(title="Faktor Cuaca")
plt.show()


# Visualisasi jumlah penyewaan berdasarkan musim
st.subheader("Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots()
sns.boxplot(data=df, x='season', y='cnt', ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.subheader("Analisis Pola Penyewaan Sepeda terhadap Suhu")
fig, ax = plt.subplots(figsize=(8,5))
sns.lineplot(x=hour_df['temp'], y=hour_df['cnt'], ax=ax)
ax.set_title("Pola Penyewaan Sepeda terhadap Suhu")
ax.set_xlabel("Temperature (temp)")
ax.set_ylabel("Jumlah Penyewaan (cnt)")
st.pyplot(fig)

weather_labels = {1: "Cerah", 2: "Berawan", 3: "Hujan", 4: "Salju"}
hour_df['weathersit_label'] = hour_df['weathersit'].map(weather_labels)
st.subheader("Analisis Pola Penyewaan Sepeda terhadap Suhu dan Cuaca")
fig, ax = plt.subplots(figsize=(12,6))
sns.scatterplot(
    x=hour_df['temp'],
    y=hour_df['cnt'],
    hue=hour_df['weathersit_label'],
    palette="coolwarm",
    ax=ax
)
ax.set_title("Hubungan Suhu dan Faktor Cuaca terhadap Jumlah Penyewaan Sepeda")
ax.set_xlabel("Suhu")
ax.set_ylabel("Jumlah Penyewaan")
ax.legend(title="Faktor Cuaca")
st.pyplot(fig)

# Visualisasi waktu paling sibuk
st.header("Waktu paling sibuk dan paling sepi dalam penyewaan sepeda berdasarkan jam, hari, dan musim")
hour_df = pd.read_csv("bike_data/hour.csv")
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=hour_df['hr'], y=hour_df['cnt'], ax=ax, palette="coolwarm")
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Distribusi Penyewaan Sepeda Berdasarkan Hari
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Hari")
day_df = pd.read_csv("bike_data/day.csv")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=day_df['weekday'], y=day_df['cnt'], ax=ax, palette="coolwarm")
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Hari")
ax.set_xlabel("Hari (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Distribusi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=hour_df['season'], y=hour_df['cnt'], ax=ax, palette="coolwarm")
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim (1 = Semi, 2 = Panas, 3 = Gugur, 4 = Dingin)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Analisis Lanjutan
st.header("Analisis Lanjutan")
def categorize_time(hour):
    if 6 <= hour <= 11:
        return "Pagi"
    elif 12 <= hour <= 15:
        return "Siang"
    elif 16 <= hour <= 19:
        return "Sore"
    else:
        return "Malam"

hour_df['time_category'] = hour_df['hr'].apply(categorize_time)
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Waktu Penggunaan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x=hour_df['time_category'], y=hour_df['cnt'], palette="coolwarm", ax=ax)
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Waktu Penggunaan")
ax.set_xlabel("Waktu Penggunaan")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)
