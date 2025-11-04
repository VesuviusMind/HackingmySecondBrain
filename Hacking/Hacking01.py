#Haking the Second Brain01
#python读写csv
#csv模块是Python内置的用于处理CSV文件的模块。下面是一个简单的示例，演示如何使用csv模块读取和写入CSV文件。
import csv
import random
with open('Hacking01.csv', mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Klaos', 18, 'Berlin'])
    writer.writerow(['Chole', 15, 'Los Angeles'])
    writer.writerow(['Mark', 19, 'Chicago'])
print("CSV Completed:Hacking01.csv")