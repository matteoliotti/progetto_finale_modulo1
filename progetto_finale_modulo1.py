# parte 1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


with open("vendite.csv","w") as s:
    s.write("Data,Negozio,prodotto,quantita,prezzo_unitario\n"
            "2024-03-15,Roma,smartphone,11,399.99\n"
            "2024-03-15,Milano,laptop,15,599.99\n"
            "2024-03-15,Napoli,TV,13,299.99\n"
            "2024-03-15,Venezia,stereo,11,29.99\n"
            "2024-03-15,Torino,auricolari,14,9.99\n"
            "2024-03-16,Roma,radio,16,19.99\n"
            "2024-03-16,Milano,smartphone,10,399.99\n"
            "2024-03-16,Napoli,laptop,17,599.99\n"
            "2024-03-16,Venezia,TV,17,299.99\n"
            "2024-03-16,Torino,stereo,12,29.99\n"
            "2024-03-17,Roma,auricolari,14,9.99\n"
            "2024-03-17,Milano,radio,18,19.99\n"
            "2024-03-17,Napoli,smartphone,15,399.99\n"
            "2024-03-17,Venezia,laptop,19,599.99\n"
            "2024-03-17,Torino,TV,10,299.99\n"
            "2024-03-18,Roma,stereo,10,29.99\n"
            "2024-03-18,Milano,auricolari,11,9.99\n"
            "2024-03-18,Napoli,radio,10,19.99\n"
            "2024-03-18,Venezia,smartphone,18,399.99\n"
            "2024-03-18,Torino,laptop,12,599.99\n"
            "2024-03-19,Roma,TV,15,299.99\n"
            "2024-03-19,Milano,stereo,16,29.99\n"
            "2024-03-19,Napoli,auricolari,10,9.99\n"
            "2024-03-19,Venezia,radio,13,19.99\n"
            "2024-03-19,Torino,smartphone,20,399.99\n"
            "2024-03-20,Roma,laptop,10,599.99\n"
            "2024-03-20,Milano,TV,11,299.99\n"
            "2024-03-20,Napoli,stereo,16,29.99\n"
            "2024-03-20,Venezia,auricolari,14,9.99\n"
            "2024-03-20,Torino,radio,10,19.99\n")


# parte 2

df=pd.DataFrame(pd.read_csv("vendite.csv"))
print(f"Primo giorno:\n{df.head()}\nforma:{df.shape}\ninfo:{df.info()}")