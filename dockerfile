FROM python:3.9

WORKDIR /app

COPY ml_model /app/ml_model
COPY .env /app/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "ml_model/dashboard.py"]
