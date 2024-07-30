import pandas as pd
from sentiment_analysis import analyze_sentiment

def load_data(file_path):
    return pd.read_csv(file_path)

def process_data(df):
    df['sentiment'] = df['text'].apply(analyze_sentiment)
    return df

def main():
    data = load_data('data/sample_data.csv')
    processed_data = process_data(data)
    print(processed_data)

if __name__ == "__main__":
    main()
