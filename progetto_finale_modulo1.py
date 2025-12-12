# parte 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

date=[]

for x in pd.date_range("2024-03-15",periods=6,freq="d"):
    date.append(x)
    date.append(x)
    date.append(x)
    date.append(x)
    date.append(x)

sedi=["Roma","Milano","Napoli","Venezia","Torino"]
prodotti=["smartphone","laptop","TV","stereo","auricolari","radio",]
prezzi=[399.99, 599.99, 299.99, 29.99, 9.99, 19.99]

df=pd.DataFrame({
    "Data":date,
    "Negozio":sedi*6,
    "prodotto":prodotti*5,
    "quantità":np.random.randint(10,21,30),
    "prezzo unitario":prezzi*5
})

df.to_csv("vendite.csv",index=False)
print(pd.read_csv("vendite.csv"))