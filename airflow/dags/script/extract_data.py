import time
import pandas as pd
import os
from dotenv import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine
from datetime import datetime

main.load_dotenv()
engine = create_engine(f'{str(os.environ.get("DB_CONN"))}/weather')

def __get_data():
    year = datetime.now().year
    month = datetime.now().month-1 if datetime.now().month > 1 else 12

    df = pd.DataFrame()

    url = f"{str(os.environ.get("URL"))}{year}-{month}"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options)
    driver.get(url)

    rows = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.XPATH, '//table[@class="days ng-star-inserted"]//tbody')))

    for row in rows:
        day = row.find_element(By.XPATH, './/td[position()=1]').text.split()
        wind_speed_avg_mph = [t.text for t in (row.find_element(By.XPATH, './/td[position()=5]')
            .find_elements(By.XPATH, './/tr//td[position()=2]'))]
        temperature_avg_f = [t.text for t in row.find_element(By.XPATH, './/td[position()=2]')
            .find_elements(By.XPATH, './/tr//td[2]')]
        humidity_percent = [t.text for t in row.find_element(By.XPATH, './/td[position()=4]')
            .find_elements(By.XPATH, './/tr//td[2]')]

        df = df._append({
            "year": year,
            "month": month,
            "day": day[1:],
            "temperature_avg_f": temperature_avg_f[1:],
            "humidity_percent": humidity_percent[1:],
            "wind_speed_avg_mph": wind_speed_avg_mph[1:],
            "processed": False
        }, ignore_index=True)

        df = df.explode(["day", "temperature_avg_f", "humidity_percent", "wind_speed_avg_mph"])

    driver.quit()

    return df

def extract_data():
    df = __get_data()

    df.to_sql('raw_data', engine, if_exists='append', index=False)
