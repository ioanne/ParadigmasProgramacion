from bar import SucursalBar
from bebidas import Gaseosa, Trago, Vino
from menu import Menu
from tipo_bebida import TipoBebida


tipo_vino = TipoBebida("Vino")
tipo_trago = TipoBebida("Trago")
tipo_gaseosa = TipoBebida("Gaseosa")


vino1 = Vino("Vino Tinto", 30.0, "Cabernet Sauvignon")
trago1 = Trago("Margarita", 10.0, [vino1, Gaseosa("Sprite", 2.5, "Lima y Limón")])
gaseosa1 = Gaseosa("Cola", 2.5, "Cola")


sucursal_cholulo = SucursalBar("BarCholulo")
sucursal_cheto = SucursalBar("BarCheto")


sucursal_cholulo.agregar_bebida(vino1)
sucursal_cholulo.agregar_bebida(trago1)
sucursal_cheto.agregar_bebida(gaseosa1)


menu = Menu()
menu.agregar_bebida(vino1)
menu.agregar_bebida(trago1)
menu.agregar_bebida(gaseosa1)


sucursal_cholulo.mostrar_menu()
sucursal_cheto.mostrar_menu()
menu.mostrar_menu()


print(sucursal_cholulo.recibir_reserva("Cliente 1", "2023-09-30"))
print(sucursal_cholulo.realizar_pedido(vino1, 3))
print(menu.buscar_bebida("Vino Tinto"))
