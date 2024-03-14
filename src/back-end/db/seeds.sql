USE san_marcos;

INSERT INTO familiasChile (nombreFamilia)
VALUES
('Jalapeños'),
('Rajas verdes'),
('Rodajas');

INSERT INTO tamanosChile (nombreTamano)
VALUES
('Chico'),
('Mediano'),
('Grande');

INSERT INTO productos (sku, idTamano, idFamilia, descripcion)
VALUES
(100001, 1, 1, "Bote jalapeños 215"),
(100010, 1, 1, "Bote jalapeños 380"),
(100003, 3, 1, "Bote jalapeños 2800"),
(100005, 3, 1, "Bote Jalapeño en trozo BS 215"),
(100008, 3, 1, "Bote jalapeños en trozos 215"),
(100011, 3, 1, "Bote jalapeños 780"),
(100012, 1, 2, "Bote rajas verdes 215 - Bajo en sodio"),
(100014, 1, 2, "Bote rajas verdes 105"),
(100015, 1, 2, "Bote rajas verdes 215"),
(100017, 3, 2, "Bote rajas verdes 800"),
(100018, 3, 2, "Bote rajas verdes 2800"),
(100016, 2, 2, "Bote rajas verdes 380"),
(100019, 3, 3, "Frasco rodajas 12 oz lit"),
(100021, 3, 3, "Frasco rodajas 12 oz TD"),
(100023, 3, 3, "Bote rodajas 2800"),
(100024, 3, 3, "Lata rodajas jalapeños bpa free 6lb 10 Oz"),
(100025, 3, 3, "Bote rodajas 215"),
(100026, 3, 3, "Bote rodajas 215 - Bajo en sodio"),
(100027, 3, 3, "Bote rodajas 14 oz"),
(100028, 3, 3, "Bote rodajas 380"),
(100032, 3, 3, "Frasco rodajas 12 oz"),
(100033, 3, 3, "Bote rodajas 800");

INSERT INTO comprasChiles (idTamano, cantidad, fecha, proveedor)
VALUES
(1, 420.0, STR_TO_DATE("2024-01-12", '%Y-%m-%d'), "Don Chiles"),
(2, 69.0, STR_TO_DATE("2024-01-14", '%Y-%m-%d'), "La Morena"),
(2, 777.0, STR_TO_DATE("2024-02-04", '%Y-%m-%d'), "Dan Perez"),
(1, 123.0, STR_TO_DATE("2024-03-10", '%Y-%m-%d'), "Doña Chilena"),
(3, 8383.0, STR_TO_DATE("2024-03-11", '%Y-%m-%d'), "Chiles.com"),
(1, 6.9, STR_TO_DATE("2024-03-12", '%Y-%m-%d'), "Amazon.com");

INSERT INTO planDeProduccion (sku, fecha, cantidad)
VALUES
(100001, STR_TO_DATE("2024-01-01", '%Y-%m-%d'), 6969),
(100001, STR_TO_DATE("2024-02-01", '%Y-%m-%d'), 777),
(100001, STR_TO_DATE("2024-03-01", '%Y-%m-%d'), 1234),
(100001, STR_TO_DATE("2024-04-01", '%Y-%m-%d'), 420),
(100010, STR_TO_DATE("2024-01-01", '%Y-%m-%d'), 6969),
(100010, STR_TO_DATE("2024-02-01", '%Y-%m-%d'), 777),
(100010, STR_TO_DATE("2024-03-01", '%Y-%m-%d'), 1234),
(100010, STR_TO_DATE("2024-04-01", '%Y-%m-%d'), 420);