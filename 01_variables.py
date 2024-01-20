#Variables

my_string_variable = "My String variable" # se recomienda variables cortas.
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)


# Aca transforma un int (numero entero) a str (string)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))


my_bool_variable = False
print(my_bool_variable)


# concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable) # mostrar diferentes datos en cadena
print('Este es el valor de:', my_bool_variable)

# Algunas Funciones del Sistema
print(len(my_int_to_str_variable))  #len, cuenta los caracteres incluyendo los espacios

# Variables en una sola linea

name, subname, alias, age = 'Marcos', 'Gimenez', 'migx', 32

sprint("Me llamo:", name, subname,". mi edad es:", age, ". y mi alias es:", alias)
