#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    products = []
    while True:
        product = input("Введите название товара (или 'стоп'): ")
        if product.lower() == 'стоп':
            break
        shop = input("Введите название магазина: ")
        price = float(input("Введите стоимость: "))
        products.append({'товар': product, 'магазин': shop, 'цена': price})

    products.sort(key=lambda item: item.get('магазин', ''))

    print("Все товары:")
    for p in products:
        print(f"{p['магазин']} - {p['товар']} - {p['цена']} руб.")

    search = input("Введите магазин для поиска: ")
    found = [p for p in products if p['магазин'].lower() == search.lower()]

    if found:
        print(f"Товары в магазине '{search}':")
        for p in found:
            print(f"{p['товар']} - {p['цена']} руб.")
    else:
        print(f"Магазин '{search}' не найден.")