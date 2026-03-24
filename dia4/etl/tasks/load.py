import mysql.connector


def load(data):
    resultado = 0
    # Primero, conecta sin especificar la base de datos para crearla si no existe
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root2025'
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS db_g7")
    conn.close()

    # Ahora conecta a la base de datos creada
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root2025',
        database='db_g7'
    )
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS random_users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(255),
                        sexo VARCHAR(10),
                        pais VARCHAR(100),
                        fecha_nac DATE);
                    """)
    conn.commit()
    
    insert_query = """
                   insert into random_users(nombre,sexo,pais,fecha_nac)
                   values(%s,%s,%s,%s)
                   """
    cursor.executemany(insert_query,data)
    conn.commit()
    resultado = cursor.rowcount
    cursor.close()
    conn.close()
    
    return resultado