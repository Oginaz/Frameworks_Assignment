## 1. Objective
The goal of this project was to **explore the CORD-19 dataset (`metadata.csv`)**, clean and prepare it for analysis, generate insights about COVID-19 research publications, and build an **interactive Streamlit application** for visualization.

## 2. Data
- **Dataset**: CORD-19 Metadata (`metadata.csv`)  
- **Size**: ~ several hundred thousand records  
- **Key columns used**:  
  - `title` (paper title)  
  - `abstract` (paper abstract)  
  - `publish_time` (date of publication)  
  - `journal` (journal name)  
  - `source_x` (source of metadata)  

## 3. Data Cleaning
- Converted `publish_time` into `datetime`.  
- Extracted `year` from publication date for time-series analysis.  
- Created a new column `abstract_word_count` to measure abstract length.  
- Handled missing values by filling titles/abstracts with empty strings and dropping unused columns.  
- Saved cleaned dataset as `cord_cleaned.csv`.

## 4. Analysis and Visualizations
- **Publications by Year**: Sharp increase during 2020–2021 due to COVID-19 pandemic.  
- **Top Journals**: A small number of journals contributed a large share of COVID-19 papers.  
- **Word Cloud**: Frequent title words included *covid, coronavirus, pandemic, sars-cov-2*.  
- **Source Distribution**: Multiple sources (e.g., PubMed, PMC, WHO) contributed metadata.  
- **Abstract Lengths**: Most abstracts ranged between 1,500–3,000 characters.  

## 5. Streamlit Application
- Built an **interactive app** with filters for year range.  
- Displayed:
  - Sample data preview  
  - Line chart of publications over time  
  - Bar chart of top journals  
  - Word cloud of paper titles  
  - Source distribution  
  - Abstract length distribution  

## 6. Challenges
- **Large dataset**: Initial CSV was too big to handle; needed sampling and caching.  
- **Missing data**: Some rows lacked publication dates or abstracts.  
- **Date parsing**: Inconsistent formats required careful parsing with `errors="coerce"`.  

## 7. Learning Outcomes
- Strengthened skills in **pandas** for cleaning and analysis.  
- Practiced **matplotlib, seaborn, wordcloud** for visualization.  
- Learned to build a functional **Streamlit app** with interactive filters.  
- Improved workflow in documenting and commenting code.

## 8. Next Steps
- Extend analysis to include **author networks and citations**.  
- Apply **NLP techniques** (topic modeling, sentiment analysis) on abstracts.  
- Optimize Streamlit app with **plotly** for richer interactivity.  
