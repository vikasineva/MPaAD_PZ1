# Створення словнику для HTTP кодів відповіді (ключ) та їх назв (значення)
with open("HTTP-codes") as file_codes:
    lines_codes = (line.rstrip().split('\t') for line in file_codes)
    dictionary_codes = dict(lines_codes)

# Дописуємо в кожний log назву коду відповіді через пробіл, завдяки створеному словнику
with open("access-log") as file_logs_input, open("access-log-output", 'w') as file_logs_output:
    stripped_lines_logs = (line.rstrip() for line in file_logs_input)
    logs_with_codes = (line + ' ' + dictionary_codes[line.split()[-2]] + '\n' for line in stripped_lines_logs)
    file_logs_output.writelines(logs_with_codes)

# Знаходження максимальної кількості байтів, що було передано при запиті з кодом відповіді OK
with open("access-log-output") as file_logs_output:
    stripped_lines_logs = (line.rstrip() for line in file_logs_output if 'OK' in line)
    byte_column = (line.split(' ')[9] for line in stripped_lines_logs)
    transmitted_bytes = (int(x) for x in byte_column if x != '-')
    print("Максимальна кількість байтів, яку було передано при запиті з кодом відповіді OK:", max(transmitted_bytes))

# Знаходження сумарної кількості байтів, що було передано при запиті файла robots.txt
with open("access-log-output") as file_logs_output:
    stripped_lines_logs = (line.rstrip() for line in file_logs_output if 'robots.txt' in line)
    byte_column = (line.split(' ')[9] for line in stripped_lines_logs)
    transmitted_bytes = (int(x) for x in byte_column if x != '-')
    print("Сумарна кількість байтів, яку було передано при запиті файла robots.txt:", sum(transmitted_bytes))
