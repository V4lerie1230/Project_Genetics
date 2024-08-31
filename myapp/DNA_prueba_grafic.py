import plotly.express as px
import pandas as pd
import numpy as np

# Definir el tamaño del DataFrame
num_values = 10


def function(x): 
    return x**2 - 3 
range_x = list(range(100))
range_y  = list(map(lambda x: function(x), range_x))

# Crear el DataFrame con valores aleatorios
df = pd.DataFrame({
    'x': range_x,
    'y': range_y
})

# Mostrar el DataFrame
print(df)

# df = px.data.iris()
fig = px.scatter(df, x="x", y="y", title="DNA aminoacids")

# If you print the figure, you'll see that it's just a regular figure with data and layout
print(fig)
print(df)
fig.show()

#  IMPORTANT: Search how to change data in the predetermined code. 
