
from flask import Flask, jsonify

app = Flask(__name__)


# Comprobar que la API funciona
@app.get("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "equipment-api"
    })


# Consultar todos los equipos
@app.get("/equipos")
def equipos():
    return jsonify([
        {
            "id": 1,
            "name": "Laptop Dell XPS 15",
            "category": "Computadoras",
            "price": "6500000"
        },
        {
            "id": 2,
            "name": "Monitor LG UltraWide 34\"",
            "category": "Periféricos",
            "price": "1800000"
        },
        {
            "id": 3,
            "name": "Servidor HP ProLiant DL380",
            "category": "Servidores",
            "price": "15000000"
        },
        {
            "id": 4,
            "name": "Teclado Mecánico Keychron K2",
            "category": "Periféricos",
            "price": "450000"
        },
        {
            "id": 5,
            "name": "Mouse Inalámbrico Logitech MX Master 3",
            "category": "Periféricos",
            "price": "480000"
        },
        {
            "id": 6,
            "name": "MacBook Pro M2 14\"",
            "category": "Computadoras",
            "price": "9200000"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
