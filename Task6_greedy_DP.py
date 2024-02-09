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
    list_strav = []
    
    #print(stravy.values())
    for strava in stravy:
        #print(strava)
        #temp = stravy.values(strava)
        strava_values = stravy.get(strava)
        name = list(strava_values.values())
        #name = list(strava_value())
        #print(name)
        cost = name[0]
        #print(cost)
        count = suma - cost
        if count > 0:
            list_strav.append(strava)
        suma = suma - cost
    return list_strav



def dynamic_programming(stravy, suma):
    pass


if __name__ == "__main__":
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
    }
    total_cost = 100

    print(greedy_algorithm(items, total_cost))
    print(dynamic_programming(items, total_cost))
