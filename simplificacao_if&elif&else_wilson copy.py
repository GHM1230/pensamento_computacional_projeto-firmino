preço_frutas =  {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0,
}

fruta_desejada = 'maçã'

resultado = preço_frutas.get(fruta_desejada)

print(f"O preço da {fruta_desejada} é R${resultado}")

