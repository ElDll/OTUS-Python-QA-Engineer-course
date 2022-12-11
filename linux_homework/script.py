import datetime
import subprocess

USERS = set()
ALL_PROCESSES = 0
USERS_PROCESSES = {}
MEMORY_COUNT = 0.0
CPU_COUNT = 0.0
MEMORY_MAX = []
CPU_MAX = []


def read_collection(collection):
    final_string = ""
    if isinstance(collection, dict):
        for key, value in collection.items():
            final_string = final_string + f"{key}: {value}\n"

    if isinstance(collection, set):
        for element in collection:
            final_string = final_string + f"'{element}',"

    return final_string


def init_users(lines):
    for i in range(len(lines)):
        if i == 0:
            continue
        result = list(lines[i].split())
        if i == 1:
            MEMORY_MAX.append(result[10])
            MEMORY_MAX.append(float(result[3]))
            CPU_MAX.append(result[10])
            CPU_MAX.append(float(result[2]))
        USERS.add(result[0])

    for user in USERS:
        USERS_PROCESSES[user] = 0


def report_generator():
    global ALL_PROCESSES, MEMORY_COUNT, CPU_COUNT
    result = subprocess.run(
        args=["ps", "aux"],
        universal_newlines=True,
        stdout=subprocess.PIPE)
    lines = result.stdout.splitlines()

    init_users(lines)

    for line in lines:
        result = list(line.split())
        if result[0] == "USER" or result[0] == "\n":
            continue
        ALL_PROCESSES += 1
        for key in USERS_PROCESSES.keys():
            if key == result[0]:
                USERS_PROCESSES[key] += 1

        MEMORY_COUNT += float(result[3])
        CPU_COUNT += float(result[2])

        if float(result[3]) > MEMORY_MAX[1]:
            MEMORY_MAX[0] = result[10][:20]
            MEMORY_MAX[1] = float(result[3])

        if float(result[2]) > CPU_MAX[1]:
            CPU_MAX[0] = result[10][:20]
            CPU_MAX[1] = float(result[2])

    report = "Отчёт о состоянии системы:\n" \
             f"Пользователи системы: " + read_collection(USERS) + "\n" \
             f"Процессов запущено: {ALL_PROCESSES}\n" \
             "Пользовательских процессов:\n" + \
             read_collection(USERS_PROCESSES) + \
             f"Всего памяти используется: {'%.1f' % MEMORY_COUNT}\n" \
             f"Всего CPU используется: {'%.1f' % CPU_COUNT}\n" \
             f"Больше всего памяти использует: {MEMORY_MAX[0]}\n" \
             f"Больше всего CPU использует: {CPU_MAX[0]}"

    print(report)

    with open(datetime.datetime.now().strftime("%d-%m-%Y-%H:%M") + "-scan.txt", "w") as file:
        file.write(report)


if __name__ == '__main__':
    report_generator()
