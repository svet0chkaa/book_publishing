import psycopg2

conn = psycopg2.connect(dbname="student", host="192.168.1.76", user="student", password="root", port="5432")

cursor = conn.cursor()
# for _ in range(7):
#     cursor.execute(f"""UPDATE orders SET processor = '{orders_arr['title']}', ghz = '{}', ram = '{}' WHERE id = '{}';""", 1, 2, 3, 4)

# print(cursor.fetchall())



# UPDATE orders SET ghz = 'value', ram = 'value' WHERE id = 'value';
orders_arr = [
    {'title': 'EL11-SSD-10GE', 'id': 1, 'processor': 'Intel Xeon E-2236', "Ghz": 3.5, "cores": 6, "ram": 32},
    {'title': 'EL42-NVMe', 'id': 2, 'processor': 'Intel Xeon E-2386G', "Ghz": 3.4, "cores": 6, "ram": 32},
    {'title': 'EL13-SSD', 'id': 3, 'processor': 'Intel Xeon E-2236', "Ghz": 3.4, "cores": 6, "ram": 32},
    {'title': 'BL22-NVMe', 'id': 4, 'processor': 'Intel Xeon W-2255', "Ghz": 3.7, "cores": 10, "ram": 128},
    {'title': 'BL21R-NVMe', 'id': 5, 'processor': 'Intel Xeon W-2255', "Ghz": 3.7, "cores": 10, "ram": 256},
    {'title': 'PL25-NVMe', 'id': 6, 'processor': 'Intel Xeon Gold 6354', "Ghz": 3, "cores": 18, "ram": 256},
    {'title': 'PL25-NVMe_1', 'id': 7, 'processor': 'Intel Xeon Gold 6354', "Ghz": 3, "cores": 18, "ram": 254},
]
# orders_arr = [
#     {'title': 'Печать книги', 'id': 1},
#     {'title': 'Брошюрирование', 'id': 2},
#     {'title': 'Дизайн обложки', 'id': 3},
#     {'title': 'Печать постера', 'id': 4},
#     {'title': 'Подарки', 'id': 5},
#     {'title': 'Печать листов', 'id': 6},
#     {'title': 'Написание рецензии', 'id': 7},
# ]
orders_arrs = [
    {'cost': '10000'},
    {'cost': '1500'},
    {'cost': '2500'},
    {'cost': '500'},
    {'cost': '1500'},
    {'cost': '100'},
    {'cost': '15000'},
]
for i in range(7):
    cursor.execute("""SET VALUES orders SET processor = '{}', ghz = '{}', ram = '{}' WHERE id = '{}';""".format(orders_arr[i]["processor"], orders_arr[i]["Ghz"], orders_arr[i]["ram"], i+1) )

for i in range(7):
   cursor.execute("""UPDATE orders SET processor = '{}', ghz = '{}', ram = '{}' WHERE id = '{}';""".format(orders_arr[i]["processor"], orders_arr[i]["Ghz"], orders_arr[i]["ram"], i+1) )
   print("""UPDATE orders SET processor = '{}', ghz = '{}', ram = '{}' WHERE id = '{}';""".format(orders_arr[i]["processor"], orders_arr[i]["Ghz"], orders_arr[i]["ram"], i+1))
for i in range(7):
   cursor.execute("""UPDATE orders SET cost = '{}' where id ={}""".format(orders_arrs[i]["cost"], i+1) )
   print("""UPDATE orders SET cost = '{}' where id ={}""".format(orders_arrs[i]["cost"], i+1))

# print(orders_arr[1]['title'])
conn.commit()   # реальное выполнение команд sql1
 
cursor.close()
conn.close()

