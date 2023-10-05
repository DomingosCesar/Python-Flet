import nmap

class ScanPort:
    def __init__(self, address, port) -> None:
        self.scanner = nmap.PortScanner()
        self.address, self.port = address, port
        
    def Scanning(self):
        return self.scanner.scan(self.address,self.port, arguments='-sS -T4')
    
    def Show_Command(self):
        return self.scanner.command_line()
    
    def Show_Info(self):
        # for host in self.scanner.all_hosts():
        #     print(host.address, host.port)
        return self.scanner.scaninfo()
    

scan = ScanPort("youtube.com", "80")

print(scan.Scanning())
scan.Show_Command()
print(scan.Show_Info())

# import nmap

# subnet = "google.com"
# scanner = nmap.PortScanner()
# scanner.scan(subnet, arguments='-sS -T4')

# print(scanner.scaninfo())
# for host in scanner.all_hosts():
#     print(host.port)

# import requests

# url = "https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAlAmgQ&hl=pt-PT&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S1628230110%3A1695311201923555&theme=glif"
# url2 = "https://accounts.google.com/v3/signin/challenge/pwd?TL=AJeL0C6X26ZBT5IKMFGdLkW2aNoXEUbNGtQFg4_GoEp_fJ0d8L7BcRPfUoVp3xQ6&checkConnection=youtube%3A965%3A0&checkedDomains=youtube&cid=1&continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1628230110%3A1695311201923555&flowEntry=AddSession&flowName=GlifWebSignIn&hl=pt-PT&pstMsg=1&theme=glif&authuser=0"
# payload = {"email": "domingosarmandotavarescesar99@gmail.com", "password": "DomingosCesar@99"} # , "password": "password"

# response = requests.post(url, data=payload)

# if response.status_code == 200:
#     print("Usuário e senha incorretos!")
# else:
#     print("Acesso negado!")

# import nmap

# begin, end, target = 75, 80, '127.0.0.1'
# scanner = nmap.PortScanner()

# for i in range(begin, end + 1):
#     res = scanner.scan(target, str(i))
#     res = res['scan'][target]['tcp'][i]['state']
#     print(f"{i} is {res}")