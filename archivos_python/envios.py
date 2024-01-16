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

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla envios
for _ in range(10):
    tipo_paquete = fake.random_element(elements=('Carta', 'Paquete pequeño', 'Paquete grande'))
    fecha_envio = fake.date_this_decade()
    costo = fake.random.uniform(10, 100)

    query = 'INSERT INTO "CourierAdmin"."envios" (tipo_paquete, fecha_envio, costo) VALUES (%s, %s, %s)'
    cursor.execute(query, (tipo_paquete, fecha_envio, costo))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
