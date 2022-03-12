import payloads
import argparse

def show_rs(rs, ip, port):
    if   rs == 'python':
        print(payloads.rs_python.format(ip, port))
    elif rs == 'nc':
        print(payloads.rs_netcat.format(ip, port))
    
    else:
        print('[*] parametro invalido')

def show_tty(tipo):
    if tipo == 'python':
        print(payloads.tty_python)
    elif tipo == 'echo':
        print(payloads.tty_echo)
    elif tipo == 'perl':
        print(payloads.tty_perl)
    else:
        print('[*] parametro invalido')

def show_hydra(tipo, wl_users, wl_pass, ip):
    if tipo == 'wordpress':
        print(payloads.hy_wordpress.format(wl_users, wl_pass, ip))
    
    else:
        print('[*] parametro invalido')

def main():

    parser = argparse.ArgumentParser(description="tirica grande")

    parser.add_argument('--tty',  dest='tty')
    parser.add_argument('--rs',   dest='rs')
    parser.add_argument('--ip',   dest='ip')
    parser.add_argument('--port', dest='port')
    
    parser.add_argument('--hydra',  dest='hydra')
    parser.add_argument('--users',   dest='users')
    parser.add_argument('--passwords',   dest='passwords')

    args = parser.parse_args()

    if args.tty:
        tty = args.tty
        show_tty(tty)
    
    elif args.rs:
        if args.ip and args.port:
            rs   = args.rs
            ip   = args.ip
            port = args.port
        
            show_rs(rs, ip, port)
        else:
            print('[+] missing parameters')

    elif args.hydra:
        if args.users and args.passwords and args.ip:
            hy        = args.hydra
            users     = args.users
            passwords = args.passwords
            ip        = args.ip
        
            show_hydra(hy, users, passwords, ip)
        else:
            print('[+] missing parameters')           
    else:
        parser.print_help()

if __name__ == '__main__':
	main()