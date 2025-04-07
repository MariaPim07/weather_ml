import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from script.predict import predict_temperature

def build_dashboard(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='year', y='predicted_temperature', data=df, marker='o', color='b')
    plt.title("Previsão de Temperatura Média por Ano")
    plt.xlabel("Ano")
    plt.ylabel("Temperatura Média (°F)")
    plt.grid(True)
    st.pyplot()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='month', y='predicted_temperature', data=df, palette='coolwarm')
    plt.title("Temperatura Média por Mês")
    plt.xlabel("Mês")
    plt.ylabel("Temperatura Média (°F)")
    plt.grid(True)
    st.pyplot()

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='season', y='predicted_temperature', data=df, palette='Set2')
    plt.title("Temperatura Média por Estação do Ano")
    plt.xlabel("Estação")
    plt.ylabel("Temperatura Média (°F)")
    plt.grid(True)
    st.pyplot()

def run_dashboard():
    st.title("Previsão de Temperatura Média da Cidade de São Paulo para os Próximos 5 Anos")

    years = list(range(2025, 2031))
    predicted_temperature = predict_temperature(years)

    st.subheader("Tabela de Previsões de Temperatura Média")
    st.write(predicted_temperature)

    # Gerar visualizações
    build_dashboard(predicted_temperature)

if __name__ == "__main__":
    run_dashboard()