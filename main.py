import csv

# Функция для анализа данных и записи в CSV-файл
def event(to_list_add, names, hour, minute):
    # Создаем новый CSV-файл с именем 'names + .csv'
    with open(names + '.csv', 'w', newline='') as writecode:
        writer = csv.writer(writecode, delimiter=';')
        # Записываем заголовок в файл
        writer.writerow(['name', 'date', 'time', 'lost_time', 'place', 'check'])

    # Проходим по списку данных о сотрудниках
    for k in to_list_add:
        name = k[0]
        date = k[1]
        time = k[2]
        place = k[3]
        # Определяем, является ли событие приходом или уходом
        check_if = 'Уход' if k[4] == 'Check-out' else 'Приход'
        time = time.split(':')
        # Проверяем условия на опоздание
        if name == names and int(time[0]) >= hour and int(time[1]) >= minute and int(time[0]) < 19:
            print(f"| {name} | "
                  f"{'.'.join(date.split('-'))} | "
                  f"{':'.join(time)} "
                  f"| Опоздание на |{int(time[1]) - minute}| минут |"
                  f" {place} |"
                  f" {check_if} |")

            # Открываем файл для добавления данных
            with open(names + '.csv', 'a') as other_writecode:
                date_date = '.'.join(date.split('-'))
                time_time = ':'.join(time)
                time_lost = int(time[1]) - minute
                writing = csv.writer(other_writecode, delimiter=';')
                # Записываем данные о событии
                writing.writerow([name, date_date, time_time, int(time_lost), place, check_if])

# Функция для обработки CSV-файла
def process_csv_file(file_puth):
    # Открываем указанный CSV-файл для чтения
    with open(file_puth, 'r', newline='') as f:
        reader = csv.DictReader(f)
        list_add = []
        for line in reader:
            name = line['Name']
            time = line['Time'].split()
            place = line['Department']
            data = time[0]
            status = line['Attendance Status']
            base = name, data, time[1], place, status
            # Добавляем данные в список
            list_add.append(list(base))
        # Вызываем функцию event, передавая список данных о сотрудниках
        event(to_list_add=list_add, names='Жылдыз', hour=9, minute=30)

# Функция main - точка входа в программу
def main():
    file_puth = 'input.csv'  # Указываем имя входного CSV-файла
    process_csv_file(file_puth)  # Вызываем функцию для обработки файла

# Проверка, выполняется ли скрипт напрямую
if __name__ == '__main__':
    main()  # Вызываем главную функцию
