#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
procesar_cantamus_one_shot.py - Ejecucion One-Shot para Cantamus
--------------------------------------------------------------
Permite doble-clic o arrastrar un archivo. Si no se pasa archivo,
toma automaticamente la partitura mas reciente de Downloads o MuseScore Cloud.
Genera el archivo listo y lo resalta en el Explorador de Windows.
"""

import sys
import os
import io
import subprocess
from pathlib import Path



# Agregar directorio scripts al sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from cantamus_pipeline import process_cantamus, get_recent_scores, inspect_score_info


def main():
    print("========================================================")
    print("       CANTAMUS PREPROCESSOR - SINTESIS CORAL AI        ")
    print("========================================================")
    print()

    target_path = None

    if len(sys.argv) > 1 and sys.argv[1] not in ["--help", "-h"]:
        candidate = Path(sys.argv[1].strip('"'))
        if candidate.exists():
            target_path = candidate

    if not target_path:
        print("Buscando partituras recientes en Downloads y MuseScore Cloud...")
        recent = get_recent_scores(limit=1)
        if not recent:
            print("[X] No se encontraron partituras recientes (.musicxml, .mscz, .mxl).")
            print("Por favor exporta tu partitura a Downloads o arrastra el archivo.")
            input("\nPresiona Enter para salir...")
            sys.exit(1)
        target_path = Path(recent[0]["path"])
        print(f"[>] Partitura detectada: {recent[0]['title']} ({recent[0]['source']})")
    else:
        print(f"[>] Archivo recibido: {target_path.name}")

    print(f"    Ruta: {target_path}")
    print()

    # Inspeccionar detalles de la partitura
    print("Analizando partitura...")
    info = inspect_score_info(target_path)
    bpm = info.get("bpm", 71)
    parts = info.get("parts", [])
    print(f"    Titulo: {info.get('title')}")
    print(f"    BPM detectado: {bpm}")
    if parts:
        print(f"    Voces detectadas ({len(parts)}): {', '.join(parts)}")

    print()
    print("Procesando reglas Cantamus (P1..Pn, monofonia, sinalefas, fermatas, BPM baking)...")
    
    try:
        out_file = process_cantamus(
            input_path=target_path,
            initial_bpm=bpm,
            rit_profile="ease-in",
            rit_drop=0.75,
            rit_measures=2,
            keep_accompaniment=False,
            fix_tenor_breathing=True
        )
        print()
        print("--------------------------------------------------------")
        print(f"[OK] Generado con exito:")
        print(f"     {out_file}")
        print("--------------------------------------------------------")
        print("Listo para subir a la web de Cantamus.")
        
        # Abrir el explorador de Windows seleccionando el archivo generado (no bloqueante y con comillas para rutas con espacios)
        try:
            cmd = f'explorer.exe /select,"{out_file}"'
            subprocess.Popen(cmd, shell=True)
        except Exception:
            pass

    except Exception as e:
        print(f"\n[X] Error al procesar: {e}")
        input("\nPresiona Enter para cerrar...")
        sys.exit(1)


if __name__ == "__main__":
    main()
