# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FWFkOxbzfuKV2UD91VPG31_xnJ-Uxurb
"""

!pip install -q streamlit

!kaggle datasets download -d lakshmi25npathi/bike-sharing-dataset

import zipfile
with zipfile.ZipFile("bike-sharing-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("bike_data")

!wget -q -O - ipv4.icanhazip.com

!streamlit run dashboard.py & npx localtunnel --port 8501

from google.colab import drive
drive.mount('/content/drive')

from google.colab import drive
drive.mount('/content/drive')

!pipreqs "/content/drive/MyDrive/Colab Notebooks/Streamlit" --scan-notebooks