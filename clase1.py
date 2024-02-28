panaderia = {
    'panesSalados': {"productos":list([
        {"nombre":"Baguette","valor":3000},
        {"nombre":"Pan de campo", "valor":2500},
        {"nombre":"Pan de centeno","valor":3500},
        {"nombre":"Pan de ajo","valor":1000},
        {"nombre":"Pan de molde integral","valor":3000},
        {"nombre":"Pan de queso","valor":1500},
        {"nombre":"Pan de aceitunas","valor":3000},
        {"nombre":"Bollos de pizza","valor":3500},
        {"nombre":"Pan de cebolla","valor":2000},
        {"nombre":"Pan de maíz","valor":2000}])},
      'panesDulces': {"productos":list([
        {"nombre":"Croissant","valor":3000},
        {"nombre":"Rosca de Reyes","valor":3000},
        {"nombre":"Pan de muerto","valor":3000},
        {"nombre":"Pan de canela","valor":3000},
        {"nombre":"Pan de banana","valor":3000},
        {"nombre":"Pan de zanahoria","valor":3000},
        {"nombre":"Donas","valor":3000},
        {"nombre":"Pan de jengibre","valor":3000},
        {"nombre":"Conchas","valor":3000},
        {"nombre":"Churros","valor":3000}])},
    'postres': {"productos":list([
        {"nombre":"Tarta de manzana","valor":3000},
        {"nombre":"Cupcakes","valor":3000},
        {"nombre":"Galletas decoradas","valor":3000},
        {"nombre":"Pastel de zanahoria","valor":3000},
        {"nombre":"Brownies","valor":3000},
        {"nombre":"Cheesecake","valor":3000},
        {"nombre":"Macarons","valor":3000},
        {"nombre":"Éclairs","valor":3000},
        {"nombre":"Tarta de frutas","valor":3000},
        {"nombre":"Donas","valor":3000}])}
}
print(f"1. Panes Salados")
print(f"2. Panes Dulces")
print(f"3. Postres")
 
categorias_selecionada = input("seleccione el numero de la categoria que desea revisar:")