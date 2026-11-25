

# Rutas de Transporte Público API

## ISABELLA LOPEZ RUIZ
## EJERCICIO 12 
##

API desarrollada con FastAPI siguiendo el patrón de Arquitectura por Capas para la gestión de usuarios y del sistema de transporte público.

## Descripción

Este proyecto implementa una API REST utilizando FastAPI, aplicando una arquitectura por capas que separa las responsabilidades en:

- Routes (Rutas)
- Services (Servicios)
- Repositories (Repositorios)
- Models (Modelos)
- Schemas (Esquemas)

La aplicación permite realizar operaciones CRUD sobre los usuarios y la entidad principal del sistema de transporte público.

---

## Arquitectura del Proyecto

```text
Cliente
   │
   ▼
Routes
   │
   ▼
Services
   │
   ▼
Repositories
   │
   ▼
Base de Datos PostgreSQL (Neon)
```

### Responsabilidad de cada capa

#### Routes
Reciben las solicitudes HTTP y envían la información a los servicios.

#### Services
Contienen la lógica de negocio de la aplicación.

#### Repositories
Gestionan las consultas y operaciones sobre la base de datos.

#### Models
Definen la estructura de las tablas en la base de datos.

#### Schemas
Validan la información recibida y enviada por la API.

---

## Estructura del Proyecto

```text
transporte_publico/
│
├── app/
│   ├── database/
│   │   └── conexion.py
│   │
│   ├── models/
│   │   ├── usuario.py
│   │   └── ejercicio.py
│   │
│   ├── repositories/
│   │   ├── usuario_repository.py
│   │   └── ejercicio_repository.py
│   │
│   ├── routes/
│   │   ├── usuarios.py
│   │   └── ejercicio.py
│   │
│   ├── schemas/
│   │   ├── usuario.py
│   │   └── ejercicio.py
│   │
│   └── services/
│       ├── usuario_service.py
│       └── ejercicio_service.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## Tecnologías Utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Neon Database
- Uvicorn
- Render
- GitHub

---



---

## Configuración de la Base de Datos

Crear un archivo `.env` con los datos de conexión a Neon:

```env
DATABASE_URL=postgresql://usuario:password@host/database
```

---

# Ejecutar el Proyecto

```bash
uvicorn main:app --reload
```



## CRUD de Usuarios

Endpoints disponibles:

| Método | Endpoint | Descripción |
|----------|----------|----------|
| GET | /usuarios | Listar usuarios |
| GET | /usuarios/{id} | Obtener usuario |
| POST | /usuarios | Crear usuario |
| PUT | /usuarios/{id} | Actualizar usuario |
| DELETE | /usuarios/{id} | Eliminar usuario |

---

## CRUD Transporte Público

Endpoints disponibles:

| Método | Endpoint | Descripción |
|----------|----------|----------|
| GET | /ejercicio | Listar registros |
| GET | /ejercicio/{id} | Obtener registro |
| POST | /ejercicio | Crear registro |
| PUT | /ejercicio/{id} | Actualizar registro |
| DELETE | /ejercicio/{id} | Eliminar registro |



