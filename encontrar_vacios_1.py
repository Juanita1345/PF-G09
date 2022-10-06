import numpy as np
import pandas as pd

def encontrar_vacios_1(data):
    df = data
    b = []

    for i in range(0,len(df.columns)):
        k = df.iloc[:,i]
        k = k.squeeze()
        k = k.astype(str)
        z = k.str.contains(r"\\N").sum()
        b.append(z)

    for i in range(0,len(b)):
        if b[i]>0:
            df.iloc[:,i].replace("\\N",np.nan, inplace = True)
          
    
    return df

