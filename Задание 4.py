#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    dict = {
        1: "apple",
        2: "banana",
        3: "cherry",
        4: "strawberry",
        5: "pineapple",
    }

    print(f"Исходный словарь {dict}")

    dict_items = dict.items()
    print(f"Объект dict_items: {dict_items}")

    swapped = {v: k for k, v in dict_items}

    print(f"Изменённый словарь {swapped}")