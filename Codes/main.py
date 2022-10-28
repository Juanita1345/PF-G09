import streamlit as st
import stream.plotstream as grap
import stream.predict as pred
from datatable import dt, f
import matplotlib.pyplot as plt
import numpy as np
import organizing.data_organize as org
import organizing.plotting as pl
import linear_model.ransac_model as rm
import organizing.cleaningNaN as clean
import linear_model.standarderror as stde
import pandas as pd

link = "../Data/2018_2022_24.csv"
data = org.organize(link, False)
code = ["ATL", "CSG", "ABY", "VLD", "BQK", "SAV", "AGS"]
airports_sigla = ["Atlanta", "Columbus", "Sur Oeste Regional",
                  "Valdosta", "Brunswick Golden", "Savannah/Hilton",
                   "Regional Augusta"]
style = ["Observar modelo","Predecir"]
print(data.head())
estilo = st.sidebar.selectbox("¿Qué desea hacer?", style)
tipo = st.sidebar.selectbox("Seleccione el aeropuerto:", airports_sigla)
data_selected =  org.select_specific(data, f.DEST,
                                     code[airports_sigla.index(tipo)])
if estilo == style[0]:
    st.header("MODELO DEL AEROPUERTO")
    st.header(tipo)
elif estilo == style[1]:
    st.header("PREDICCIÓN DE RETRASO DE ATERIZAJE EN EL AEROPUERTO")
    st.header(tipo)
st.write("Cantidad de datos de",tipo, "es de", data_selected.shape[0], "Datos.")


X, Y = clean.clean(data_selected["DEP_DELAY"].to_list(),
                   data_selected["ARR_DELAY"].to_list())
model = rm.model_linear(X, Y)

while (model.score(X, Y) < 0.9):
    model = rm.model_linear(X, Y)

st.write("La precisión del retraso de vuelo de llegada es del ",
          round(model.score(X, Y)*100,1), "% de las veces.")

berror, merror =  stde.standarderror(X, Y, model)
m = model.estimator_.coef_[0][0]
b = model.estimator_.intercept_[0]
if estilo == style[0]:
    grap.graficar(X,Y,m,merror,b,berror)
elif estilo == style[1]:
    pred.predecir(m,b,merror,berror)
