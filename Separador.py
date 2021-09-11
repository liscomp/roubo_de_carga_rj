#%% Import modules
import numpy as np # Arrays module
import pandas as pd # DataFrame module
#%% Data processing
roubo = pd.read_csv("BaseDPEvolucaoMensalCisp_2003-2019.csv",
                    sep=";",index_col=False,encoding="iso-8859-1",
                    usecols=["CISP","mes","ano","AISP","RISP","munic","Regiao","roubo_carga"],
                    skipinitialspace=True)
pop_Mensal = pd.read_csv("PopulacaoEvolucaoMensalCisp.csv",
                         sep=";",index_col=False,
                         skipinitialspace=True)
pop_Anual  = pd.read_csv("PopulacaoEvolucaoAnualCisp.csv",
                         sep=";",index_col=False,
                         skipinitialspace=True)
delegacias = pd.read_csv("Tabela_CISP_Delegacia.csv",
                         sep=";",index_col='CISP',
                         skipinitialspace=True)

qtd_colunas = len(delegacias)
colunas = np.full(qtd_colunas,'CISP',dtype=object) + delegacias.index.values.astype(str) + np.full(qtd_colunas,' (',dtype=object) + delegacias['Nome das CISP’s'] + np.full(qtd_colunas,')',dtype=object)
colunas = pd.Index(colunas,name='CISP')
#%%
roubo_CISP = roubo[["CISP","roubo_carga"]].groupby(by=["CISP"]).sum().reset_index()
roubo_Mensal = roubo[["ano","mes","roubo_carga"]].groupby(by=["ano","mes"]).sum()["roubo_carga"]
roubo_Anual = roubo[["ano","roubo_carga"]].groupby(by=["ano"]).sum()["roubo_carga"]
roubo_CISP_Mensal = roubo[["CISP","mes","ano","roubo_carga"]].groupby(by=["CISP","ano","mes"]).sum().reset_index()
roubo_CISP_Anual = roubo[["CISP","ano","roubo_carga"]].groupby(by=["CISP","ano"]).sum().reset_index()
#%%
Tabela_Roubo_CISP = roubo_CISP.pivot_table(values=["roubo_carga"],columns=["CISP"]).reset_index(drop=True)
Tabela_Roubo_CISP_Mensal = roubo_CISP_Mensal.pivot_table(values=["roubo_carga"], index= ["ano","mes"],columns=["CISP"])["roubo_carga"]
Tabela_Roubo_CISP_Anual = roubo_CISP_Anual.pivot_table(values=["roubo_carga"], index= ["ano"],columns=["CISP"])["roubo_carga"]

tabela_pop_CISP_Mensal = pop_Mensal.pivot_table(values=["pop"], index=["ano","mes"], columns=["CISP"])["pop"]
tabela_pop_CISP_Anual  = pop_Anual.pivot_table(values=["pop"], index=["ano"], columns=["CISP"])["pop"]
#%%
Tabela_Roubo_CISP_Mensal_Self = Tabela_Roubo_CISP_Mensal.div(Tabela_Roubo_CISP.to_numpy(),axis='columns')
Tabela_Roubo_CISP_Anual_Self = Tabela_Roubo_CISP_Anual.div(Tabela_Roubo_CISP.to_numpy(),axis='columns')
Tabela_Roubo_CISP_Mensal_Others = Tabela_Roubo_CISP_Mensal.div(roubo_Mensal,axis='index')
Tabela_Roubo_CISP_Anual_Others  = Tabela_Roubo_CISP_Anual.div(roubo_Anual,axis='index')
#%%
Tabela_Roubo_CISP_Mensal_pop = Tabela_Roubo_CISP_Mensal.div(tabela_pop_CISP_Mensal,axis='index')
Tabela_Roubo_CISP_Anual_pop = Tabela_Roubo_CISP_Anual.div(tabela_pop_CISP_Anual,axis='index')
del Tabela_Roubo_CISP_Mensal_pop[1]
del Tabela_Roubo_CISP_Anual_pop[1]

Tabela_Roubo_CISP_pop = Tabela_Roubo_CISP_Anual_pop.sum(axis=0)
Tabela_Roubo_Mensal_pop = Tabela_Roubo_CISP_Mensal_pop.sum(axis=1)
Tabela_Roubo_Anual_pop =  Tabela_Roubo_CISP_Anual_pop.sum(axis=1)

Tabela_Roubo_CISP_Mensal_Self_pop = Tabela_Roubo_CISP_Mensal_pop.div(Tabela_Roubo_CISP_pop,axis='columns')
Tabela_Roubo_CISP_Anual_Self_pop = Tabela_Roubo_CISP_Anual_pop.div(Tabela_Roubo_CISP_pop,axis='columns')
Tabela_Roubo_CISP_Mensal_Others_pop = Tabela_Roubo_CISP_Mensal_pop.div(Tabela_Roubo_Mensal_pop,axis='index')
Tabela_Roubo_CISP_Anual_Others_pop  = Tabela_Roubo_CISP_Anual_pop.div(Tabela_Roubo_Anual_pop,axis='index')
#%%
Tabela_Roubo_CISP_Mensal.columns = colunas
Tabela_Roubo_CISP_Anual.columns = colunas
Tabela_Roubo_CISP_Mensal_Self.columns = colunas
Tabela_Roubo_CISP_Anual_Self.columns = colunas
Tabela_Roubo_CISP_Mensal_Others.columns = colunas
Tabela_Roubo_CISP_Anual_Others.columns = colunas
delegacias.index = colunas

colunas = colunas.delete(0)
Tabela_Roubo_CISP_Mensal_pop.columns = colunas
Tabela_Roubo_CISP_Anual_pop.columns = colunas
Tabela_Roubo_CISP_Mensal_Self_pop.columns = colunas
Tabela_Roubo_CISP_Anual_Self_pop.columns = colunas
Tabela_Roubo_CISP_Mensal_Others_pop.columns = colunas
Tabela_Roubo_CISP_Anual_Others_pop.columns = colunas
#%%
Lista_Roubo_CISP_Mensal            = Tabela_Roubo_CISP_Mensal.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
Lista_Roubo_CISP_Mensal_pop        = Tabela_Roubo_CISP_Mensal_pop.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal_pop.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
Lista_Roubo_CISP_Mensal_Self       = Tabela_Roubo_CISP_Mensal_Self.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal_Self.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
Lista_Roubo_CISP_Mensal_Others     = Tabela_Roubo_CISP_Mensal_Others.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal_Others.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
Lista_Roubo_CISP_Mensal_Self_pop   = Tabela_Roubo_CISP_Mensal_Self_pop.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal_Self_pop.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
Lista_Roubo_CISP_Mensal_Others_pop = Tabela_Roubo_CISP_Mensal_Others_pop.reset_index().melt(id_vars=['ano','mes'],value_vars=list(Tabela_Roubo_CISP_Mensal_Others_pop.columns),var_name='CISP',value_name='roubo_carga').set_index(['CISP','ano','mes']).join(delegacias)
#%%
Tabela_Roubo_CISP_Mensal.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal.csv",sep=";")
Tabela_Roubo_CISP_Anual.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual.csv",sep=";")
Tabela_Roubo_CISP_Mensal_Self.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal_Self.csv",sep=";")
Tabela_Roubo_CISP_Anual_Self.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual_Self.csv",sep=";")
Tabela_Roubo_CISP_Mensal_Others.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal_Others.csv",sep=";")
Tabela_Roubo_CISP_Anual_Others.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual_Others.csv",sep=";")
Tabela_Roubo_CISP_Mensal_pop.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal_pop.csv",sep=";")
Tabela_Roubo_CISP_Anual_pop.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual_pop.csv",sep=";")
Tabela_Roubo_CISP_Mensal_Self_pop.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal_Self_pop.csv",sep=";")
Tabela_Roubo_CISP_Anual_Self_pop.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual_Self_pop.csv",sep=";")
Tabela_Roubo_CISP_Mensal_Others_pop.to_csv("Tabela/Mensal/Tabela_Roubo_CISP_Mensal_Others_pop.csv",sep=";")
Tabela_Roubo_CISP_Anual_Others_pop.to_csv("Tabela/Anual/Tabela_Roubo_CISP_Anual_Others_pop.csv",sep=";")
#%%
Lista_Roubo_CISP_Mensal['mes/ano'] = Lista_Roubo_CISP_Mensal.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal.index.get_level_values(1).astype(str)
Lista_Roubo_CISP_Mensal_pop['mes/ano'] = Lista_Roubo_CISP_Mensal_pop.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal_pop.index.get_level_values(1).astype(str)
Lista_Roubo_CISP_Mensal_Self['mes/ano'] = Lista_Roubo_CISP_Mensal_Self.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal_Self.index.get_level_values(1).astype(str)
Lista_Roubo_CISP_Mensal_Others['mes/ano'] = Lista_Roubo_CISP_Mensal_Others.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal_Others.index.get_level_values(1).astype(str)
Lista_Roubo_CISP_Mensal_Self_pop['mes/ano'] = Lista_Roubo_CISP_Mensal_Self_pop.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal_Self_pop.index.get_level_values(1).astype(str)
Lista_Roubo_CISP_Mensal_Others_pop['mes/ano'] = Lista_Roubo_CISP_Mensal_Others_pop.index.get_level_values(2).astype(str) + '/' + Lista_Roubo_CISP_Mensal_Others_pop.index.get_level_values(1).astype(str)
# %%
Lista_Roubo_CISP_Mensal.to_csv("Lista/Lista_Roubo_CISP_Mensal.csv",sep=";")
Lista_Roubo_CISP_Mensal_pop.to_csv("Lista/Lista_Roubo_CISP_Mensal_pop.csv",sep=";")
Lista_Roubo_CISP_Mensal_Self.to_csv("Lista/Lista_Roubo_CISP_Mensal_Self.csv",sep=";")
Lista_Roubo_CISP_Mensal_Others.to_csv("Lista/Lista_Roubo_CISP_Mensal_Others.csv",sep=";")
Lista_Roubo_CISP_Mensal_Self_pop.to_csv("Lista/Lista_Roubo_CISP_Mensal_Self_pop.csv",sep=";")
Lista_Roubo_CISP_Mensal_Others_pop.to_csv("Lista/Lista_Roubo_CISP_Mensal_Others_pop.csv",sep=";")
# %%
Lista_Roubo_CISP_Mensal.index = Lista_Roubo_CISP_Mensal.index.reorder_levels(['ano','mes','CISP'])
Lista_Roubo_CISP_Mensal_pop.index = Lista_Roubo_CISP_Mensal_pop.index.reorder_levels(['ano','mes','CISP'])
Lista_Roubo_CISP_Mensal_Self.index = Lista_Roubo_CISP_Mensal_Self.index.reorder_levels(['ano','mes','CISP'])
Lista_Roubo_CISP_Mensal_Others.index = Lista_Roubo_CISP_Mensal_Others.index.reorder_levels(['ano','mes','CISP'])
Lista_Roubo_CISP_Mensal_Self_pop.index = Lista_Roubo_CISP_Mensal_Self_pop.index.reorder_levels(['ano','mes','CISP'])
Lista_Roubo_CISP_Mensal_Others_pop.index = Lista_Roubo_CISP_Mensal_Others_pop.index.reorder_levels(['ano','mes','CISP'])
# %%
Lista_Roubo_CISP_Max = pd.DataFrame(Lista_Roubo_CISP_Mensal.loc[(ano,*Lista_Roubo_CISP_Mensal.loc[ano]['roubo_carga'].idxmax())] for ano in range(2003,2020))
Lista_Roubo_CISP_Max.index = pd.MultiIndex.from_tuples(Lista_Roubo_CISP_Max.index, names=('ano', 'mes','CISP')).reorder_levels(['CISP','ano', 'mes'])
Lista_Roubo_CISP_Max_pop = pd.DataFrame(Lista_Roubo_CISP_Mensal_pop.loc[(ano,*Lista_Roubo_CISP_Mensal_pop.loc[ano]['roubo_carga'].idxmax())] for ano in range(2003,2020))
Lista_Roubo_CISP_Max_pop.index = pd.MultiIndex.from_tuples(Lista_Roubo_CISP_Max_pop.index, names=('ano', 'mes','CISP')).reorder_levels(['CISP','ano', 'mes'])
# %%
Lista_Roubo_CISP_Max.to_csv("Lista/Lista_Roubo_CISP_Max.csv",sep=";")
Lista_Roubo_CISP_Max_pop.to_csv("Lista/Lista_Roubo_CISP_Max_pop.csv",sep=";")
# %%
