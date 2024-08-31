import plotly.express as px
import pandas as pd

# Crear los datos
'''
A G T T A G A G T T A G
T C A A T C T C A A T C
'''
ADN_MATRIZ = [
   "A","G","T","T","A","G","A","G","T","T","A","G",
   "T","C","A","A","T","C","T","C","A","A","T","C",
]
numbers_of_bases = int(len(ADN_MATRIZ)/2)

data = {
    'x': list(range(numbers_of_bases)) + list(range(numbers_of_bases)),  # Puntos en el eje x, dos veces el mismo rango
    'y': [1]*numbers_of_bases + [1.2]*numbers_of_bases,  # Dos líneas paralelas en el eje y: 1 y 2
    'class': ADN_MATRIZ
}

df = pd.DataFrame(data)

# Crear el diagrama de puntos
fig = px.scatter(df, x='x', y='y', color='class', title='Ejemplo de ADN')

fig.update_layout(
    yaxis=dict(
        tickvals=[1, 2],  # Valores fijos en el eje y
        ticktext=['Línea 1', 'Línea 2'],  # Etiquetas para los valores fijos
        range=[0.5, 10]  # Rango del eje y para mantener las líneas visibles
    )
)

# Mostrar el gráfico
fig.show()