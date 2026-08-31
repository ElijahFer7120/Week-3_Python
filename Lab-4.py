"""
Week 3 assignment 1

Purpose:
Shows how a function names repeated logic and makes the code easier to reuse
"""



def calculate_total(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

global_tax_rate = 0.035

prime_changer_mirage = calculate_total(19.21, global_tax_rate)
Metal_Cardbot_BlackHook = calculate_total(39.99, global_tax_rate)
disney_pixar_cars_value = calculate_total(16.99,global_tax_rate)
