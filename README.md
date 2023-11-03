# Reporting_CSV
Certainly! Here's a description for GitHub in both English and Russian:

### English:

**Project Description for GitHub:**

This project is a Python script that reads data from a CSV file, analyzes it to determine if employees are late for work or leaving early, and records the results in another CSV file. Let's break down the main components and functions of this project:

1. Importing the CSV Library:
   ```python
   import csv
   ```

2. `event` Function:
   - This function takes four parameters: `to_list_add`, `names`, `hour`, and `minute`.
   - `to_list_add` - a list of employee data read from the source CSV file.
   - `names` - the name of the employee for whom you want to check for lateness.
   - `hour` and `minute` - the hour and minute after which lateness will be considered.
   - The function creates a new CSV file with the name `names + '.csv'` and writes a header to it.

   Then, the function iterates through the `to_list_add` list, analyzes the data for each employee, and if the employee meets the specified conditions, it prints information about their lateness and writes this information to the created CSV file.

3. `process_csv_file` Function:
   - This function takes the name of a CSV file (`file_puth`) as a parameter.
   - It opens the specified file and reads its data using the `csv` library.
   - It then converts the read data into a list, `list_add`, which contains information about employees, including name, date, time, place, and status (arrival/departure).
   - It calls the `event` function, passing the `list_add` and other parameters.

4. `main` Function:
   - This is the main function of the script.
   - It sets the name of the CSV file to be processed (`file_puth`) and calls the `process_csv_file` function to start data processing.

5. The `if __name__ == '__main__'` Condition Block:
   - This block checks if the script is run directly (as opposed to being imported as a module), and if so, it calls the `main` function.

The main goal of this project is to analyze data about employee arrivals and departures, calculate lateness if present, and record this information in a new CSV file. Thus, this script can be useful for monitoring employee work hours and identifying cases of lateness.

### Русский:

**Описание проекта для GitHub:**

Этот проект - это Python-скрипт, который считывает данные из CSV-файла, анализирует их, чтобы определить, опаздывают ли сотрудники на работу или уходят раньше, и записывает результаты в другой CSV-файл. Давайте рассмотрим основные компоненты и функции этого проекта:

1. Импорт библиотеки CSV:
   ```python
   import csv
   ```

2. Функция `event`:
   - Эта функция принимает четыре параметра: `to_list_add`, `names`, `hour` и `minute`.
   - `to_list_add` - список данных о сотрудниках, считанных из исходного CSV-файла.
   - `names` - имя сотрудника, для которого нужно проверить опоздания.
   - `hour` и `minute` - час и минута, после которых опоздания будут учитываться.
   - Функция создает новый CSV-файл с именем `names + '.csv'` и записывает в него заголовок.

   Затем функция проходит по списку `to_list_add`, анализирует данные каждого сотрудника и, если сотрудник соответствует заданным условиям, выводит информацию о его опоздании и записывает эту информацию в созданный CSV-файл.

3. Функция `process_csv_file`:
   - Эта функция принимает имя CSV-файла (`file_puth`) как параметр.
   - Открывает указанный файл и считывает его данные с использованием библиотеки `csv`.
   - Затем преобразует считанные данные в список `list_add`, который содержит информацию о сотрудниках, включая имя, дату, время, место и статус (приход/уход).
   - Вызывает функцию `event`, передавая список `list_add` и другие параметры.

4. Функция `main`:
   - Это главная функция скрипта.
   - Здесь устанавливается имя CSV-файла, который нужно обработать (`file_puth`), и вызывается функция `process_csv_file`, чтобы начать обработку данных.

5. Блок условия `if __name__ == '__main__`:
   - Этот блок проверяет, запущен ли скрипт напрямую (а не импортирован как модуль), и, если да, вызывает функцию `main`.

Основная цель этого проекта - анализировать данные о приходе и уходе сотрудников, вычислять опоздания, если они присутствуют, и записывать эту информацию в новый CSV-файл. Таким образом, этот скрипт может быть полезен для мониторинга рабочего времени сотрудников и выявления случаев опоздания.
