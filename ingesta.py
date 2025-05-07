import pymysql
import csv
import boto3

conn = pymysql.connect(
    host="tu-host",
    user="tu-usuario",
    password="tu-contraseña",
    database="tu-base-datos"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM tu_tabla")

ficheroUpload = "data.csv"
with open(ficheroUpload, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([desc[0] for desc in cursor.description])
    writer.writerows(cursor.fetchall())

cursor.close()
conn.close()

nombreBucket = "gfc-output-01"
s3 = boto3.client("s3")
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada y archivo subido correctamente a S3")