import pandas as pd
import streamlit as st 

tabela = pd.read_excel("tabela_vendas_100_dados.xlsx")
print(tabela)

# título 
st.title("Deashboard de Vendas")

# campo de seleção e filtro de dados 
regioes = st.multiselect("Selecione as regiões", tabela["Região"].unique()) 

if regioes:
    tabela = tabela[tabela["Região"].isin(regioes)]

# 2 métricas 
# faturamento total 
st.metric("Faturamento Total", f"R${tabela['Valor Venda'].sum()}")

# ticket médio 
st.metric("Ticket Médio", f"R${tabela['Valor Venda'].mean()}")

# gráfico Faturamento por região 
st.bar_chart(tabela.groupby("Região")['Valor Venda'].sum())

# gráfico Faturamento por Produto
st.bar_chart(tabela.groupby("Produto")['Valor Venda'].sum())