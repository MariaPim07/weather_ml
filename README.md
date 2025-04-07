
# WEATHER_ML

Project created with the purpose of forecasting the temperature for the next 5 years in the city of São Paulo.

---

## Project Structure

- **airflow/**: Contains DAG scripts orchestrated by Airflow.
- **database/**: Table creation scripts and data backups.
- **ml_model/**: Machine learning prediction scripts and Streamlit dashboard.
- **requirements.txt**: Project dependencies

---

## Dependencies

### Python and libraries

The required libraries are listed in requirements.txt:

- `pandas`
- `scikit-learn`
- `seaborn`
- `streamlit`
- `sqlalchemy`
- `psycopg2-binary`
- `apache-airflow`

To install manually:

```bash
pip install -r requirements.txt
```

### Docker

Docker and Docker Compose must be installed (links below):

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Usage (Local)

1. Clone the repository:

```bash
git clone https://github.com/MariaPim07/weather_ml
```

2. Start the containers with Docker Compose:

```bash
docker-compose up --build
```

3. Restore the data available in database/backup into the Weather database (tables raw_data and processed_data).

4. The Airflow webserver will be available at:

```
http://localhost:8080
```

- Default user: `airflow`
- Default password: `airflow`

---

5. The dashboard will be available at:

```
http://localhost:8501
```

To manually start the dashboard:

```bash
cd ../dashboard
streamlit run app.py
```
