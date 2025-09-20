import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -- load data 
@st.cache_data
def load_data():
    drive_file_id = "1Ytsa7wjhIRvFNn2LTTT0J5Qmf5p467Ku"
    drive_url = f"https://drive.google.com/uc?id={drive_file_id}"

    local_paths = [
        "data/cord_cleaned_sample.csv",      # if running from repo root
        "../data/cord_cleaned_sample.csv",   # if running from notebooks/
    ]

    if os.environ.get("STREAMLIT_RUNTIME") == "true":
        # Running on Streamlit Cloud → use Google Drive
        df = pd.read_csv(drive_url)
    else:
        # Running locally → check both possible paths
        for path in local_paths:
            if os.path.exists(path):
                df = pd.read_csv(path)
                break
        else:
            st.error("Local file not found in data/ or ../data/.")
            st.stop()

    # -- Convert publish_time column to datetime
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

    # -- Extract year from publish_time
    df['year'] = df['publish_time'].dt.year

    # -- Abstract length (characters)
    df['abstract_word_count'] = df['abstract'].astype(str).apply(len)

    return df

# -- load the dataset once
df = load_data()

# -- app layout 
st.title("CORD-19 Data Explorer")
st.markdown("""
This Streamlit app provides an interactive exploration of the **CORD-19 metadata** dataset.  
You can filter by publication year, explore publication trends, journals, and word usage.
""")

# -- sidebar filters
st.sidebar.header("Filters")

# -- year range filter
year_min = int(df['year'].min())
year_max = int(df['year'].max())

year_range = st.sidebar.slider(
    "Select year range",
    min_value=year_min,
    max_value=year_max,
    value=(2012, 2021)
)

# -- filter dataframe based on year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -- Show Sample Data 
st.subheader("Sample of the Dataset")
st.dataframe(filtered_df.head(10))

# --- Visualization 1: Publications Over Time ---
st.subheader("Publications Over Time")
pubs_by_year = filtered_df['year'].value_counts().sort_index()

# -- Plot line chart of publications by year
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x=pubs_by_year.index, y=pubs_by_year.values, marker="o", ax=ax)
ax.set_title("Number of Publications Over the Years")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
st.pyplot(fig)

# --- Visualization 2: Top Journals ---
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = filtered_df['journal'].value_counts().head(10)

# -- Plot bar chart of top 10 journals
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, hue=top_journals.index, palette='viridis', legend=False, ax=ax)
ax.set_title("Top 10 Journals Publishing COVID-19 Research")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Visualization 3: Word Cloud of Titles ---
st.subheader("Word Cloud of Paper Titles")
all_titles = " ".join(filtered_df['title'].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)


fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.set_title("Word Cloud of COVID-19 Paper Titles", color='black', fontsize=16)
ax.axis("off")
st.pyplot(fig)

# --- Visualization 4: Source Distribution ---
st.subheader("Distribution of Sources")
fig, ax = plt.subplots(figsize=(12, 6))
filtered_df['source_x'].value_counts().plot(kind="bar", ax=ax)
ax.set_title("Distribution of Paper Counts by Source")
ax.set_xlabel("Source")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# --- Visualization 5: Abstract Word Count Distribution ---
st.subheader("Distribution of Abstract Word Counts")

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(filtered_df['abstract_word_count'], bins=50, kde=True, color="skyblue", ax=ax)
ax.set_title("Distribution of Abstract Word Counts")
ax.set_xlabel("Word Count")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)
