# Minecraft Game

Este proyecto es un juego inspirado en Minecraft, donde los jugadores pueden explorar un mundo generado, moverse, saltar, correr, y colocar o romper bloques.

## Estructura del Proyecto

- **src/main.py**: Punto de entrada del juego. Inicializa la ventana y gestiona la lógica del juego.
- **src/terrain.py**: Define la clase `Terrain` para generar y renderizar el terreno.
- **src/player.py**: Define la clase `Player` para manejar las acciones del jugador.
- **src/blocks.py**: Define las clases `Block` y sus subclases para diferentes tipos de bloques.
- **src/utils/__init__.py**: Contiene funciones utilitarias para el proyecto.
- **requirements.txt**: Lista las dependencias necesarias.

## Instalación

1. Clona el repositorio:
   ```
   git clone <URL_DEL_REPOSITORIO>
   cd minecraft-game
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el juego, utiliza el siguiente comando:
```
python src/main.py
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.