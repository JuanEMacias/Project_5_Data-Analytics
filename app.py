#Importamos librerias
import pandas as pd 
import plotly.express as px 
import streamlit as st 

#Leemos el conjunto de datos
car_data = pd.read_csv('vehicles_us,csv')

#Añadimos el header 
st.header(' Gráficas para el conjunto de datos de anuncios de venta de coches')

#Creamos las casillas de histogramas 
hist_button1 = st.checkbox('Cronstruir un histograma para la columna model')
hist_button2 = st.checkbox('Cronstruir un histograma para la columna odometer')
hist_button3 = st.checkbox('Cronstruir un histograma para la columna model_year')
hist_button4 = st.checkbox('Cronstruir un histograma para la columna transmission')
hist_button5 = st.checkbox('Cronstruir un histograma para la columna is_4wd')
hist_button6 = st.checkbox('Cronstruir un histograma para la columna condition')

#Creamos las casillas de scatterplots
scatter_button1 = st.checkbox('Construir un gráfico de dispersión para la columna model')
scatter_button2 = st.checkbox('Construir un gráfico de dispersión columna odometer')
scatter_button3 = st.checkbox('Construir un gráfico de dispersión columna model_year')
scatter_button4 = st.checkbox('Construir un gráfico de dispersión columna transmission')
scatter_button5 = st.checkbox('Construir un gráfico de dispersión columna is_4wd')
scatter_button6 = st.checkbox('Construir un gráfico de dispersión condition')

#Creamos las condiciones para creación de histograma de la columa model 
if hist_button1: 
    st.write('Creación de histograma: modelo del vehículo')

    fig = px.histogram(car_data, x='model') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de histograma de la columa odometer
if hist_button2: 
    st.write('Creación de histograma: Kilometraje del vehículo')

    fig = px.histogram(car_data, x='odometer') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de histograma de la columa model_year
if hist_button3: 
    st.write('Creación de histograma año del vehículo')

    fig = px.histogram(car_data, x='model_year') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de histograma de la columa transmission
if hist_button4:
    st.write('Creación de histograma: Transmisión del vehículo')

    fig = px.histogram(car_data, x='transmission')
    
    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de histograma de la columa is_4wd
if hist_button5:
    st.write('Creación de histograma: Tracción del vehículo')
    fig = px.histogram(car_data, x='is_4wd')
    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de histograma de la columa condition
if hist_button6:
    st.write('Creación de histograma: Condición del vehículo')
    fig = px.histogram(car_data, x='condition')
    st.plotly_chart(fig, use_container_width = True)


#Creamos las condiciones para creación de scatterplot de las columas model y price
if scatter_button1:
    st.write('Creación de diagrama de dispersión: Relación precio y modelo')

    fig = px.scatter(car_data, x='model', y='price') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de scatterplot de las columas odometer y price
if scatter_button2:
    st.write('Creación de diagrama de dispersión: Relación precio y km')

    fig = px.scatter(car_data, x='odometer', y='price') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de scatterplot de las columas model_year y price
if scatter_button3:
    st.write('Creación de diagrama de dispersión: Relación precio y año')

    fig = px.scatter(car_data, x='model_year', y='price') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de scatterplot de las columas transmission y price
if scatter_button4:
    st.write('Creación de diagrama de dispersión: Relación precio y transmisión')

    fig = px.scatter(car_data, x='transmission', y='price') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de scatterplot de las columas is_4wd y price
if scatter_button5:
    st.write('Creación de diagrama de dispersión: Relación precio y tracción')

    fig = px.scatter(car_data, x='is_4wd', y='price') 

    st.plotly_chart(fig, use_container_width = True)

#Creamos las condiciones para creación de scatterplot de las columas condition y price
if scatter_button6:
    st.write('Creación de diagrama de dispersión: Relación precio y condición')

    fig = px.scatter(car_data, x='condition', y='price') 

    st.plotly_chart(fig, use_container_width = True)