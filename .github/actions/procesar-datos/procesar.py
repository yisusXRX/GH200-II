import os
import sys
from pathlib import Path

entorno = sys.argv[1] if len(sys.argv) > 1 else "staging"

# Crear carpeta y archivo de salida para subir como artefacto
out_dir = Path("reporte")
out_dir.mkdir(exist_ok=True)
reporte_file = out_dir / "resumen.txt"
reporte_file.write_text(f"Reporte generado en Python para el entorno: {entorno}\n", encoding="utf-8")

# Exponer un output para el workflow usando GITHUB_OUTPUT
github_output = os.environ.get("GITHUB_OUTPUT")
resumen_msg = f"Procesado ok en {entorno}"

if github_output:
    with open(github_output, "a", encoding="utf-8") as f:
        f.write(f"resumen={resumen_msg}\n")

print(resumen_msg)