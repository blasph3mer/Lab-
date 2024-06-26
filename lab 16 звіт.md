Лабораторна робота №16: Розширений список завдань (TODO list) у Python
Мета роботи:
Створення розширеного списку завдань з використанням об'єктно-орієнтованого програмування (ООП) в Python, включаючи функціональність для додавання, видалення, редагування, фільтрації, сортування завдань, а також збереження та завантаження списку з файлу.

Опис завдання:
Клас Task:

Атрибути:
title (str): Назва завдання.
description (str): Опис завдання.
due_date (date): Дата виконання завдання.
status (str): Статус завдання ("Pending", "In Progress", "Completed").
priority (str): Пріоритет завдання ("Low", "Medium", "High").
notes (str): Додаткові нотатки до завдання.
duration (int): Очікувана тривалість виконання завдання у годинах.
recurrence (str): Періодичність завдання ("daily", "weekly", "monthly", або None).
Методи:
is_due_today(): Перевіряє, чи завдання потрібно виконати сьогодні.
to_dict(): Перетворює завдання на словник для збереження у файл.
from_dict(data): Створює завдання зі словника (для завантаження з файлу).
Клас Schedule:

Атрибути:
tasks (list): Список завдань.
history (list): Історія змін завдань.
Методи:
add_task(task): Додає завдання до списку.
remove_task(task_title): Видаляє завдання за назвою.
get_task(task_title): Повертає завдання за назвою.
update_task(task_title, **kwargs): Оновлює атрибути завдання.
list_overdue_tasks(): Повертає список прострочених завдань.
list_tasks_due_today(): Повертає список завдань на сьогодні.
sort_tasks_by_due_date(): Сортує завдання за датою виконання.
weekly_schedule(start_date): Повертає завдання на тиждень, починаючи з start_date.
monthly_schedule(year, month): Повертає завдання на вказаний місяць.
list_tasks_by_priority(priority): Повертає завдання з певним пріоритетом.
save_to_file(filename): Зберігає список завдань у JSON файл.
load_from_file(filename): Завантажує список завдань з JSON файлу.
list_tasks_with_notes(): Повертає завдання, що мають нотатки.
mark_as_completed(task_title): Позначає завдання як виконане.
list_completed_tasks(): Повертає список виконаних завдань.
find_task_by_keyword(keyword): Повертає завдання, що містять ключове слово.
check_deadlines(): Повертає завдання, термін яких закінчується протягом 24 годин.
list_all_tasks(): Повертає всі завдання.
list_tasks_by_duration(min_duration, max_duration): Повертає завдання з тривалістю в заданому діапазоні.
task_history(): Повертає історію змін завдань.
clear_completed_tasks(): Видаляє виконані завдання.
list_recurring_tasks(): Повертає повторювані завдання.
set_reminder(task_title, reminder_date): Встановлює нагадування для завдання.
completion_percentage(): Обчислює відсоток виконаних завдань.
Виконання роботи:
Створення об'єктів:

Створено об'єкти класу Task з різними параметрами.
Створено об'єкт класу Schedule.
Додавання завдань:

Використано метод add_task() для додавання завдань до розкладу.
Операції з завданнями:

Виконано різні операції над завданнями, такі як оновлення, позначення як виконаних, пошук за ключовим словом тощо.
Збереження та завантаження:

Збережено розклад у файл schedule.txt.
Завантажено розклад з файлу.
Висновки:
У цій лабораторній роботі було успішно реалізовано розширений список завдань з використанням ООП в Python. Було створено класи Task та Schedule, реалізовано методи для керування завданнями та їх атрибутами, а також забезпечено збереження та завантаження даних у файл. Код відповідає вимогам завдання та демонструє розуміння принципів ООП.
