# Aplicación web enfocada en la inversión de criptomonedas

Está aplicación web está dedicada a la obtención de diferentes criptomonedas, donde podremos comprarlas, hacer un registro en nuestra base de datos y tener un seguimiento de nuestras inversiones.

# Instrucciones para la instalación de nuestra aplicación web
1. En primer lugar abriremos el programa VISUAL STUDIO donde levantaremos nuestra aplicación en una red local.

2. Abriremos el terminal de dicho programa y crearemos el entorno virtual para ponder montar la aplicación.

```
python -m venv venv
```

3. Activaremos el entorno virtual:
    Si tu ordenador es un MAC
    ```
    . venv/bin/activate
    ```
    Si es un WINDOWS
    ```
    venv\Scripts\activate
    ```

4. Instalaremos todos los requisitos que necesitamos para que funcionen las diferentes paquetes.
```
pip install -r requirements.txt
```

5. Crearemos las variables de entorno. Para ello, duplicaremos el fichero ".env_template", renombraremos a ".env" y dentro del mismo editaremos el contenido de "FLASK_ENV" por "FLASK_ENV=development".

6. Seguidamente, editaremos el archivo "config_template" y lo renombraremos como "config", dentro de este, introduciremos una clave secreta para el token en el apartado "SECRET_KEY" y modificaremos el apartado "APIKEY" introduciendo nuestra clave de la página, siempre dentro de las comillas.

7. Crearemos una carpeta llamada "data" y dentro de ella, un archivo de tipo base de datos con el nombre "Compras.db" según muestra el apartado de "RUTA_DATABASE" del archivo anterior.

8. Por último, crearemos una base de datos según las tablas del archivo "Initial", dentro de la carpeta migrations.

# Ejecución

Para ejecutar nuestra aplicación escribiremos en el terminal `flask run`.