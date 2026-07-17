import json

def migrate_interpreters():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    for song in data:
        audio = song.get('audio')
        midi = song.get('midi')
        titulo = song.get('titulo', '').lower()

        # Regla 1: Si solo tiene MIDI (y no tiene audio mp3), interpreter es None/vacío
        if midi and not audio:
            song['interprete'] = None
        # Regla 2: En Señor ten Piedad (Kyrie / Señor ten Piedad en título o tags)
        elif 'kyrie' in titulo or 'señor ten piedad' in titulo or any('señor ten piedad' in t.lower() for t in song.get('tags', [])):
            song['interprete'] = "Magdalena Palomer, Francisca Aguirre, Nicolás Van Wersch, Felipe Rodríguez"
        # Regla 3: En las con link a YouTube (video embed o audio embed o tipo YouTube)
        elif song.get('youtube_video_embed') or song.get('youtube_audio_embed') or song.get('tipo') == 'youtube':
            song['interprete'] = "Coro Misión País"
        # Regla 4: Por defecto "Felipe Rodríguez"
        else:
            song['interprete'] = "Felipe Rodríguez"

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Migración de intérpretes completada con éxito.")

if __name__ == '__main__':
    migrate_interpreters()
