# Back-end endpoints

## `/familias`

### Methods

#### GET
Regresa todas las familias de chiles registradas

##### Llamada
N/A

##### Respuesta
Se regresa un arreglo que contiene la informacion de todas las familias, cada elemento del arreglo cuenta con la siguiente estructura

| Campo   | Tipo   | Descripcion                    |
| ------- | ------ | ------------------------------ |
| id      | int    | ID de la familia de chiles     |
| familia | string | Nombre de la familia de chiles |

Ejemplo:

```json
[
    {
        "familia": "Jalapeños",
        "id": 1
    },
    {
        "familia": "Rajas verdes",
        "id": 2
    },
    {
        "familia": "Rodajas",
        "id": 3
    }
]
```

#### POST
Agrega una nueva familia de chiles a la BBDD

##### Llamada

| Campo         | Tipo   | Descripcion                          |
| ------------- | ------ | ------------------------------------ |
| nueva_familia | string | Nombre de la nueva familia a agregar |

Ejemplo
```json
{
    "nueva_familia": "Flaming hot"
}
```

##### Respuesta
N/A

#### PATCH
Actualiza el nombre de una familia

##### Llamada

| Campo        | Tipo   | Descripcion                  |
| ------------ | ------ | ---------------------------- |
| id           | int    | ID de la familia a renombrar |
| nuevo_nombre | string | Nuevo nombre de la familia   |

Ejemplo
```json
{
    "id": "1",
    "nuevo_nombre": "Flaming hot"
}
```

##### Respuesta
N/A

#### DELETE
Elimina una familia de chiles y toda la informacion relacionada a esta

##### Llamada

| Campo        | Tipo   | Descripcion                 |
| ------------ | ------ | --------------------------- |
| id           | int    | ID de la familia a eliminar |

Ejemplo
```json
{
    "id": "2"
}
```

##### Respuesta
N/A

## `/tamanos`

### Methods

#### GET
Regresa todos los tamanos de chiles registrados

##### Llamada
N/A

##### Respuesta
Se regresa un arreglo que contiene la informacion de todos los tamanos, cada elemento del arreglo cuenta con la siguiente estructura

| Campo   | Tipo   | Descripcion       |
| ------- | ------ | ----------------- |
| id      | int    | ID del tamano     |
| tamano  | string | Nombre del tamano |

Ejemplo
```json
[
    {
        "id": 1,
        "tamano": "Chico"
    }
]
```

#### POST
Agrega un nuevo tamano de chile

##### Llamada

| Campo        | Tipo   | Descripcion             |
| ------------ | ------ | ----------------------- |
| nuevo_tamano | string | Nombre del nuevo tamano |

Ejemplo
```json
{
    "nuevo_tamano": "Mediano"
}
```

##### Respuesta
N/A

#### PATCH
Actualiza el nombre de un tamano

##### Llamada

| Campo        | Tipo   | Descripcion               |
| ------------ | ------ | ------------------------- |
| id           | int    | ID del tamano a renombrar |
| nuevo_nombre | string | Nombre del nuevo tamano   |

Ejemplo

```json
{
    "id": 1,
    "nuevo_nombre": "Jumbo"
}
```

##### Respuesta
N/A

#### DELETE
Elimina un tamano de chile y todos los registros relacionados

##### Llamada

| Campo        | Tipo   | Descripcion              |
| ------------ | ------ | ------------------------ |
| id           | int    | ID del tamano a eliminar |

Ejemplo

```json
{
    "id": 1
}
```

##### Respuesta
N/A

## `/productos`

### Methods

#### GET
Regresa el listado de todos los productos registrados

##### Llamada
N/A

##### Respuesta
Se regresa un array conteniendo todos los productos, cada uno con la siguiente estructura

| Campo       | Tipo   | Descripcion                       |
| ----------- | ------ | --------------------------------- |
| sku         | int    | ID del producto                   |
| descripcion | string | Nombre del producto               |
| id_familia  | int    | ID de la familia del producto     |
| familia     | int    | Nombre de la familia del producto |
| id_tamano   | int    | ID del tamano del producto        |
| tamano      | int    | Nombre del tamano del producto    |

Ejemplo

```json
[
    {
        "descripcion": "Chiles 2",
        "id_familia": 1,
        "id_tamano": 2,
        "familia": "Jalapeno",
        "tamano": "Mediano",
        "sku": 1000001
    },
    {
        "descripcion": "Chiles 2",
        "id_familia": 2,
        "id_tamano": 2,
        "nombre_familia": "Rajas verdes",
        "nombre_tamano": "Mediano",
        "sku": 1000002
    }
]
```

#### POST
Agrega un producto

##### Llamada

| Campo       | Tipo   | Descripcion                       |
| ----------- | ------ | --------------------------------- |
| sku         | int    | ID del producto a crear           |
| descripcion | string | Nombre del producto               |
| id_familia  | int    | ID de la familia del producto     |
| id_tamano   | int    | ID del tamano del producto        |

Ejemplo

```json
{
    "sku": 1000001,
    "id_tamano": 1,
    "id_familia": 2,
    "descripcion": "Chile chiquito"
}
```
##### Respuesta
N/A

#### PATCH
Corrige los datos de un producto (menos su SKU)

##### Llamada

| Campo       | Tipo   | Descripcion                       |
| ----------- | ------ | --------------------------------- |
| sku         | int    | ID del producto a corregir        |
| descripcion | string | Nombre del producto               |
| id_familia  | int    | ID de la familia del producto     |
| id_tamano   | int    | ID del tamano del producto        |

Ejemplo

```json
{
    "sku": 1000001,
    "id_tamano": 1,
    "id_familia": 2,
    "descripcion": "Chile chiquito"
}
```

##### Respuesta
N/A

#### DELETE
Elimina un producto y todo lo relacionado a este

##### Llamada

| Campo       | Tipo   | Descripcion                       |
| ----------- | ------ | --------------------------------- |
| sku         | int    | ID del producto a eliminar        |

Ejemplo

```json
{
    "sku": 1000001,
}
```

##### Respuesta
N/A


## `/compras`

### Methods

#### GET
Regresa el historial de compras

##### Llamada
N/A

##### Respuesta
Un arreglo que contiene compras, cada una con la siguiente estructura
| Campo     | Tipo   | Descripcion                                |
| --------- | ------ | ------------------------------------------ |
| id_compra | int    | ID de la compra                            |
| id_tamano | int    | ID del tamaño de chile comprado            |
| tamano    | string | Nombre del tamaño                          |
| cantidad  | float  | Cantidad (toneladas) comprada              |
| proveedor | string | Nombre del proveedor                       |
| fecha     | string | Fecha (en formato YYYY-MM-DD) de la compra |

Ejemplo
```json
[
    {
        "cantidad": 420.0,
        "fecha": "2023-02-03",
        "id_compra": 2,
        "id_tamano": 1,
        "proveedor": "Don chile",
        "tamano": "Chico"
    },
    {
        "cantidad": 69.0,
        "fecha": "2023-10-03",
        "id_compra": 3,
        "id_tamano": 2,
        "proveedor": "Chileventas.com",
        "tamano": "Mediano"
    }
]
```

#### POST

##### Llamada
Un arreglo de las compras a registrar
| Campo     | Tipo   | Descripcion                                |
| --------- | ------ | ------------------------------------------ |
| id_tamano | int    | ID del tamaño de chile comprado            |
| cantidad  | float  | Cantidad (toneladas) comprada              |
| proveedor | string | Nombre del proveedor                    |
| fecha     | string | Fecha (en formato YYYY-MM-DD) de la compra |

Ejemplo
```json
[
    {
    "id_tamano": 1,
    "cantidad": 69,
    "fecha": "2024-01-01",
    "proveedor": "Vendedor 1"
    },
    {
    "id_tamano": 2,
    "cantidad": 420,
    "fecha": "2024-01-01",
    "proveedor": "Vendedor 2"
    }
]
```

##### Respuesta
N/A

#### PATCH

##### Llamada
| Campo     | Tipo   | Descripcion                                      |
| --------- | ------ | ------------------------------------------------ |
| id_compra | int    | ID de la compra a editar                         |
| id_tamano | float  | Nuevo ID del tamano comprado                     |
| cantidad  | string | Nueva cantidad de la compra                      |
| fecha     | string | Nueva fecha (en formato YYYY-MM-DD) de la compra |
| proveedor | string | Nuevo nombre del proveedor|

Ejemplo
```json
{
    "id_compra": 1,
    "id_tamano": 420,
    "cantidad": 6969,
    "fecha": "2024-01-02",
    "proveedor": "nuevoschiles.com"
}
```

##### Respuesta
N/A

#### DELETE

##### Llamada
| Campo     | Tipo   | Descripcion              |
| --------- | ------ | ------------------------ |
| id_compra | int    | ID de la compra a borrar |

##### Respuesta
N/A

## `/meses_compras`

* Cualquier metodo (GET de preferencia :D)

### Llamada
N/A

### Respuesta

Ejemplo
- min (string): Primer fecha de compra registrada (YYYY-MM-DD)
- max (string): Ultima fecha de compra registrada (YYYY-MM-DD)

```json
{
    "max": "2024-01-02",
    "min": "2023-02-03"
}
```

## `/plan_de_produccion`

### GET
#### Llamada
N/A

#### Respuesta
Regresa todos los planes (sku + fecha (YYYY-MM)) de produccion registrados

Ejemplo
```json
[
    {
        "cantidad": 69420,
        "descripcion": "Bote jalapeños 215",
        "familia": "Jalapeños",
        "fecha": "2024-02-01",
        "id_familia": 1,
        "id_tamano": 1,
        "sku": 100001,
        "tamano": "Chico"
    }
]
```

### POST
#### Llamada
LA FECHA TIENE QUE SER SOLO YYYY-MM, sin dia

Ejemplo
```json
[
    {
    "sku": 100001,
    "fecha": "2024-04",
    "cantidad": 1234
    },
    {
    "sku": 100001,
    "fecha": "2024-05",
    "cantidad": 1234
    }
]
```

#### Respuesta
N/A

### PATCH
#### Llamada
LA FECHA TIENE QUE SER SOLO YYYY-MM, sin dia

Ejemplo
```json
{
    "sku": 100001,
    "fecha": "2022-02",
    "nueva_cantidad": 777
}
```

#### Respuesta
N/A

### DELETE
#### Llamada
LA FECHA TIENE QUE SER SOLO YYYY-MM, sin dia

Ejemplo
```json
{
    "sku": 100001,
    "fecha": "2022-02",
}
```

#### Respuesta
N/A

## `/meses_plan`

### GET
Regresa el rango de meses disponibles

#### Llamada
N/A

#### Respuesta
Regresa la primer y ultima fecha registradas en el plan de produccion, el dia de la primer fecha se cambia por 01 y el de la ultima por 31

Ejemplo
```json
{
    "max": "2024-02-31",
    "min": "2024-02-01"
}
```

## `GET/generate_file`

Recibe una matriz de datos y genera un archivo .xlsx

### Llamada
Una matriz de datos en formato JSON
Ejemplo
```json
[["Column 1", "Column 2"],
["Value 1", "Value 2"],
["Value 3", "Value 4"]]
```

### Respuesta
Genera un archivo con los datos dados