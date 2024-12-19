import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1- Importando os Dados
data = pd.read_csv("data/pedidos.csv")
df = pd.DataFrame(data)

#2- Função principal que será executada quando o programa for inciado (visual do navegador)
def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    
    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
    with aba1:
        display_dataframe(df)
    with aba2:
        display_charts(df)
    with aba3:
        display_metrics(df)

#3- Função para exibir o DataFrame
def display_dataframe(data):
    st.header("Visualização do DataFrame")
    st.sidebar.header("Filtros") #cabeçalho da barra lateral
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data['Regiao'].unique(), #opções
        data['Regiao'].unique() #opções selecionadas por padrão
    )
    filtered_data = data[data['Regiao'].isin(selected_region)] #filtro
    st.write(filtered_data) #exibe o dataframe
    
#4- Função para exibir os gráficos
def display_charts(data):
    st.header("Visualização de Gráficos")
    #st.set_option("deprecation.showPyplotGlobalUse", False) #remove mensagens de Warren
    
    #Gráfico 1: Desempenho por Região
    st.subheader("Desempenho por Região")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="Regiao", data=data, ax=ax)
    st.pyplot(fig)
    #plt.figure(figsize=(10, 6))
    #sns.countplot(x="Regiao", data=data)
    #st.pyplot()
    
    #Gráfico 2: Itens mais vendidos
    st.subheader("Itens mais Vendidos")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x="Item", data=data, ax=ax)
    st.pyplot(fig)
    #plt.figure(figsize=(10, 6))
    #sns.countplot(x="Item", data=data)
    #st.pyplot()
    
    #Gráfico 3: Preço Médio por Item
    st.subheader("Preço Médio por Item")
    avg_price = data.groupby("Item")["PrecoUnidade"].mean().sort_values(ascending=False)
    st.write(avg_price)

#5- Função para exibir métricas
def display_metrics(data):
    st.subheader("Métricas")
    
    #Métricas simples
    total_sales = data["Unidades"].sum()
    average_price = data["PrecoUnidade"].mean()
    most_productive = data["Vendedor"].value_counts().idxmax()
    
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        st.metric("O vendedor mais produtivo foi:", most_productive)
    with coluna2:
        st.metric("Vendas Totais:", total_sales)
    with coluna3:
        st.metric("Preço Médio:", round(average_price, 2))
    
#6- Execução do aplicativo
if __name__ == "__main__":
    main()