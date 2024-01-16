# -*- coding: utf-8 -*-
import psycopg2
from faker import Faker

# Configuración de la conexión a la base de datos
db_config = {
    'host': '172.17.0.2',
    'database': 'Admin_CE',
    'user': 'rubio_cesar',
    'password': 'carp123'
}

# Crear una conexión a la base de datos
connection = psycopg2.connect(**db_config)

# Crear un cursor para ejecutar consultas
cursor = connection.cursor()

# Establecer el esquema actual a CourierAdmin
cursor.execute("SET search_path TO CourierAdmin;")

# Crear instancia de Faker
fake = Faker()

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla empleados
for _ in range(10):
    nombre = fake.name()
    correo = fake.email()[:50]
    cargo = fake.random_element(elements=('Gerente', 'Analista', 'Recepcionista'))

    query = 'INSERT INTO "CourierAdmin"."empleados" (nombre, correo, cargo) VALUES (%s, %s, %s)'
    cursor.execute(query, (nombre, correo, cargo))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
