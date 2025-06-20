import unicodedata

def limpiar_texto(texto):
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(
        c for c in texto_normalizado if unicodedata.category(c) != 'Mn'
    )
    texto_final = texto_sin_tildes.replace('ñ', 'n').replace('Ñ', 'N')
    return texto_final

def limpiar_archivo_mdl(archivo_entrada, archivo_salida):
    # Abrir con codificación compatible con archivos generados por Rational Rose
    with open(archivo_entrada, 'r', encoding='latin-1') as f:
        contenido = f.read()

    contenido_limpio = limpiar_texto(contenido)

    # Guardar como UTF-8 para que sea más compatible
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(contenido_limpio)

# Ejemplo de uso
entrada = "Sistema FlowTrack.mdl"
salida = "Sistema FlowTrack - Prueba.mdl"

limpiar_archivo_mdl(entrada, salida)

print(f"Archivo limpio guardado como: {salida}")
