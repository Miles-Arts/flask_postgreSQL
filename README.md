# Aprende Flask desde Cero

Aprende a utilizar el framework web Flask de Python para crear aplicaciones web dinámicas muy fácilmente, conoce cómo usar el framework Flask desde cero.

#python #flask #web

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de carpetas:

```
app/
  app.py                # Archivo principal de la aplicación Flask
  static/               # Archivos estáticos como CSS y JavaScript
    css/
      layout.css        # Estilos de la aplicación
    js/
      layout.js         # Funcionalidades JavaScript
  templates/            # Plantillas HTML
    index.html          # Página principal
    layout.html         # Plantilla base
env/                    # Entorno virtual para dependencias de Python
README.md               # Documentación del proyecto
```

## Entorno Virtual

En este proyecto se utiliza un entorno virtual llamado `env` para gestionar las dependencias de Python. A continuación, se detallan los pasos para configurarlo y activarlo:

1. **Crear el entorno virtual**:
   ```bash
   python -m venv env
   ```

2. **Activar el entorno virtual** (en terminal Bash en Windows):
   ```bash
   source ./env/Scripts/activate
   ```

3. **Instalar las dependencias necesarias**:
   ```bash
   pip install flask
   ```

## Archivos Clave

- **app.py**: Archivo principal donde se configura y ejecuta la aplicación Flask.
- **layout.js**: Archivo JavaScript para funcionalidades dinámicas.
- **layout.css**: Archivo CSS para los estilos de la aplicación.
- **index.html** y **layout.html**: Plantillas HTML para la interfaz de usuario.

## Cómo Ejecutar el Proyecto

1. Asegúrate de tener el entorno virtual activado.
2. Ejecuta el archivo `app.py`:
   ```bash
   python app/app.py
   ```
3. Abre tu navegador y accede a `http://127.0.0.1:5000` para ver la aplicación en funcionamiento.

## Cerrar y Desactivar el Entorno Virtual

Para desactivar el entorno virtual después de usarlo, simplemente ejecuta el siguiente comando:

```bash
deactivate
```

Esto cerrará la conexión al entorno virtual `env` y volverás al entorno global de Python.

## Información Adicional

- **Puerto de la Aplicación**: La aplicación Flask está configurada para ejecutarse en el puerto `5050`. Puedes cambiar este puerto en el archivo `app.py` si es necesario.
- **Modo de Depuración**: El modo de depuración está activado (`debug=True`) para facilitar el desarrollo. Esto permite ver errores detallados en el navegador y recargar automáticamente la aplicación al realizar cambios en el código.
- **Dependencias**: Actualmente, la única dependencia instalada es Flask. Si necesitas instalar más paquetes, asegúrate de hacerlo dentro del entorno virtual con `pip install nombre-paquete`.

---

**Autor:** Milton Figueredo

Gracias a: 

- **Oscar Alejandro Flavio García Fuentes**
  - [YouTube](https://www.youtube.com/watch?v=-1DmVCPB6H8)
  - [GitHub](https://github.com/UskoKruM)

---