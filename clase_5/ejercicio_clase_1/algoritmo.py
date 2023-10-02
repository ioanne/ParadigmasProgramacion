from productos import (
    ProductoBazar,
    ProductoCarniceria,
    ProductoLimpieza,
)


producto1 = ProductoCarniceria(
    "Carne de res", 10.99, "Filete de primera calidad", 20, "2023-09-30"
)
producto2 = ProductoBazar("Lavaplatos", 2.49, "Botella de 500 ml", 50, "10x10x20 cm")
producto3 = ProductoLimpieza(
    "Detergente", 3.99, "Para lavadoras automáticas", 30, "Fresco de limón"
)


print(producto1.obtener_descripcion())
print(producto2.obtener_precio())
print(producto3.obtener_aroma())
print(producto1.imprimir_informacion())
