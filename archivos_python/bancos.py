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

# Generar y ejecutar consultas SQL para insertar datos ficticios en la tabla bancos
for _ in range(10):
    nombre_banco = fake.company()
    tipo_cuenta = fake.random_element(elements=('Cuenta corriente', 'Cuenta de ahorros', 'Tarjeta de crédito'))
    numero_cuenta = fake.random_number(digits=10)
    saldo = fake.random.uniform(1000, 10000)

    query = f'INSERT INTO "CourierAdmin"."bancos" (nombre_banco, tipo_cuenta, numero_cuenta, saldo) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (nombre_banco, tipo_cuenta, str(numero_cuenta), saldo))

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar cursor y conexión
cursor.close()
connection.close()
