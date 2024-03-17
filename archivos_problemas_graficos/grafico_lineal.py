import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos_problemas_graficos\\pedos.csv')

#Creando
sns.lineplot(x='fecha', y='pedos', data=df)

#Creando un punto en el momento de mas pedos
plt.plot('01-09',17,"o")

plt.show()