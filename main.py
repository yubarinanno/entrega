from flask import Flask, jsonify
import fileinput

app = Flask(__name__)

users = []

def process_file():
    with fileinput.input(files=('datos.txt')) as f:
        for line in f:
            if line.startswith("D11") and len(users) < 10:
                dni = line[62:73]
                fechaPago = f"{line[542:544]}{line[544:546]}/{line[546:548]}"
                montoPago = int(line[525:537])
                nombre = line[224:374].strip()

                users.append({ 'dni': dni, 'fechaPago': fechaPago, 'montoPago': montoPago, 'nombre': nombre })

            if len(users) == 10:
                break

process_file()

@app.route('/')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    PORT = 5000  
    app.run(port=PORT)
