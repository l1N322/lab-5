#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    products = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            product = input("Введите название товара: ")
            shop = input("Введите название магазина: ")
            price = float(input("Введите стоимость: "))
            products.append({'товар': product, 'магазин': shop, 'цена': price})

            products.sort(key=lambda item: item.get('магазин', ''))

        elif command == 'list':
            print("Все товары:")
            for p in products:
                print(f"{p['магазин']} - {p['товар']} - {p['цена']} руб.")

        elif command == 'search':
            search = input("Введите магазин для поиска: ")
            found = [p for p in products if p['магазин'].lower() == search.lower()]

            if found:
                print(f"Товары в магазине '{search}':")
                for p in found:
                    print(f"{p['товар']} - {p['цена']} руб.")
            else:
                print(f"Магазин '{search}' не найден.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("search - вывести информацию о товарах, продающихся в данном магазине;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)