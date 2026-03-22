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
    cursor.execute("CREATE DATABASE IF NOT EXISTS proyecto_etl")
    conn.close()

    # Ahora conecta a la base de datos creada
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root2025',
        database='proyecto_etl'
    )
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pais(
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        nombre VARCHAR(255) NOT NULL,
                        capital VARCHAR(255) NOT NULL,
                        region VARCHAR(255),
                        poblacion BIGINT);
                    """)
    conn.commit()
    
    insert_query = """
                   insert into pais(nombre,capital,region,poblacion)
                   values(%s,%s,%s,%s)
                   """
    cursor.executemany(insert_query,data)
    conn.commit()
    resultado = cursor.rowcount
    cursor.close()
    conn.close()
    
    return resultado