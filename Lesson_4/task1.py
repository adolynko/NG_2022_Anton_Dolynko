import psutil
import platform

logicvalue = ['n','n','n','n','n']
cpu_freq = psutil.cpu_freq()
logical_cpus = psutil.cpu_count()
cpu_name = platform.processor()
os_name = platform.platform()
RAM = psutil.virtual_memory()
entries = list([str(cpu_freq[2]), str(logical_cpus), cpu_name, os_name, str(RAM[0]) ])
entriesForReading = ["cpu_freq", "logical_cpus", "cpu_name","os_name","RAM(in bytes)"]
def ShowMenu():
    for entry in entries:
        print('[',entries.index(entry),'] / [', logicvalue[entries.index(entry)], ']:', entriesForReading[entries.index(entry)] )
    print(len(entries),'proceed :')

def WriteInTxt():
    info = open('setup.txt', 'a')
    for entry in entries:
        if logicvalue[entries.index(entry)] == 'y':
            info.write(f'{entry}\n')
    info.close()

def main():
    ShowMenu()
    while True:
        print('Choose option')
        data = int(input())
        if data == len(logicvalue):
            break
        if logicvalue[data] == 'n':
            logicvalue[data] = 'y'
        else:
            logicvalue[data] = 'n'
        ShowMenu()   
    print('finished')
    WriteInTxt()

main()
        