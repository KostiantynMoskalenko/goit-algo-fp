"""
Необхідно написати програму на Python, яка використовує два підходи —
жадібний алгоритм та алгоритм динамічного програмування для розв’язання
задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого
бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені
у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю
та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви,
максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію
dynamic_programming, яка обчислює оптимальний набір страв для максимізації
калорійності при заданому бюджеті.
"""


def greedy_algorithm(stravy, suma):
    dict_key_and_ratio = {}
    # Порахуємо відношення калорій до вартості для страв та додамо в словник
    for key, value in stravy.items():
        ratio = 0
        for inner_key, inner_value in value.items():
            if ratio == 0:
                ratio = inner_value
            else:
                # Та створимо словник з цими даними
                ratio = inner_value/ratio
                dict_key_and_ratio[key] = ratio
                ratio = 0
    # Зробимо сортування за спаданням по співвідношенню калорій до вартості
    list_sorted_ratio = sorted(dict_key_and_ratio.items(), key=lambda x: x[1],
                               reverse=True)
    dict_sorted_ratio = dict(list_sorted_ratio)
    # Роздрукуємо найменування страв з їх пріорітетами
    print(dict_sorted_ratio)
    # Відберемо страви жадібним алгоритмом за відношенням калорій до вартості
    spysok_strav = {}
    for key, value in dict_sorted_ratio.items():
        current_strava = stravy[key]
        cost = current_strava.get("cost")
        count = suma // cost
        if count > 0:
            spysok_strav[key] = count
        suma = suma - cost*count

    return spysok_strav


def dynamic_programming(stravy, suma):
    dict_key_and_ratio = {}
    # Порахуємо відношення калорій до вартості для страв та додамо в словник
    for key, value in stravy.items():
        ratio = 0
        for inner_key, inner_value in value.items():
            if ratio == 0:
                ratio = inner_value
            else:
                # Та створимо словник з цими даними
                ratio = inner_value/ratio
                dict_key_and_ratio[key] = ratio
                ratio = 0
    # Зробимо сортування за спаданням по співвідношенню калорій до вартості
    list_sorted_ratio = sorted(dict_key_and_ratio.items(), key=lambda x: x[1],
                               reverse=True)
    dict_sorted_ratio = dict(list_sorted_ratio)
    # Відберемо страви алгоритмом динамічного програмування
    spysok_strav = {}
    min_strav_req = [0] + [float("inf")] * suma
    last_strava_usage = [0] * (suma + 1)
    for s in range(1, suma + 1):
        for key, value in dict_sorted_ratio.items():
            current_strava = stravy[key]
            cost = current_strava.get("cost")
            if s >= cost and min_strav_req[s - cost] + 1 < min_strav_req[s]:
                min_strav_req[s] = min_strav_req[s - suma] + 1
                last_strava_usage[s] = cost
    current_sum = suma
    while current_sum > 0:
        #cost = last_strava_usage[current_sum]
        spysok_strav[key] = spysok_strav.get(key, 0) + 1
        current_sum = current_sum - cost
    return spysok_strav


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
        }
    total_cost = 80

    print("Страви і їх кількість при використанні жадібного алгоритму",
          greedy_algorithm(items, total_cost))
    print("Страви і їх кількість при використанні динамічного програмування",
          dynamic_programming(items, total_cost))
