#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
#
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
#
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
#
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[9]:
import pandas as pd
import numpy as np

black_friday = pd.read_csv("black_friday.csv")

# ## Inicie sua análise a partir daqui

# In[84]:


black_friday.head(5)


# ## Questão 1
#
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[85]:


def q1():
    return black_friday.shape
    pass


# ## Questão 2
#
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[29]:


def q2():
    return black_friday[(black_friday["Age"] == '26-35') & (black_friday["Gender"] == 'F')].shape[0]
    pass


# ## Questão 3
#
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[87]:


def q3():
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
#
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[88]:


def q4():
    return np.unique(black_friday.dtypes.values).shape[0]
    pass


# ## Questão 5
#
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[89]:


def q5():
    nrows = black_friday.shape[0]
    null_filter = black_friday.isnull().any(axis=1).values
    register_any_null = black_friday.loc[null_filter, :].shape[0]
    return register_any_null / nrows
    pass


# ## Questão 6
#
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[90]:


def q6():
    return black_friday.isna().sum().max()
    pass


# ## Questão 7
#
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[91]:


def q7():
    filter_not_null = black_friday.Product_Category_3.notnull()
    return black_friday.loc[filter_not_null, 'Product_Category_3'].mode()[0]
    pass


# ## Questão 8
#
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[92]:


def q8():
    purchase_aux = black_friday.Purchase - black_friday.Purchase.min()
    return (purchase_aux / (black_friday.Purchase.max() - black_friday.Purchase.min())).mean()
    pass


# ## Questão 9
#
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[93]:


def q9():
    purchase_std = black_friday.Purchase.std()
    black_friday_norm = (
        ((black_friday.Purchase - black_friday.Purchase.mean()) / purchase_std))
    return black_friday_norm[(black_friday_norm < 1) & (black_friday_norm > -1)].count()
    pass


# ## Questão 10
#
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[94]:


def q10():
    return True if black_friday[(black_friday['Product_Category_2'].isna()) & (black_friday['Product_Category_3'].isna())].shape[0] == black_friday[(black_friday['Product_Category_2'].isna())].shape[0] else False
    pass


# %%
