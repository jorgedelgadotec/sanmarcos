from flask import Flask, jsonify, request, make_response, send_file
from flask_cors import CORS
from dotenv import load_dotenv
from http import HTTPStatus
from openpyxl import Workbook
from werkzeug.utils import secure_filename
import pandas as pd
import mysql.connector
import os

load_dotenv()

db = mysql.connector.connect(
    host = os.environ.get('HOST'),
    user = os.environ.get('DB_USER'),
    password = os.environ.get('PASSWORD'),
    database = os.environ.get('DATABASE')
)

app = Flask("SanMarcosAPI")
CORS(app, origins=['http://localhost:3000'])

# ✅
@app.route("/ping", methods=["GET"])
def get_ping():
    return jsonify("pong"), HTTPStatus.OK

# ✅
@app.route("/familias", methods=["GET"])
def get_familias():
    query = "SELECT * FROM familiasChile"
    cursor = db.cursor()
    cursor.execute(query)

    familias = [{'id': familia[0], 'familia': familia[1]} for familia in cursor.fetchall()]

    cursor.close()

    return jsonify(familias), HTTPStatus.OK

# ✅
@app.route("/familias", methods=["POST"])
def post_familias():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    nueva_familia = req_data.get("nueva_familia")

    if nueva_familia is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST

    query = "INSERT INTO familiasChile (nombreFamilia) VALUES (%s)"
    cursor = db.cursor()
    cursor.execute(query, (nueva_familia,))
    db.commit()
    cursor.close()

    return  "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/familias", methods=["PATCH"])
def patch_familias():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    id = req_data.get("id")
    nuevo_nombre = req_data.get("nuevo_nombre")

    if id is None or nuevo_nombre is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "UPDATE familiasChile SET nombreFamilia = %s WHERE idFamilia = %s"
    cursor = db.cursor()
    cursor.execute(query, (nuevo_nombre, id))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# 🚫
# TODO: Make it a transaction
@app.route("/familias", methods=["DELETE"])
def delete_familias():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    id = req_data.get("id")

    if id is None :
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "DELETE FROM familiasChile WHERE idFamilia = %s"
    cursor = db.cursor()
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    
    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/tamanos", methods=["GET"])
def get_tamanos():
    query = "SELECT * FROM tamanosChile"
    cursor = db.cursor()
    cursor.execute(query)

    tamanos = [{'id': tamano[0], 'tamano': tamano[1]} for tamano in cursor.fetchall()]

    cursor.close()

    return jsonify(tamanos), HTTPStatus.OK

# ✅
@app.route("/tamanos", methods=["POST"])
def post_tamanos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    nuevo_tamano = req_data.get("nuevo_tamano")

    if nuevo_tamano is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "INSERT INTO tamanosChile (nombreTamano) VALUES (%s)"
    cursor = db.cursor()
    cursor.execute(query, (nuevo_tamano, ))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/tamanos", methods=["PATCH"])
def patch_tamanos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    id = req_data.get("id")
    nuevo_nombre = req_data.get("nuevo_nombre")

    if id is None or nuevo_nombre is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "UPDATE tamanosChile SET nombreTamano = %s WHERE idTamano = %s"
    cursor = db.cursor()
    cursor.execute(query, (nuevo_nombre, id))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# 🚫
# TODO: Make it a transaction
@app.route("/tamanos", methods=["DELETE"])
def delete_tamanos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    id = req_data.get("id")

    if id is None :
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "DELETE FROM tamanosChile WHERE idTamano = %s"
    cursor = db.cursor()
    cursor.execute(query, (id,))
    db.commit()
    cursor.close()
    
    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/productos", methods=["GET"])
def get_productos():
    query = '''SELECT p.sku, p.idTamano, t.nombreTamano, p.idFamilia, f.nombreFamilia, p.descripcion 
        FROM productos p 
        INNER JOIN familiasChile f ON p.idFamilia = f.idFamilia 
        INNER JOIN tamanosChile t ON p.idTamano = t.idTamano'''
    cursor = db.cursor()
    cursor.execute(query)

    productos = [{'sku': producto[0], 'id_tamano': producto[1], 'tamano': producto[2], 'id_familia': producto[3], 'familia': producto[4], 'descripcion': producto[5]} for producto in cursor.fetchall()]

    cursor.close()

    return jsonify(productos), HTTPStatus.OK

# ✅
@app.route("/productos", methods=["POST"])
def post_productos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    sku = req_data.get("sku")
    id_tamano = req_data.get("id_tamano")
    id_familia = req_data.get("id_familia")
    descripcion = req_data.get("descripcion")

    if sku is None or id_tamano is None or id_familia is None or descripcion is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "INSERT INTO productos (sku, idTamano, idFamilia, descripcion) VALUES (%s, %s, %s, %s)"
    cursor = db.cursor()
    
    try:
        cursor.execute(query, (sku, id_tamano, id_familia, descripcion))
        db.commit()
        cursor.close()
        return "", HTTPStatus.NO_CONTENT
    
    except mysql.connector.IntegrityError as err:
        return "Duplicate SKU", HTTPStatus.CONFLICT

# ✅
@app.route("/productos", methods=["PATCH"])
def patch_productos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    sku = req_data.get("sku")
    id_tamano = req_data.get("id_tamano")
    id_familia = req_data.get("id_familia")
    descripcion = req_data.get("descripcion")

    if sku is None or id_tamano is None or id_familia is None or descripcion is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST

    query = '''UPDATE productos 
        SET idTamano = %s, idFamilia = %s, descripcion = %s 
        WHERE sku = %s'''
    cursor = db.cursor()
    cursor.execute(query, (id_tamano, id_familia, descripcion, sku))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/productos", methods=["DELETE"])
def delete_productos():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    sku = req_data.get("sku")

    if sku is None :
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "DELETE FROM productos WHERE sku = %s"
    cursor = db.cursor()
    cursor.execute(query, (sku,))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/compras", methods = ["GET"])
def get_compras():
    query = '''SELECT cc.*, tc.nombreTamano
        FROM comprasChiles cc
        INNER JOIN tamanosChile tc
            ON cc.idTamano = tc.idTamano'''
    
    cursor = db.cursor()
    cursor.execute(query)
    compras = [{
        'id_compra': compra[0],
        'id_tamano': compra[1],
        'cantidad': compra[2],
        'fecha': str(compra[3]),
        'proveedor': compra[4],
        'tamano': compra[5],
    } for compra in cursor.fetchall()]

    return jsonify(compras), HTTPStatus.OK

# ✅
@app.route("/compras", methods = ["POST"])
def post_compras():
    entries = request.json

    if entries is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
        
    if len(entries) == 0:
        return "", HTTPStatus.NO_CONTENT
    
    query = "INSERT INTO comprasChiles (idTamano, cantidad, fecha, proveedor) VALUES "
    values = []
    for entry in entries:
        query += "(%s, %s, STR_TO_DATE(%s, '%Y-%m-%d'), %s),"

        values.append(entry['id_tamano'])
        values.append(entry['cantidad'])
        values.append(entry['fecha'])
        values.append(entry['proveedor'])

    query = query[:-1]
    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/compras", methods = ["PATCH"])
def patch_compras():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    compra = req_data.get('id_compra')
    tamano = req_data.get('id_tamano')
    cantidad = req_data.get('cantidad')
    fecha = req_data.get('fecha')
    proveedor = req_data.get('proveedor')

    if compra is None or tamano is None or cantidad is None or fecha is None or proveedor is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = '''UPDATE comprasChiles
        SET cantidad = %s, idTamano = %s, fecha = STR_TO_DATE(%s, '%Y-%m-%d'), proveedor = %s 
        WHERE idCompra = %s'''

    cursor = db.cursor()
    cursor.execute(query, (cantidad, tamano, fecha, proveedor, compra))
    db.commit()
    cursor.close()
    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/compras", methods = ["DELETE"])
def delete_compras():
    req_data = request.json

    if req_data is None:
        return "No data given", HTTPStatus.BAD_REQUEST
    
    compra = req_data.get('id_compra')

    if compra is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "DELETE FROM comprasChiles WHERE idCompra = %s"
    cursor = db.cursor()
    cursor.execute(query, (compra,))
    db.commit()
    cursor.close()
    
    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/meses_compras")
def get_meses_compras():
    query = "SELECT fecha FROM comprasChiles ORDER BY fecha ASC"
    cursor = db.cursor()
    cursor.execute(query)
    fecha = cursor.fetchall()
    
    fechas = {
        "min": "2024-01-01",
        "max": "2024-12-31"
    }

    if len(fecha) != 0:
        fechas['min'] = "-".join(str(fecha[0][0]).split("-")[:2:]) + "-01"

        query = "SELECT fecha FROM comprasChiles ORDER BY fecha DESC"
        cursor.execute(query)
        fechas['max'] = "-".join(str(cursor.fetchall()[0][0]).split("-")[:2:]) + "-31"
        return jsonify(fechas), HTTPStatus.OK

    return jsonify(fechas), HTTPStatus.OK

# ✅
@app.route("/plan_de_produccion", methods=["GET"])
def get_plan():
    query = '''SELECT pdp.*, p.descripcion, p.idTamano, tc.nombreTamano, p.idFamilia, fc.nombreFamilia
        FROM planDeProduccion pdp
        INNER JOIN productos p ON pdp.sku = p.sku
        INNER JOIN tamanosChile tc on p.idTamano = tc.idTamano
        INNER JOIN familiasChile fc on p.idFamilia = fc.idFamilia'''
    
    cursor = db.cursor()
    cursor.execute(query)

    meses = {
        "01": "enero",
        "02": "febrero",
        "03": "marzo",
        "04": "abril",
        "05": "mayo",
        "06": "junio",
        "07": "julio",
        "08": "agosto",
        "09": "septiembre",
        "10": "octubre",
        "11": "noviembre",
        "12": "diciembre",
    }

    plan = [{
        'sku': p[0],
        'fecha': str(p[1]),
        'cantidad': p[2],
        'descripcion': p[3],
        'id_tamano': p[4],
        'tamano': p[5],
        'id_familia': p[6],
        'familia': p[7],
    } for p in cursor.fetchall()]

    # plan_filtrado = dict()

    # for p in plan:
    #     if p["sku"] in plan_filtrado:
    #         plan_filtrado[p["sku"]]['produccion'][p['fecha'].split("-")[0]][meses[p['fecha'].split("-")[1]]] = p["cantidad"]
    #     else:
    #         plan_filtrado[p["sku"]] = {
    #             'descripcion': p["descripcion"],
    #             'id_familia': p['id_familia'],
    #             'familia': p['familia'],
    #             'id_tamano': p['id_tamano'],
    #             'tamano': p['tamano'],
    #             'sku': p['sku'],
    #             'produccion': {
    #                 p['fecha'].split("-")[0]: {
    #                     meses[p['fecha'].split("-")[1]]: p['cantidad']
    #                 }
    #             }
    #         }

    # plan_guapo = [value for value in plan_filtrado.values()]

    return jsonify(plan), HTTPStatus.OK

# ✅
@app.route("/plan_de_produccion", methods=["POST"])
def post_plan():
    entries = request.json

    if entries is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
        
    if len(entries) == 0:
        return "", HTTPStatus.NO_CONTENT

    query = "INSERT INTO planDeProduccion (sku, fecha, cantidad) VALUES "
    values = []
    for entry in entries:
        values.append(entry["sku"])
        values.append(entry["fecha"] + "-01")
        values.append(entry["cantidad"])

        query += "(%s, STR_TO_DATE(%s, '%Y-%m-%d'), %s),"

    query = query[:-1]

    cursor = db.cursor()
    cursor.execute(query, values)
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/plan_de_produccion", methods=["PATCH"])
def patch_plan():
    req_data = request.json

    if req_data is None:
        return "Missing data", HTTPStatus.BAD_REQUEST
    
    sku = req_data.get("sku")
    fecha = req_data.get("fecha")
    fecha = fecha.split("-")[0] + "-" + fecha.split("-")[1] + "-01"
    nueva_cantidad = req_data.get("cantidad")

    if sku is None or fecha is None or nueva_cantidad is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST

    query = '''UPDATE planDeProduccion
        SET cantidad = %s
        WHERE sku = %s AND fecha = STR_TO_DATE(%s, '%Y-%m-%d')'''
    cursor = db.cursor()
    cursor.execute(query, (nueva_cantidad, sku, fecha))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/plan_de_produccion", methods=["DELETE"])
def delete_plan():
    req_data = request.json

    if req_data is None:
        return "Missing data", HTTPStatus.BAD_REQUEST
    
    sku = req_data.get("sku")
    fecha = req_data.get("fecha")
    fecha = fecha.split("-")[0] + "-" + fecha.split("-")[1] + "-01"

    if sku is None or fecha is None :
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    
    query = "DELETE FROM planDeProduccion WHERE sku = %s AND fecha = STR_TO_DATE(%s, '%Y-%m-%d')"
    cursor = db.cursor()
    cursor.execute(query, (sku, fecha))
    db.commit()
    cursor.close()

    return "", HTTPStatus.NO_CONTENT

# ✅
@app.route("/meses_plan", methods=["GET"])
def get_meses_plan():
    query = "SELECT fecha FROM planDeProduccion ORDER BY fecha ASC"
    cursor = db.cursor()
    cursor.execute(query)
    fecha = cursor.fetchall()

    fechas = {
        "min": "2024-01-01",
        "max": "2024-12-31"
    }

    if len(fecha) != 0:
        fechas["min"] = "-".join(str(fecha[0][0]).split("-")[:2:]) + "-01"

        query = "SELECT fecha FROM planDeProduccion ORDER BY fecha DESC"
        cursor.execute(query)
        fechas['max'] = "-".join(str(cursor.fetchall()[0][0]).split("-")[:2:]) + "-31"
        return jsonify(fechas), HTTPStatus.OK

    return jsonify(fechas), HTTPStatus.OK

# ✅
@app.route("/generate_file", methods=["POST"])
def get_file():
    matrix = request.json
    if matrix is None:
        return "Missing data", HTTPStatus.BAD_REQUEST
    
    wb = Workbook()
    ws = wb.active

    if len(matrix) < 1:
        return "Empty matrix", HTTPStatus.BAD_REQUEST
    
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[0])):
            r = str(row + 1)
            c = chr(column + 65)
            cell = c + r

            ws[cell] = matrix[row][column]

    wb.save("file.xlsx")
    
    return send_file("file.xlsx", as_attachment=True)

# 🚫
# TODO: Implement
@app.route("/load_file", methods=["POST"])
def load_file():
    uploaded_file = request.files.get("file")

    if not uploaded_file:
        return "No file given", HTTPStatus.BAD_REQUEST
    
    filename = secure_filename(uploaded_file.filename)
    path = os.path.join("/Users/jorgedelgado/Chamba/projects/sanMarcosAPI/src/back-end", filename)
    uploaded_file.save(path)

    data = pd.read_excel(path)

    print(1)
    req_data = request.json
    print(2)
    if req_data is None:
        return "Missing field(s)", HTTPStatus.BAD_REQUEST
    print(3)
    table = req_data.get('table')

    if table == "plan":
        print("el plan")
        return "", 200
    elif table == "compras":
        print("las compras")
        return "", 200

if __name__ == "__main__":
    app.run(debug=True, port=8000)