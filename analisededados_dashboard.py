#!/usr/bin/env python
# coding: utf-8

# # Integração Dash e Python
# - Descrição da  documentação: Dash is a python framework created by plotly for creating interactive web applications<br>
# O Dash é uma ferramente criada a partir do plotly/matplotlib (criação de gráficos) e do flask (criação de apps). A integração permite a inserção de gráficos na internet.
# 
# ##### Instalação do Dash:
# pip install dash<br>
# pip install dash-auth (autenticador do dash)
# 
# ##### Funcionamento do Dash:
# - Layout (front-end):
#     - HTML (textos, imagens, edição estática)
#     - Dash components (componentes dos gráficos)
# - Callbacks (back-end)
# 
# ##### Início do código do Dash:
# Na página do Dash, copiar e colar o código inicial padrão
# 
# ##### Desafio:
# A partir da base de dados excel (vendas de diversas lojas de uma rede de shoppings ao longo do mês de dezembro de 2019), criar um dashboard online que apresente, de forma interativa, as quantidades vendidas de cada produto em cada loja.

# In[1]:


import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from dash import Dash, html, dcc


# In[2]:


#importação da base de dados

df = pd.read_excel('Vendas.xlsx')
display(df)
df.info()


# In[3]:


df_lojas_produtos = df[['ID Loja', 'Produto', 'Quantidade', 'Valor Unitário', 'Valor Final']].groupby(['ID Loja', 'Produto']).sum()
df_lojas_produtos = df_lojas_produtos.reset_index()
display(df_lojas_produtos)


# ##### Criação do aplicativo dash
# Na documentação do dash (https://dash.plotly.com/layout) há um tutorial de criação

# In[4]:


# gráficos MATPLOTLIB / SEABORN
plt.figure(figsize=(10,5))
plt.title('VALOR dos produtos vendidos por loja na rede de shoppings em dezembro/2019')
fig1 = sns.barplot(data=df_lojas_produtos, x='ID Loja', y='Valor Final', hue='Produto')
fig1.tick_params(axis='x', rotation=90) 

plt.figure(figsize=(10,5))
plt.title('QUANTIDADE de produtos vendidos por loja na rede de shoppings em dezembro/2019')
fig2 = sns.barplot(data=df_lojas_produtos, x='ID Loja', y='Quantidade', hue='Produto')
fig2.tick_params(axis='x', rotation=90) 

plt.figure(figsize=(10,5))
plt.title('QUANTIDADE e VALOR dos produtos vendidos por loja na rede de shoppings em dezembro/2019')
fig3 = sns.scatterplot(data=df_lojas_produtos, x='Quantidade', y='Valor Final', hue='Produto', size='ID Loja', sizes=(10,500))
fig3.tick_params(axis='x', rotation=90) 


# In[6]:


# gráficos PLOTLY
fig1 = px.bar(df_lojas_produtos, x='ID Loja', y='Valor Final', color='Produto', barmode='group')
fig1.show()

fig2 = px.bar(df_lojas_produtos, x='ID Loja', y='Quantidade', color='Produto', barmode='group')
fig2.show()

fig3 = px.scatter(df_lojas_produtos, x='Quantidade', y='Valor Final', color='Produto', size='Valor Unitário', size_max=60)
fig3.show()


# In[ ]:


app = Dash(__name__)

############################## GRÁFICOS ##############################
fig1 = px.bar(df_lojas_produtos, x='ID Loja', y='Valor Final', color='Produto')
fig2 = px.bar(df_lojas_produtos, x='ID Loja', y='Quantidade', color='Produto')
fig3 = px.scatter(df_lojas_produtos, x='Quantidade', y='Valor Final', color='Produto', size='Valor Unitário', size_max=60)

############################## LAYOUT DASH ##############################

#html.H1: título 
#html.Div: sub-título
#parâmetro children: texto
#parâmetro style: edição em css
#html.H3: título, porém menor que o H1
#dcc.Graph(id, figure): nome do gráfico e seu placeholder
#dcc.RadioItems: botões de navegação no gráfico
app.layout = html.Div(children=[
    
    html.H1(children='Meu Dashboard (Revisão)'),

    html.Div(children='''
        Dashboard de vendas de uma rede de shoppings:
    '''),

    html.H3(children='VALOR dos produtos vendidos por loja na rede de shoppings em dezembro/2019'),
    
    dcc.Graph(id='grafico_barras1', figure=fig1),
    
    html.H3(children='QUANTIDADE de produtos vendidos por loja na rede de shoppings em dezembro/2019'),
    
    dcc.Graph(id='grafico_barras2', figure=fig2),
    
    html.H3(children='QUANTIDADE e VALOR dos produtos vendidos por loja na rede de shoppings em dezembro/2019'),
    
    dcc.Graph(id='grafico_scatter', figure=fig3),
    
], style={'text-align':'center'})

    

############################## UPLOAD DO DASH NA INTERNET ##############################
if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:




