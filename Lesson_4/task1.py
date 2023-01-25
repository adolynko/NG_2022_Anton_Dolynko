import psutil
import platform

cpu_freq = psutil.cpu_freq()
logical_cpus = psutil.cpu_count()
cpu_name = platform.processor()
os_name = platform.platform()
RAM = psutil.virtual_memory()
entries = list([str(cpu_freq[2]), str(logical_cpus), cpu_name, os_name, str(RAM[0]) ])
entriesForReading = ["cpu_freq", "logical_cpus", "cpu_name","os_name","RAM(in bytes)"]

def logicalToStrConverter(logic):
    return "y" if logic else "n"

def showMenu(modes):
    for entry in entries:
        print("[" + str(entries.index(entry)) + "] / [ " + logicalToStrConverter(modes[entry]) + " ]: " + str(entriesForReading[entries.index(entry)]))
    print("["+ str(len(entries)) + "]: Proceed")

def getUserChoice(modes):
    showMenu(modes)
    return int(input("Choose the option "))

def buildModes():
    modes = {}
    for entry in entries:
        modes[entry] = False
    return modes

def startManager():
    modes = buildModes()
    while True:
        choice = getUserChoice(modes)
        if choice == len(entries):
            break
        else:
            modes[entries[choice]] = not modes[entries[choice]]
    writeInTxt(modes)

def writeInTxt(modes):
    info = open("info.txt","w")
    for values in modes:
        if logicalToStrConverter(modes[values]) == "y":
            info.write(f'{values}\n')

startManager()