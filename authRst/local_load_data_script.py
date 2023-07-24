import csv
import mysql.connector
import re

# Conectar ao banco de dados MySQL
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydb'
)
cursor = cnx.cursor()

# Ler o arquivo CSV e inserir os dados no banco de dados
with open('./authRst/local_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        latitude = row['latitude']
        longitude = row['longitude']

        latitude_first_dot_index = latitude.find(".")
        latitude = latitude[:latitude_first_dot_index+1] + latitude[latitude_first_dot_index+1:].replace(".", "")

        longitude_first_dot_index = longitude.find(".")
        longitude = longitude[:longitude_first_dot_index+1] + longitude[longitude_first_dot_index+1:].replace(".", "")

        query = """
            INSERT INTO myapp_local (id, nome, latitude, longitude, bairro, recursos, cidade, estado, cep, foto_url,nota, relevancia, tipo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            int(row['id']),
            row['nome'],
            float(latitude),
            float(longitude),
            row['bairro'],
            row['recursos'],
            row['cidade'],
            row['estado'],
            row['cep'],
            row['foto_url'],
            row['nota'],
            row['relevancia'],
            row['tipo'],

        )
        cursor.execute(query, values)

# Confirmar as alterações no banco de dados
cnx.commit()

# Fechar a conexão com o banco de dados
cursor.close()
cnx.close()
