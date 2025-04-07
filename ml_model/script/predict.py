import pandas as pd
import joblib
import os
from sqlalchemy import create_engine
from dotenv import main

main.load_dotenv()
engine = create_engine(f'{str(os.environ.get("DB_CONN"))}/weather')

dir_path = os.path.dirname(__file__)

def __get_data():
    try:
        return pd.read_sql_query('select * from processed_data', con=engine)
    except Exception as err:
        print(err)

def __get_model():
    return joblib.load(f"{dir_path}/RandomForestRegressor_model.pkl")

def predict_temperature(years = []):
    model = __get_model()
    historical_df = __get_data()
    
    humidity_mean = historical_df['humidity_percent'].mean()
    wind_speed_mean = historical_df['wind_speed_avg_mph'].mean()

    future_data = []
    for year in years:
        for month in range(1, 13):
            years_of_month = pd.to_datetime(f'{year}-{month}-01').days_in_month
            for day in range(1, years_of_month + 1):
                future_data.append([year, month, day, (month - 1) // 3 + 1, humidity_mean, wind_speed_mean])

    future_data_df = pd.DataFrame(future_data, columns=['year', 'month', 'day', 'season', 'humidity_percent', 'wind_speed_avg_mph'])
    
    predict = model.predict(future_data_df)
    
    future_data_df['predicted_temperature'] = predict

    return future_data_df

if __name__ == "__main__":
    predict_temperature([2026])