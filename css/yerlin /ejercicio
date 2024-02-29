def mostrar_menu(menu):
   print("Menú: panes")


   for categoria, productos in menu.items():
       print(f"{categoria}:")
       for producto, precio in productos.items():
           print(f"   - {producto}: ${precio}")


def hacer_compra(menu, categoria_elegida):
   total = 0
   seleccion = None
   while seleccion != 'fin':
       mostrar_menu({categoria_elegida: menu[categoria_elegida]})
       seleccion = input("Por favor, selecciona el producto que deseas comprar (o escribe 'fin' para terminar): ")
       if seleccion.lower() == 'fin':
           break
       encontrado = False
       for producto, precio in menu[categoria_elegida].items():
           if seleccion in producto:
               total += precio
               print(f"Producto seleccionado: {producto} - Precio: ${precio}")
               encontrado = True
               break
       if not encontrado:
           print("Lo siento, ese producto no está en el menú.")


   print(f"Total a pagar: ${total}")


menu = {
   "Panes": {
       "1.Pan salado": 1000,
       "2.Pan de queso": 5000,
       "3.Pan de centeno": 9000,
       "4.Pan de cebada": 6000,
       "5.Pan de avena": 7000,
       "6.Pan de maíz": 4000,
       "7.Pan de soja": 5000,
       "8.Pan de espelta": 7000,
       "9.Pan de arroz": 7000
   },


   "Pasteles": {
       "1.Tarta de chocolate": 4000,
       "2.Pastel de zanahoria": 6000,
       "3.Cheesecake de fresa": 7000,
       "4.Bizcocho de limón": 8000,
       "5.Tarta de manzana": 6000,
       "6.Red Velvet": 4000,
       "7.Mousse de chocolate": 5000,
       "8.Pastel de tres leches": 9000,
       "9.Tiramisú": 6000,
       "10.Selva negra": 7000,
   },


   "Galletas": {
       "1.Galletas de chocolate chip": 7000,
       "2.Galletas de avena y pasas": 7000,
       "3.Galletas de mantequilla": 7000,
       "4.Galletas de jengibre": 5000,
       "5.Galletas de mantequilla de cacahuete": 4000,
       "6.Galletas de almendra": 5000,
       "7.Galletas de azúcar": 6000,
       "8.Galletas de chispas de caramelo": 4000,
       "9.Galletas de coco": 9000,
       "10.Galletas de canela": 1000,
   }
}

print("""
 _____  _                                   _      _                                           _                                                    _                    
| ___ \(_)                                 (_)    | |                                         | |                                                  | |                   
| |_/ / _   ___  _ __  __   __  ___  _ __   _   __| |  ___     __ _   _ __   _   _   ___  ___ | |_  _ __   __ _     _ __    __ _  _ __    __ _   __| |  ___  _ __   __ _ 
| ___ \| | / _ \| '_ \ \ \ / / / _ \| '_ \ | | / _` | / _ \   / _` | | '_ \ | | | | / _ \/ __|| __|| '__| / _` |   | '_ \  / _` || '_ \  / _` | / _` | / _ \| '__| / _` |
| |_/ /| ||  __/| | | | \ V / |  __/| | | || || (_| || (_) | | (_| | | | | || |_| ||  __/\__ \| |_ | |   | (_| |   | |_) || (_| || | | || (_| || (_| ||  __/| |   | (_| |
\____/ |_| \___||_| |_|  \_/   \___||_| |_||_| \__,_| \___/   \__,_| |_| |_| \__,_| \___||___/ \__||_|    \__,_|   | .__/  \__,_||_| |_| \__,_| \__,_| \___||_|    \__,_|
                                                                                                                   | |                                                   
   """)              
print("Por favor, seleccione la opción válida:")
print("1. Panes")
print("2. Pasteles")
print("3. Galletas")


categoria_elegida = input("Por favor, elige el número correspondiente a la categoría que deseas comprar  : ")


if categoria_elegida == '1':
   categoria_elegida = "Panes"
elif categoria_elegida == '2':
   categoria_elegida = "Pasteles"
elif categoria_elegida == '3':
   categoria_elegida = "Galletas"
else:
   print("La opción seleccionada no es válida.")


if categoria_elegida:
   hacer_compra(menu, categoria_elegida)









