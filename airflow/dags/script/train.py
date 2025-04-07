import os
import pandas as pd
from dotenv import main
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error, root_mean_squared_error
from sqlalchemy import create_engine
import joblib

main.load_dotenv()
engine = create_engine(f'{str(os.environ.get("DB_CONN"))}/weather')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
MODEL_PATH = os.path.join(BASE_DIR, 'ml_model\\script', 'RandomForestRegressor_model.pkl')

def __get_data():
    try:
        return pd.read_sql_query('select * from processed_data', con=engine)
    except Exception as err:
        print(err)

def model_train():
    df = __get_data()

    X = df[['year', 'month', 'day', 'season', 'humidity_percent', 'wind_speed_avg_mph']]
    y = df['temperature_avg_f']

    # 80% train 20% test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=500, random_state=42, max_features="sqrt",
        min_samples_leaf=1, min_samples_split=2, max_depth=30)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    print(f'R2 Score: {r2}')

    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae}')

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    rmse = root_mean_squared_error(y_test, y_pred)
    print(f'Root Mean Squared Error: {rmse}')

    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)
        print('Old model removed')

    joblib.dump(model, MODEL_PATH)
