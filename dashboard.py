from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Lê o arquivo Excel e armazena os dados em uma variável chamada df
df = pd.read_excel("Produtos.xlsx")

# Cria o gráfico de barras
fig = px.bar(df, x="Produtos", y="Quantidade", color="Produtos")

# Layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Faturamento da Loja'),
    html.H2(children='Gráfico dos produtos da loja'),
    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)


