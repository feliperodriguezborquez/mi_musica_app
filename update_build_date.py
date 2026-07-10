import datetime

def update_date():
    now = datetime.datetime.now()
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    date_str = f"{now.day} de {meses[now.month - 1]} de {now.year}"
    
    with open('build_date.txt', 'w', encoding='utf-8') as f:
        f.write(date_str)
    print(f"build_date.txt actualizado con: {date_str}")

if __name__ == '__main__':
    update_date()
