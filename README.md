<h1 align="center"> Triple Ten Data Analytics: Proyecto Sprint 5 </h1>

### Descripción
***
En este proyecto, se contruye y despliega una aplicación web para obtener fáciemnte gráficas estadísticas de un dataset de venta de coches.
Primero se realizó e la creación de un entorno virtual dentro de conda llamado vehicles_env ys e guardaron los requerimeintos en el archivo requirements.txt 
Se procedió a realizar el análsis exploratorio del dataset el cual se ecuentra en formato .csv, con el nombre de archivo 'vehicle_us.csv'. 
El análsis del proyecto se realizó en un jupyter notebook y puede ser encontrado en el archivo 'EDA.ipynb' dentro de la carpeta notebooks. 
Finalmente se construyó la aplicación web mediante https://dashboard.render.com, esn esta aplicación mediante la selección de datos en las casillas desginadas podremoos observar laabless gráficas que se consideraron más importantes en el análsis exploratorio de datos. 
Dichas gráficas son la distribución (mediante hsitogramas) de las variables de modelo del vehículo, año, condición, registro de kilómetros, transmisión y si cuentan o no con tracción a las 4 ruedas. 
Además se añade una gráfica de dispersión donde observamos como se relacioanan estas varibles con el precio del vehículo. 

## Tecnologías
***
Los recursos utilizados en este proyecto son:
* Python 
* Jupyter Notebooks
* Librerías pandas & plotly express 
## Requerimientos
***
Los requerimientos para este proyecto se encuentran el archivo requirements.txt, donde hallamos los comandos e instalar los recursos necesariso para este proyecto. 
Podemos crear el entorno e instalar los requerimientos medainte el sigueinte comanda en la terminal de anaconda: 
```conda env create --name vehicles_env --file requirements.txt```

## Enlaces
***
A continuación se muestra el enlace a la aplicaión web creada con render: 

