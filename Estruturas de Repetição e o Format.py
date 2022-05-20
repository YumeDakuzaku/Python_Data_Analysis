#!/usr/bin/env python
# coding: utf-8

# # Passo 1 - Percorrer todos os arquivos da pasta da base de dados 

# In[1]:


import os #biblioteca para trabalhar com arquivos, diretórios do pc, google drive, etc
import pandas as pd #biblioteca pandas para ler o arquivo 


# In[2]:


lista_arquivo = os.listdir("C:/Users/DANIEL/Documents/YD_Hashtag/Vendas") #lembrar de substituir \ para /


# In[3]:


print(lista_arquivo) 


# In[4]:


display(lista_arquivo) #mesma função que o print, porém visualmente melhor


# # Passo 2 - Importar as bases de dados apenas de "Vendas"

# In[5]:


tabela_consolidada = pd.DataFrame()
for arquivo in lista_arquivo: #Atenção para respeitar a indentação do ptyhon
    if "Vendas" in arquivo:
        #print(f"C:/Users/DANIEL/Documents/YD_Hashtag/Vendas/{arquivo}")
        #else:
        #print('Não é um Arquivo de venda') importar nesse formato ou através do read do pandas:
        tabela = pd.read_csv(f"C:/Users/DANIEL/Documents/YD_Hashtag/Vendas/{arquivo}")
        tabela_consolidada = tabela_consolidada.append(tabela) #para adicionar a nova tabela


# # Passo 3 - Mostrar todas bases de dados consolidadas

# In[6]:


display(tabela_consolidada)


# # Passo 4 - Calcular o produto mais vendido (em quantidade)

# In[7]:


tabela_produtos = tabela_consolidada.groupby('Produto').sum().sort_values(by="Quantidade Vendida", ascending = False)
#Somando pela quantidade vendida e em ordem decrescente.
display(tabela_produtos)


# # Passo 5 - Calcular o produto que mais faturou

# In[8]:


tabela_consolidada['Faturamento'] = tabela_consolidada['Preco Unitario']*tabela_consolidada['Quantidade Vendida']
tabela_faturamento = tabela_consolidada.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']]
display(tabela_faturamento)


# # Passo 6 - Calcular a loja/cidade que mais vendeu - criar um gráfico

# In[9]:


tabela_consolidada['Faturamento'] = tabela_consolidada['Preco Unitario']*tabela_consolidada['Quantidade Vendida']
tabela_loja = tabela_consolidada.groupby('Loja').sum().sort_values(by="Faturamento", ascending = False)
tabela_loja = tabela_loja[['Faturamento']]
display(tabela_loja)


# In[10]:


import plotly.express as px #importando a biblioteca que cria gráficos

grafico =px.bar(tabela_loja,x=tabela_loja.index,y='Faturamento') #Excessão x= tabela.index, porque quando usa groupby vira um índice 
grafico.show()


# link da vídeo aula: https://www.youtube.com/playlist?list=PLpdAy0tYrnKyCZsE-ifaLV1xnkXBE9n7T
