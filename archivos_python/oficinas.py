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

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla oficinas
for _ in range(10):
    direccion = fake.address()[:255]  
    pais = fake.country()[:100]  
    ciudad = fake.city()[:100]  
    director_responsable = fake.name()[:255]  

    query = 'INSERT INTO "CourierAdmin"."oficinas" (direccion, pais, ciudad, director_responsable) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (direccion, pais, ciudad, director_responsable))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
