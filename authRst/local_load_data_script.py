import csv
import mysql.connector

# Conectar ao banco de dados MySQL
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='FbFb0112*',
    database='mydb'
)
cursor = cnx.cursor()

# Ler o arquivo CSV e inserir os dados no banco de dados
with open('C:/Workspace/django_auth/authRst/local_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        latitude = float(row['latitude'].replace('.', ''))
        longitude = float(row['longitude'].replace('.', ''))
        query = """
            INSERT INTO myapp_local (id, nome, latitude, longitude, bairro, recursos, cidade, estado, cep, foto_url,nota, relevancia, tipo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            int(row['id']),
            row['nome'],
            latitude,
            longitude,
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
