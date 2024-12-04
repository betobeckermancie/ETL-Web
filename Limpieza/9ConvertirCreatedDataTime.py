import pandas as pd

#convertir la columna createdAt a datetime
df['createdAt'] = pd.to_datetime(df["createdAt"])

#verificar cambios
print("df.types")