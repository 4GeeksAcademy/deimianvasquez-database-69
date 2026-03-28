
-- ==============================================
-- Base de datos de practica
-- Tablas: paises y consolas
-- ==============================================

-- Tabla de paises.
-- nombre: unico y obligatorio.
CREATE TABLE paises (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    description VARCHAR(100) NULL
);

-- Tabla de consolas.
-- fabricante puede ser NULL.
CREATE TABLE consolas(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    fabricante VARCHAR(50) NULL
);

-- Migracion sugerida:
-- Agrega el campo description en paises (100 caracteres, permite NULL).
-- ALTER TABLE paises
-- ADD COLUMN IF NOT EXISTS description VARCHAR(100) NULL;