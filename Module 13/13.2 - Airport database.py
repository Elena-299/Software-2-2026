from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Pyhon',
        autocommit=True
    )

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    sql = """
        SELECT ident, name, municipality
        FROM airport
        WHERE ident = %s
    """
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        response_data = {
            "ICAO": result["ident"],
            "Name": result["name"],
            "Location": result["municipality"]
        }
    else:
        response_data = {
            "error": "Airport not found"
        }
    return response_data

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)