# %% [markdown]
# ### LIBRERIAS

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# # EJERCICIO

# %% [markdown]
# - Carga la base de datos Northwind en un DataFrame de Pandas.
# - Utiliza la tabla de clientes para calcular el número de clientes por país.
# - Crea un gráfico de barras que muestre el número de clientes por país.
# - Ordena los países de manera descendente por el número de clientes.
# - Agrega títulos, etiquetas de ejes y cualquier otra información relevante al gráfico para que sea fácil de entender.

# %% [markdown]
# ## Carga la base de datos Northwind en un DataFrame de Pandas.

# %%
Categories = pd.read_csv('D:\ESP. MACHINE LEARNING\Categories.csv')
Customers = pd.read_csv('D:\ESP. MACHINE LEARNING\Customers.csv')
Employees = pd.read_csv('D:\ESP. MACHINE LEARNING\Employees.csv')
OrderDetails = pd.read_csv('D:\ESP. MACHINE LEARNING\OrderDetails.csv')
Orders = pd.read_csv('D:\ESP. MACHINE LEARNING\Orders.csv')
Products = pd.read_csv('D:\ESP. MACHINE LEARNING\Products.csv')
Shippers = pd.read_csv('D:\ESP. MACHINE LEARNING\Shippers.csv')
Suppliers = pd.read_csv('D:\ESP. MACHINE LEARNING\Suppliers.csv')

# %% [markdown]
# ## Utiliza la tabla de clientes para calcular el numero de clientes por pais

# %%
cantidad = Customers['Country'].value_counts().reset_index()
print(cantidad)

# %% [markdown]
# ## Crea un gráfico de barras que muestre el número de clientes por país.

# %%
barras = cantidad['count']
nombres = cantidad['Country']
plt.figure(figsize=(19, 6))
plt.bar(nombres, barras, width=0.7)

# %% [markdown]
# ## Ordena los países de manera descendente por el número de clientes.

# %%
tabla = cantidad.sort_values(by='count')  

# %% [markdown]
# ## Agrega títulos, etiquetas de ejes y cualquier otra información relevante al gráfico para que sea fácil de entender.

# %%
barras = tabla['count']
nombres = tabla['Country']
plt.figure(figsize=(19, 6))
plt.bar(nombres, barras, width=0.7)


