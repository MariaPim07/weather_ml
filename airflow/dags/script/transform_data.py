import os
import pandas as pd
from dotenv import main
from sqlalchemy import create_engine

main.load_dotenv()
engine = create_engine(f'{str(os.environ.get("DB_CONN"))}/weather')

def __get_data():
    try:
        return pd.read_sql_query('select * from raw_data where processed = false', con=engine)
    except Exception as err:
        print(err)

def __update_data(df):
    try:
        df['processed'] = True

        df.to_sql('raw_data', engine, index=True, if_exists='replace')
    except Exception as err:
        print(err)

def transform_load_data():
    try:
        df = __get_data()

        if df.empty == False:
            processed_df = pd.DataFrame()

            processed_df['year'] = pd.to_numeric(df['year'])
            processed_df['month'] = pd.to_numeric(df['month'])
            processed_df['day'] = pd.to_numeric(df['day'])
            processed_df['season'] = df['month'].apply(lambda x: '1' if x in [12, 1, 2] else #summer
                                                            '2' if x in [3, 4, 5] else #fall
                                                            '3' if x in [6, 7, 8] else #winter
                                                            '4') #spring
            processed_df['temperature_avg_f'] = pd.to_numeric(df['temperature_avg_f'])
            processed_df['humidity_percent'] = pd.to_numeric(df['humidity_percent'])
            processed_df['wind_speed_avg_mph'] = pd.to_numeric(df['wind_speed_avg_mph'])

            processed_df = processed_df.bfill()

            processed_df.to_sql('processed_data', engine, index=False, if_exists='append')

            __update_data(df)
    except Exception as err:
        print(err)