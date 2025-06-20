import re
import uuid

def reemplazar_quids(input_path, output_path):
    # Leer contenido del archivo original
    with open(input_path, 'r', encoding='latin-1') as f:
        contenido = f.read()

    contenido = re.sub(r'\bSalida\b', 'Entrada', contenido, flags=re.IGNORECASE)

    # Buscar todos los valores de quid
    quids_originales = set(re.findall(r'quid\s+"([0-9A-F]+)"', contenido, re.IGNORECASE))

    # Generar nuevos quids únicos
    mapa_quids = {quid: uuid.uuid4().hex[:12].upper() for quid in quids_originales}

    # Reemplazar todos los quids antiguos por los nuevos
    for antiguo, nuevo in mapa_quids.items():
        contenido = re.sub(rf'\b{re.escape(antiguo)}\b', nuevo, contenido)

    # Guardar archivo modificado
    with open(output_path, 'w', encoding='latin-1') as f:
        f.write(contenido)

    print(f"✅ Reemplazo completado. Archivo guardado en: {output_path}")
    print(f"🔁 Total de quids reemplazados: {len(mapa_quids)}")

# 🔧 Uso
# Cambia estas rutas por las de tu sistema
input_file = 'zzz.cat'
output_file = 'zzz - mod.cat'

reemplazar_quids(input_file, output_file)
