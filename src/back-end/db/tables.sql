DROP DATABASE IF EXISTS san_marcos;
CREATE DATABASE san_marcos;
USE san_marcos;

CREATE TABLE familiasChile (
  idFamilia INT AUTO_INCREMENT PRIMARY KEY,
  nombreFamilia VARCHAR(255)
);

CREATE TABLE tamanosChile (
  idTamano INT AUTO_INCREMENT PRIMARY KEY,
  nombreTamano VARCHAR(255)
);

CREATE TABLE comprasChiles (
  idCompra INT AUTO_INCREMENT PRIMARY KEY,
  idTamano INT,
  cantidad FLOAT,
  fecha DATE,
  proveedor VARCHAR(255), -- Nullable?
  FOREIGN KEY (idTamano) REFERENCES tamanosChile(idTamano)
);

CREATE TABLE productos (
  sku INT PRIMARY KEY,
  idTamano INT,
  idFamilia INT,
  descripcion VARCHAR(255),
  FOREIGN KEY (idTamano) REFERENCES tamanosChile(idTamano),
  FOREIGN KEY (idFamilia) REFERENCES familiasChile(idFamilia)
);

CREATE TABLE planDeProduccion (
  sku INT,
  fecha DATE,
  cantidad INT,
  PRIMARY KEY (sku, fecha),
  FOREIGN KEY (sku) REFERENCES productos(sku) ON DELETE CASCADE
);