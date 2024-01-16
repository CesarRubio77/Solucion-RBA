# -*- coding: utf-8 -*-
import psycopg2
from faker import Faker
import random

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

# Reclamos posibles
tipos_reclamo = ['Ninguno', 'Pérdida de paquete', 'Paquete dañado', 'Paquete erróneo']

# Generar y ejecutar consultas SQL para insertar datos ficticios en las tablas clientes y reclamos
for _ in range(5):  # Insertar datos para 5 clientes
    nombre_cliente = fake.name()
    cursor.execute('INSERT INTO "CourierAdmin"."clientes" (nombre) VALUES (%s) RETURNING id', (nombre_cliente,))
    cliente_id = cursor.fetchone()[0]

    # Insertar reclamos para el cliente
    for _ in range(random.randint(0, 3)):  # Cada cliente puede tener 0 a 3 reclamos
        fecha_reclamo = fake.date_this_decade()
        tipo_reclamo = random.choice(tipos_reclamo)

        cursor.execute('INSERT INTO "CourierAdmin"."reclamos" (cliente_id, fecha_reclamo, tipo_reclamo) VALUES (%s, %s, %s)',
                       (cliente_id, fecha_reclamo, tipo_reclamo))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
