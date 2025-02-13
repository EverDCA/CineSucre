# Crear un Entorno Virtual en Python

Un entorno virtual en Python permite aislar dependencias de proyectos para evitar conflictos entre ellos. A continuación, se detallan los pasos para crear y activar un entorno virtual en diferentes sistemas operativos.

## 1. Verificar la Instalación de Python
Antes de crear un entorno virtual, asegúrate de que Python está instalado ejecutando:

```sh
python --version
```

Si tienes múltiples versiones de Python, prueba con:

```sh
python3 --version
```

## 2. Crear un Entorno Virtual
Ejecuta el siguiente comando en la terminal o línea de comandos dentro del directorio donde quieres crear el entorno:

```sh
python -m venv .venv
```

Si tienes varias versiones de Python instaladas, usa:

```sh
python3 -m venv .venv
```

Esto creará un directorio llamado `.venv` que contiene una copia aislada de Python y sus herramientas.

## 3. Activar el Entorno Virtual

### En Windows (CMD o PowerShell)

CMD:
```sh
.venv\Scripts\activate
```

PowerShell:
```sh
.venv\Scripts\Activate.ps1
```

### En macOS y Linux

```sh
source .venv/bin/activate
```

Una vez activado, verás el nombre del entorno virtual en el prompt de la terminal.

## 4. Instalar Dependencias

Después de activar el entorno, puedes instalar paquetes con `pip` sin afectar el sistema global:

```sh
pip install nombre_paquete
```

Para instalar múltiples dependencias desde un archivo:

```sh
pip install -r requirements.txt
```

## 5. Desactivar el Entorno Virtual
Para salir del entorno virtual, usa:

```sh
deactivate
```

Esto restaurará la sesión a su estado original.

## 6. Eliminar un Entorno Virtual
Si ya no necesitas el entorno, simplemente elimina la carpeta:

```sh
rm -rf .venv  # macOS y Linux
rmdir /s /q .venv  # Windows
```

---
Siguiendo estos pasos, puedes gestionar fácilmente entornos virtuales en Python para diferentes proyectos.

## 7. Tailwind

### Paso 1
#### npm install -D tailwindcss@3

### Paso 2
#### npx tailwindcss init

### Paso 3
#### Aplicar tailwind config
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["static/templates/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}


### Paso 3
#### npx tailwindcss -i ./static/src/tailwind.css -o ./static/css/main.css --watch