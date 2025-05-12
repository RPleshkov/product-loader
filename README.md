# 🚀 Product-Loader Project Setup

Проект использует [FastStream](https://faststream.airt.ai/latest/), [Docker](https://www.docker.com/), и [uv](https://docs.astral.sh/uv/) — быстрый менеджер зависимостей и Python-окружений.

## 📦 Установка

Следуйте этим шагам для локального развертывания проекта:

### 1. Установка Docker

```bash
curl -sSL https://get.docker.com/ | sh
````

### 2. Установка `uv`

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Установка Python через `uv`

```bash
uv python install 3.12
```

### 4. Установка зависимостей

```bash
uv sync
```

### 5. Подготовка переменных окружения

```bash
cp .env.example .env
```

### 6. Запуск инфраструктуры через Docker Compose

```bash
docker compose up -d
```

### 7. Применение миграций

```bash
alembic upgrade head
```

### 8. Запуск FastStream-приложения

```bash
faststream run src.main:app
```

## 🛠️ Используемые технологии

* **FastStream** — асинхронная система обработки сообщений (NATS, Kafka и др.)
* **SQLAlchemy** + **Alembic** — ORM и миграции
* **Docker Compose** — для локальной инфраструктуры
* **uv** — быстрый менеджер зависимостей и Python-окружений

## 📁 Структура проекта

```text
.
├── alembic/                  # Миграции базы данных
│   ├── versions/             # Файлы версий миграций
│   ├── env.py                # Конфигурация Alembic
│   └── script.py.mako
│
├── src/
│   ├── database/             # Работа с БД
│   │   ├── session.py
│   │   └── models/
│   │       ├── base.py
│   │       ├── product.py
│   │       └── otherinfo.py
│   │
│   ├── handlers/             # Обработчики сообщений
│   │   └── parse_stream.py
│   │
│   ├── config.py             # Настройки проекта
│   ├── schemas.py            # Pydantic-схемы
│   └── main.py               # Точка входа FastStream
│
├── .env.example              # Пример переменных окружения
├── .env                      # Фактические переменные окружения (локально)
├── alembic.ini               # Конфиг Alembic
├── docker-compose.yml        # Docker Compose (PostgreSQL и др.)
├── pyproject.toml            # Зависимости и настройки проекта
├── uv.lock                   # Лок файл зависимостей uv
└── README.md

```

