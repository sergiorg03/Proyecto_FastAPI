# EventMaster API

Esta API ha sido construida con **FastAPI** para gestionar la venta de entradas de una plataforma de eventos.
Permite administrar recintos y eventos, asegurando que no se supere el aforo permitido al comprar tickets.

## Requisitos

- Python 3.10+
- PostgreSQL
- FastAPI
- SQLAlchemy

## Instalación

1.  Clona este repositorio.
2.  Crea un entorno virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Linux/Mac
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
4.  Configura las variables de entorno creando un archivo `.env` en la raíz del proyecto (ver `example.env`).
    ```env
    DATABASE_URL=postgresql://user:password@host:port/dbname
    ```

## Ejecución

Para iniciar el servidor de desarrollo:
Dentro de la carpeta Eventmaster ejecuta el siguiente comando:
```bash
uvicorn app.main:app --reload
```

La documentación interactiva estará disponible en: http://127.0.0.1:8000/docs

## Despliegue

Este proyecto está configurado para desplegarse en **Railway** usando el archivo `Procfile` incluido.
