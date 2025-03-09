import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Streamlit app
st.title("Analisis Data Penyewaan Sepeda")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load kedua dataset
def load_data(option):
    if option == "Data Harian (day.csv)":
        df = pd.read_csv(r"C:\Users\salsa\Documents\DICODING STUPEN\Dataset_BikeSharingData\day.csv")
    else:
        df = pd.read_csv(r"C:\Users\salsa\Documents\DICODING STUPEN\Dataset_BikeSharingData\hour.csv")
    return df

# Pilihan dataset
dataset_option = st.selectbox("Pilih Dataset:", ["Data Harian (day.csv)", "Data Per Jam (hour.csv)"])
df = load_data(dataset_option)

# Tampilkan dataset yang dipilih
st.subheader(f"Dataset: {dataset_option}")
st.write(df.head())

# **Analisis berdasarkan dataset yang dipilih**
if dataset_option == "Data Harian (day.csv)":
    st.subheader("Pengaruh Suhu terhadap Penyewaan (Data Harian)")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='temp', y='cnt', alpha=0.5, ax=ax)
    ax.set_xlabel("Temperatur")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

    st.subheader("Tren Penyewaan Sepeda Harian")
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='dteday', y='cnt', ax=ax)
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

else:
    st.subheader("Pengaruh Suhu terhadap Penyewaan (Data Per Jam)")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='temp', y='cnt', alpha=0.5, ax=ax)
    ax.set_xlabel("Temperatur")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

    st.subheader("Tren Penyewaan Sepeda Berdasarkan Jam")
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='hr', y='cnt', ax=ax)
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewaan")
    st.pyplot(fig)

# Explanatory Data Analysis (EDA)
st.subheader("Explanatory Data Analysis (EDA)")

# Statistik Deskriptif
st.write("### Statistik Deskriptif")
st.write(df.describe())

# Korelasi antar variabel (hanya kolom numerik)
st.write("### Korelasi Antar Variabel")
st.write(df.select_dtypes(include=['number']).corr())


# Visualisasi jumlah penyewaan berdasarkan suhu
st.subheader("Pengaruh Suhu terhadap Penyewaan")
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


# Visualisasi waktu paling sibuk
st.subheader("Waktu paling sibuk dan paling sepi dalam penyewaan sepeda berdasarkan jam, hari, dan musim")
hour_df = pd.read_csv(r"C:\Users\salsa\Documents\DICODING STUPEN\Dataset_BikeSharingData\hour.csv")
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=hour_df['hr'], y=hour_df['cnt'], ax=ax)
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Distribusi Penyewaan Sepeda Berdasarkan Hari
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Hari")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=hour_df['weekday'], y=hour_df['cnt'], ax=ax)
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Hari")
ax.set_xlabel("Hari (0 = Minggu, 6 = Sabtu)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Distribusi Penyewaan Sepeda Berdasarkan Musim
st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(12, 5))
sns.boxplot(x=hour_df['season'], y=hour_df['cnt'], ax=ax)
ax.set_title("Distribusi Penyewaan Sepeda Berdasarkan Musim")
ax.set_xlabel("Musim (1 = Semi, 2 = Panas, 3 = Gugur, 4 = Dingin)")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# Tren sepanjang waktu
st.subheader("Tren Jumlah Penyewaan dari Waktu ke Waktu")
fig, ax = plt.subplots(figsize=(15, 5)) 
sns.lineplot(data=hour_df, x='dteday', y='cnt', ax=ax, ci=None)  
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_title("Tren Penyewaan Sepeda dari Waktu ke Waktu")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)
