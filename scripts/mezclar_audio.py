#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mezclar_audio.py - Mezclador Profesional de Voces Cantāmus + Instrumental MuseSounds
-----------------------------------------------------------------------------------
Combina las voces sintetizadas por Cantāmus (IA) con el acompañamiento instrumental
generado en MuseScore 4 con MuseSounds (máxima fidelidad orquestal/acústica):

- Alineación temporal milimétrica (offset en milisegundos).
- Balance de ganancia vocal (+dB) para claridad e inteligibilidad del texto lírico.
- Nivelación y masterización suave con normalización de picos (-0.5 dBFS).
- Exportación en MP3 de alta fidelidad (320 kbps) o WAV.
"""

import sys
import os
import io
import math
from pathlib import Path

# Consola UTF-8 segura
if sys.platform == "win32":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
    except Exception:
        pass

from pydub import AudioSegment
from pydub.effects import normalize as pydub_normalize


def mezclar_cantamus_musesounds(
    vocal_path,
    instrumental_path,
    output_path=None,
    vocal_gain_db=2.5,
    vocal_delay_ms=0,
    instrumental_gain_db=0.0,
    fade_out_ms=1500,
    target_peak_db=-0.5
):
    """
    Mezcla una pista vocal de Cantāmus con una pista instrumental de MuseSounds.

    Parámetros:
      vocal_path: Ruta al archivo de audio de voces (MP3, WAV, M4A)
      instrumental_path: Ruta al audio instrumental de MuseScore MuseSounds
      output_path: Ruta de salida (si es None, añade '_Master_Completo.mp3')
      vocal_gain_db: Realce de volumen vocal en decibelios (recomendado: +2.0 a +3.5 dB)
      vocal_delay_ms: Desplazamiento de las voces en ms (+ adelanta/atrasa para sincro exacta)
      instrumental_gain_db: Ajuste de volumen instrumental
      fade_out_ms: Duración del fundido final suave
      target_peak_db: Techo de volumen máximo para evitar saturación digital
    """
    vocal_path = Path(vocal_path)
    instrumental_path = Path(instrumental_path)

    if not vocal_path.exists():
        raise FileNotFoundError(f"Archivo de voces no encontrado: {vocal_path}")
    if not instrumental_path.exists():
        raise FileNotFoundError(f"Archivo instrumental no encontrado: {instrumental_path}")

    if output_path is None:
        output_path = vocal_path.parent / f"{vocal_path.stem}_Master_Completo.mp3"
    else:
        output_path = Path(output_path)

    print(f"[>] Cargando pista vocal: {vocal_path.name}")
    voces = AudioSegment.from_file(str(vocal_path))

    print(f"[>] Cargando pista instrumental: {instrumental_path.name}")
    instrumental = AudioSegment.from_file(str(instrumental_path))

    # Asegurar coincidencia de canales y sample rate
    if voces.channels != instrumental.channels:
        if instrumental.channels == 2:
            voces = voces.set_channels(2)
        else:
            instrumental = instrumental.set_channels(voces.channels)

    if voces.frame_rate != instrumental.frame_rate:
        target_sr = max(voces.frame_rate, instrumental.frame_rate)
        voces = voces.set_frame_rate(target_sr)
        instrumental = instrumental.set_frame_rate(target_sr)

    # Aplicar ganancia a las pistas
    if vocal_gain_db != 0:
        voces = voces + vocal_gain_db
    if instrumental_gain_db != 0:
        instrumental = instrumental + instrumental_gain_db

    # Ajuste de retraso o adelanto en voces
    if vocal_delay_ms > 0:
        silencio = AudioSegment.silent(duration=vocal_delay_ms, frame_rate=voces.frame_rate)
        voces = silencio + voces
    elif vocal_delay_ms < 0:
        trim_ms = abs(vocal_delay_ms)
        voces = voces[trim_ms:]

    # Alinear duración: la mezcla toma la duración de la pista más larga
    max_len = max(len(voces), len(instrumental))
    base = AudioSegment.silent(duration=max_len, frame_rate=voces.frame_rate)
    if instrumental.channels == 2:
        base = base.set_channels(2)

    # Superponer pistas sobre la base silenciosa
    mezcla = base.overlay(instrumental, position=0)
    mezcla = mezcla.overlay(voces, position=0)

    # Fundido final suave (Fade Out)
    if fade_out_ms > 0 and len(mezcla) > fade_out_ms:
        mezcla = mezcla.fade_out(duration=fade_out_ms)

    # Masterización suave: normalización de volumen
    print("[>] Aplicando masterización y normalización de picos...")
    mezcla = pydub_normalize(mezcla, headroom=abs(target_peak_db))

    # Exportar con alta fidelidad
    print(f"[>] Guardando mezcla final en: {output_path}")
    ext = output_path.suffix.lower().replace(".", "")
    if ext == "wav":
        mezcla.export(str(output_path), format="wav")
    else:
        mezcla.export(str(output_path), format="mp3", bitrate="320k")

    print(f"[OK] ¡Canción completa generada exitosamente! -> {output_path}")
    return output_path


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso:")
        print("  python mezclar_audio.py <audio_voces> <audio_instrumental> [audio_salida] [vocal_gain_db] [delay_ms]")
        print("Ejemplo:")
        print("  python mezclar_audio.py voces_cantamus.mp3 instrumental_musescore.mp3 cancion_final.mp3 3.0 0")
        sys.exit(1)

    voces_f = sys.argv[1]
    inst_f = sys.argv[2]
    out_f = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].replace(".", "").replace("-", "").isdigit() else None
    
    rest = sys.argv[3:] if out_f is None else sys.argv[4:]
    gain = float(rest[0]) if len(rest) > 0 else 2.5
    delay = int(rest[1]) if len(rest) > 1 else 0

    mezclar_cantamus_musesounds(voces_f, inst_f, out_f, vocal_gain_db=gain, vocal_delay_ms=delay)
