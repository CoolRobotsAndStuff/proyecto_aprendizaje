## Predicción de Formula 1 - Instrucciones de Instalación


1. Instalar R version >= 4.5.0. Si la instalación fue exitosa el comando  ```Rscript --version``` debería poder correrse desde la terminal.

2. Instalar python version >= 3.13.5. Se puede checkear con ```python --version```.

3. Clonar este repositorio y entrar al directorio base.

4. Instalar dependencias de R con el siguiente comando:

    ```bash
    Rscript install.R
    ```

5. Correr el servidor con:

    ```bash
    python server.py
    ```

6. Entrar a http://localhost:8000 desde cualquer buscador.


### Entrenar modelo y correr pruebas

Este repositorio ya cuenta con los modelos entrenados. Para entrenarlos nuevamente se deben seguir los pasos anteriores y luego correr:

```bash
Rscript train_generated.R
```

Para probar los modelos ya entrenados y medir la eficiencia correr:

```bash
python test.py
```

> Nota: la inferencia de los modelos se realiza totalmente en R (en el script ```predict_generated.R```). El script test.py simplemente llama al programa en R repetidamente sobre los datos de prueba y utiliza el output que este devuelve para analizar la performance del modelo.

### Obtener nuevos datos

Este repositorio contiene datos de entrenamiento ya descargados. Si, sin embargo, se desea obtener los datos nuevamente, se debe realizar lo siguiente:

1. Instalar dependencias: ```pip install fastf1```

2. Editar el script ```getdata.py``` y seleccionar los años de los que se desea obtener datos.

3. Correr ```python getdata.py```. Este paso obtiene los datos crudos para ser procesados luego. Una vez termine de correr el script debería haber un archivo con el nombre ```f1data_INICIO-FIN.csv``` donde INICIO y FIN son los años de los que se extrajeron los datos.

4. Editar el script ```common.py``` y cambiar la variable "fname" a "f1data_INICIO-FIN", completando los años correspondientes. Esto selecciona qué archivo se usará para preprocesar los datos y luego entrenar el modelo.

5. Correr ```python generate.py```. Este script genera los datos procesados, varios archivos con metadatos útiles para el servidor y tambien los scripts "train_generated.R" y "predict_generated.R" (esto último es necesario para superar limitaciones técnicas del lenguaje R). 

6. Finalmente se puede correr ```Rscript train_generated.R``` para entrenar al modelo con los nuevos datos. Una vez entrenado se puede testear y correr el servidor como se describe en la primera sección.














