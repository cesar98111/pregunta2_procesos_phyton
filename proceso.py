import subprocess
import platform

def windowProccess():
    ip = "8.8.8.8"
    numeroPing = input("introduce el numero de ping\n")
    hola = subprocess.run(["ping","-n", numeroPing, ip], capture_output=True)
    response = hola.stdout

    print(response)
    


def linuxProccess(): 
    ip = "8.8.8.8"
    numeroPing = input("introduce el numer\n")
    hola = subprocess.run(["ping","-c", numeroPing, ip], capture_output=True)
    response = hola.stdout

    print(response)

if __name__ == '__main__':
    plataforma = platform.platform().split("-")
    print(plataforma[0])
    if (plataforma[0] == "Linux"):
        linuxProccess()
    else:
         windowProccess()

