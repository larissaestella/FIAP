import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go

# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")

# Adicionando o logo
st.image("logo.png", width=150)

# Criando as páginas
pages = st.sidebar.selectbox("Escolha a Distribuição:", [
    "Introdução",
    "Distribuição de Bernoulli",
    "Distribuição Binomial",
    "Distribuição de Poisson",
    "Distribuição Normal",
    "Analise seus Dados"
])

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)

if pages == "Introdução":
    st.title("Aula de Distribuições Probabilísticas - FIAP")
    st.write("As distribuições probabilísticas são fundamentais para a Inferência Estatística e Machine Learning, permitindo modelar incertezas e entender padrões nos dados.")
    st.write("Por exemplo, ao estimar a chance de um cliente converter em uma compra, podemos usar uma distribuição Bernoulli. Já para prever a demanda por um produto, uma distribuição Poisson pode ser aplicada. Modelos de aprendizado de máquina, como redes neurais e regressão logística, também se beneficiam dessas distribuições para ajustar pesos e probabilidades de classificação.")
    st.video("https://www.youtube.com/watch?v=f6nXayXgjZI")

elif pages == "Distribuição de Bernoulli":
    st.header("Distribuição de Bernoulli")
    st.write("A distribuição de Bernoulli modela experimentos com duas possibilidades: sucesso (1) ou fracasso (0). Um exemplo clássico é o lançamento de uma moeda, onde podemos definir sucesso como 'cara' e fracasso como 'coroa'.")
    st.latex(r"P(X = x) = p^x (1 - p)^{1-x}, \quad x \in \{0,1\}")
    p = st.slider("Probabilidade de sucesso (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    valores = [0, 1]
    probabilidades = [1 - p, p]
    df_bernoulli = pd.DataFrame({"X": valores, "P(X)": probabilidades})
    st.write("Tabela de probabilidades:")
    st.write(df_bernoulli)
    plot_distribution(valores, probabilidades, "Distribuição de Bernoulli", "Resultado", "Probabilidade")

elif pages == "Distribuição Binomial":
    st.header("Distribuição Binomial")
    st.write("A distribuição Binomial modela o número de sucessos em n tentativas independentes. Um exemplo seria acertar um pênalti em 10 tentativas, dado que um jogador tem 80% de acerto.")
    st.latex(r"P(X = k) = \binom{n}{k} p^k (1 - p)^{n-k}")
    n = st.slider("Número de tentativas (n):", min_value=1, max_value=50, value=10, step=1)
    k = st.slider("Número de sucessos (k):", min_value=0, max_value=n, value=5, step=1)
    p = st.slider("Probabilidade de sucesso (p):", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    x = np.arange(0, n + 1)
    y = stats.binom.pmf(x, n, p)
    df_binomial = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)})
    st.write("Tabela de probabilidades:")
    st.write(df_binomial)
    plot_distribution(x, y, "Distribuição Binomial", "Número de sucessos", "Probabilidade")

elif pages == "Distribuição de Poisson":
    st.header("Distribuição de Poisson")
    st.latex(r"P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}")
    lambd = st.slider("Taxa média de ocorrência (λ):", min_value=1, max_value=20, value=5, step=1)
    x = np.arange(0, lambd * 3)
    y = stats.poisson.pmf(x, lambd)
    df_poisson = pd.DataFrame({"X": x, "P(X)": y, "P(X ≤ k) (Acumulado)": np.cumsum(y)})
    st.write("Tabela de probabilidades:")
    st.write(df_poisson)
    plot_distribution(x, y, "Distribuição de Poisson", "Número de eventos", "Probabilidade")

elif pages == "Distribuição Normal":
    st.header("Distribuição Normal")
    mu = st.number_input("Média (μ):", value=0.0)
    sigma = st.number_input("Desvio Padrão (σ):", value=1.0, min_value=0.1)
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    y = stats.norm.pdf(x, mu, sigma)
    y_cdf = stats.norm.cdf(x, mu, sigma)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='PDF'))
    fig.add_trace(go.Scatter(x=x, y=y_cdf, mode='lines', name='CDF'))
    fig.update_layout(title="Distribuição Normal", xaxis_title="Valores", yaxis_title="Densidade / Probabilidade acumulada")
    st.plotly_chart(fig)

elif pages == "Analise seus Dados":
    st.header("Análise de Dados")
    st.write("Faça upload do seu arquivo Excel para analisar a distribuição de uma variável numérica.")
    uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=["xlsx", "xls"])
    
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write("Amostra dos dados:")
        st.write(df.head())
        
        colunas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
        if colunas_numericas:
            coluna_escolhida = st.selectbox("Escolha uma coluna numérica:", colunas_numericas)
            
            if coluna_escolhida:
                st.write("Distribuição dos dados:")
                st.write(df[coluna_escolhida].describe())
                
                dist = st.selectbox("Escolha a distribuição para análise:", ["Poisson", "Normal", "Binomial"])
                
                if dist == "Poisson":
                    lambda_est = df[coluna_escolhida].mean()
                    st.write(f"Estimativa de λ: {lambda_est:.2f}")
                    x = np.arange(0, lambda_est * 3)
                    y = stats.poisson.pmf(x, lambda_est)
                    plot_distribution(x, y, "Distribuição de Poisson", "Número de eventos", "Probabilidade")
                
                elif dist == "Normal":
                    mu_est = df[coluna_escolhida].mean()
                    sigma_est = df[coluna_escolhida].std()
                    st.write(f"Estimativa de μ: {mu_est:.2f}, σ: {sigma_est:.2f}")
                    fig = px.histogram(df, x=coluna_escolhida, marginal="box", nbins=20, histnorm='probability density')
                    st.plotly_chart(fig)
                
                elif dist in ["Binomial"]:
                    threshold = st.number_input("Defina o limiar para True/False:")
                    p_est = (df[coluna_escolhida] > threshold).mean()
                    k = st.slider("Número de sucessos (k):", min_value=0, max_value=50, value=5, step=1)
                    st.write(f"Estimativa de p: {p_est:.2f}")
                    valores = np.arange(0, k + 1)
                    probabilidades = stats.binom.pmf(valores, k, p_est)
                    plot_distribution(valores, probabilidades, f"Distribuição {dist}", "Resultado", "Probabilidade")
                    df_binomial = pd.DataFrame({"X": valores, "P(X)": probabilidades})
                    st.write("Tabela de probabilidades:")
                    st.write(df_binomial)

