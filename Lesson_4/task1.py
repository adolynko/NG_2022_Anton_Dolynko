import psutil
import time

print(1, psutil.cpu_freq())#частота процессора

print(2, psutil.cpu_count(logical=False)) #ядра
print(3 ,psutil.cpu_count(logical=True)) #логические процессоры
################################
print(4, psutil.virtual_memory( ))#оперативная память
print(5, psutil.swap_memory( ))#подкачка
################################
print(6, psutil.disk_partitions(all=False))
print(7, psutil.disk_usage('C:\\'))
print(8, psutil.disk_io_counters( perdisk=False, nowrap=True ))
################################




#psutil.cpu_count