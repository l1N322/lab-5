#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    glas = set("аеёиоуыэюяaeiou")

    text = input("Введите строку: ").lower()

    count = sum(1 for char in text if char in glas)

    print(count)