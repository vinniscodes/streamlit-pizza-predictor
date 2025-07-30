import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x, y)

st.title("Prevendo Valor de Pizza")
st.divider()
diametro = st.number_input("Digite o tamanho do diametro da pizza: ")
if diametro: 
    resultado_predicao = modelo.predict([[diametro]])
    preco_previsto = resultado_predicao[0][0]
    preco_arredondado = round(preco_previsto, 2)
    st.write(f"O valor da pizza com diametro de {diametro: .2f}cm é de R${preco_previsto: .2f}.")
