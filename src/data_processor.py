import pandas as pd
import numpy as np

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data from {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{file_path}'.")
    except Exception as e:
        print(f"Error loading data: {e}")
    return None

def get_weather_data(df, month, year):
    if df is None:
        return None, None
    try:
        df['Month'] = df['Month'].astype(int)
        filtered = df[(df['Month'] == int(month)) & (df['Year'] == int(year))]
        if filtered.empty:
            return None, None
        temp = filtered['tem'].mean()
        rain = filtered['rain'].mean()
        if np.isnan(temp) or np.isnan(rain):
            return None, None
        return temp, rain
    except Exception as e:
        print(f"Error processing weather data: {e}")
        return None, None

def get_available_years(df):
    if df is None or 'Year' not in df.columns:
        return None, None
    try:
        return df['Year'].min(), df['Year'].max()
    except Exception as e:
        print(f"Error getting available years: {e}")
        return None, None
