#%%
import numpy as np # modulo de arrays(vetores)
import pandas as pd # modulo de dataframe(tabelas)
import matplotlib.pyplot as plt # modulo de plot dados
from matplotlib.ticker import MultipleLocator
#%%
cores = {'CISP74 (Alcântara)':'darkorange', 
         'CISP72 (São Gonçalo)':'black',
         'CISP64 (São João de Meriti)':'red',
         'CISP59 (Duque de Caxias)':'lime',
         'CISP54 (Belford Roxo)':'forestgreen',
         'CISP39 (Pavuna)':'magenta',
         'CISP38 (Brás de Pina)':'yellow',
         'CISP34 (Bangu)':'olive',
         'CISP22 (Penha)':'navy',
         'CISP21 (Bonsucesso)':'purple',
         'CISP94 (Piraí)': 'red',
         'CISP5 (Mem de Sá)':'black',
         'CISP44 (Inhaúma)':'blue',
         'CISP40 (Honório Gurgel)':'cyan',
         'CISP17 (São Cristovão)':'red',
         'CISP35 (Campo Grande)':'maroon',
         'CISP33 (Realengo)':'deeppink',
         'CISP31 (Ricardo de Albuquerque)':'navy',
         'CISP52 (Nova Iguaçu)':'red',
         'CISP25 (Engenho Novo)':'darkorange',
         'CISP29 (Madureira)':'deeppink',
         'CISP4 (Praça da República)':'lime',
         'CISP24 (Piedade)':'maroon',
         'CISP23 (Méier)':'darkorchid',
         }
marcas = {'CISP74 (Alcântara)':'s', 
         'CISP72 (São Gonçalo)':'o',
         'CISP64 (São João de Meriti)':'s',
         'CISP59 (Duque de Caxias)':'D',
         'CISP54 (Belford Roxo)':'^',
         'CISP39 (Pavuna)':'^',
         'CISP38 (Brás de Pina)':'<',
         'CISP34 (Bangu)':'>',
         'CISP22 (Penha)':'+',
         'CISP21 (Bonsucesso)':'x',
         'CISP94 (Piraí)': '^',
         'CISP5 (Mem de Sá)':'s',
         'CISP44 (Inhaúma)':'>',
         'CISP40 (Honório Gurgel)':'v',
         'CISP17 (São Cristovão)':'o',
         'CISP35 (Campo Grande)':'_',
         'CISP33 (Realengo)':'o',
         'CISP31 (Ricardo de Albuquerque)':'D',
         'CISP52 (Nova Iguaçu)':'X',
         'CISP25 (Engenho Novo)':'x',
         'CISP29 (Madureira)':'v',
         'CISP4 (Praça da República)':'o',
         'CISP24 (Piedade)':'v',
         'CISP23 (Méier)':'s',
         }
#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
CISP_Anual = dados[dados.sum(axis=0).sort_values(ascending=False).index].columns[:CISPs]
CISP_Anual = CISP_Anual[np.array([''.join(numero for numero in cisp if numero.isdigit()) for cisp in CISP_Anual],dtype=np.uint32).argsort()[::-1]]
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
ax.set_ylim(ymin = 0,ymax = 800) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Número de roubos",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.05,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal
#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual_Others"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
CISP_Anual_Others = dados[dados.sum(axis=0).sort_values(ascending=False).index].columns[:CISPs]
CISP_Anual_Others = CISP_Anual_Others[np.array([''.join(numero for numero in cisp if numero.isdigit()) for cisp in CISP_Anual_Others],dtype=np.uint32).argsort()[::-1]]
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual_Others:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
ax.set_ylim(ymin = 0,ymax = 0.17) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Probabilidade",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.05,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual_Others,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal
#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual_Self"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
#ax.set_ylim(ymin = 0,ymax = 0.165) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Probabilidade",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.05,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal

#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual_pop"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
CISP_Anual_pop = dados[dados.sum(axis=0).sort_values(ascending=False).index].columns[:CISPs]
CISP_Anual_pop = CISP_Anual_pop[np.array([''.join(numero for numero in cisp if numero.isdigit()) for cisp in CISP_Anual_pop],dtype=np.uint32).argsort()[::-1]]
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual_pop:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
ax.set_ylim(ymin = 0,ymax = 0.004) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Número de roubos normalizado pela população",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.05,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual_pop,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal
#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual_Others_pop"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
CISP_Anual_Others_pop = dados[dados.sum(axis=0).sort_values(ascending=False).index].columns[:CISPs]
CISP_Anual_Others_pop = CISP_Anual_Others_pop[np.array([''.join(numero for numero in cisp if numero.isdigit()) for cisp in CISP_Anual_Others_pop],dtype=np.uint32).argsort()[::-1]]
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual_Others_pop:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
ax.set_ylim(ymin = 0,ymax = 0.135) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Probabilidade",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.05,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual_Others_pop,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal
#%%
CISPs = 15
arquivo = "Tabela_Roubo_CISP_Anual_Self_pop"
dados = pd.read_csv("Tabela/Anual/"+arquivo+".csv",sep=";",index_col=["ano"])
#%%
dpi = 300 # Defino o dpi usado na figura
# Criamos a figura e o eixo de plotagem
fig, ax = plt.subplots(figsize=(10,8),dpi=dpi) # Tamanho da figura em inch (10,8) e o dpi (300)
plt.title(arquivo,fontweight='bold', size = 15) # Plotar o titulo da figura
# Plotar o fit
for cisp in CISP_Anual_pop:
  if cisp not in cores.keys() and cisp not in marcas.keys():
    ax.plot(dados[cisp],lw=1)
  else:
    ax.plot(dados[cisp],color=cores[cisp],marker=marcas[cisp],lw=1)
ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.set_facecolor("whitesmoke") # Cor do fundo do grafico
# Grades do fundo do grafico
ax.grid(color='white', # Cor das linhas grade
        linestyle='-', # Tipo de linha da grade
        linewidth=3) # Grossura da linha da grade
# Definir limite dos eixos apresentados na figura
ax.set_xlim(xmin = 2002,xmax = 2020) # (minimo,maximo)
#ax.set_ylim(ymin = 0,ymax = 0.165) # (minimo,maximo)
# Definir os rotulos dos eixos 
ax.set_xlabel("Ano",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.set_ylabel("Probabilidade",fontweight='bold', # Nome do rotulo
              size = 15) # Tamanho do rotulo
ax.minorticks_on() # Ligar os traços menores dos eixos
# Definir comos os traços dos eixos são apresentados
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "major" , # Traços maiores dos eixos
               direction = "in", # Direcao dos tracos
               length = 10, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis ="both", # Eixos (both = os dois eixos)
               which = "minor" , # Tracos menores dos eixos
               direction = "in", # Direcao dos tracos
               length = 5, # Tamanho dos tracos
               width = 1.5, # Grossura dos tracos
               bottom = True, top = True, left = True, right = True) # Ligar os tracos nos eixos
ax.tick_params(axis = "both", labelsize = 15) # Valores nos eixos
ax.legend(fontsize = 8, # Tamanho do texto na legenda
          loc = (0.1,0.75), # Localizacao da legenda em relacao ao tamanho do eixo ((0,0) -> esquerda inferior do eixo)
          labels = CISP_Anual_pop,
          ncol = 2, 
          edgecolor ="black") # Cor da borda
props = dict(boxstyle='round', facecolor='white')
fig.savefig("Graficos/"+arquivo,dpi=dpi,bbox_inches='tight',pad_inches=0.1) # Exportar a figura
plt.show() # Imprimir a figura no terminal
# %%
