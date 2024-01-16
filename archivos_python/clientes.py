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

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla clientes
for _ in range(10):
    nombre = fake.name()
    
    # Limitar la longitud del correo electrónico a 50 caracteres
    correo_electronico = fake.email()[:50]
    
    pais = fake.country()

    # Limitar la longitud del número de teléfono a 20 caracteres
    numero_telefono = fake.phone_number()[:20]

    query = f'INSERT INTO "CourierAdmin"."clientes" (nombre, correo_electronico, pais, numero_telefono) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (nombre, correo_electronico, pais, numero_telefono))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
