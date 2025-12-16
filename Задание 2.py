#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    str1 = set(input("Введите строку: ").lower())
    str2 = set(input("Введите строку: ").lower())

    general = str1.intersection(str2)
    print(general)