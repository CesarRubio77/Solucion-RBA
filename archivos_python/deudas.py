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

# Bancos posibles
bancos = ['Banco Pichincha', 'Banco Del Austro', 'Banco Guayaquil', 'Banco Pacifico']

# Tipos de deuda posibles
tipos_deuda = ['Tarjeta de crédito', 'Préstamo personal', 'Hipoteca', 'Otro']

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla deudas
for _ in range(5):  # Insertar datos para 5 deudas
    nombre_banco = random.choice(bancos)
    tipo_deuda = random.choice(tipos_deuda)
    monto_deuda = round(random.uniform(1000, 10000), 2)  # Monto deuda aleatorio entre 1000 y 10000
    fecha_limite = fake.date_this_decade()

    cursor.execute('INSERT INTO "CourierAdmin"."deudas" (nombre_banco, tipo_deuda, monto_deuda, fecha_limite) VALUES (%s, %s, %s, %s)',
                   (nombre_banco, tipo_deuda, monto_deuda, fecha_limite))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
