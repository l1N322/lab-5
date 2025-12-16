#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    school = {
        '1а': 25,
        '1б': 27,
        '2а': 30,
        '2б': 28,
        '6а': 24,
        '7в': 26
    }

    print("Исходные данные:", school)
    print("Общее количество учащихся:", sum(school.values()))

    school['2а'] = 32
    print(f" После изменения в 2а классе: {school}")

    school['8г'] = 29
    print(f" После добавления 8г класса: {school}")

    del school['1б']  # Удаляем класс 1б
    print(f" После удаления 1б класса: {school}")

    sum_students = sum(school.values())
    print(f"Общее количество учащихся в школе: {sum_students}")