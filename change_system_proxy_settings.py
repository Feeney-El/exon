import subprocess

change_proxy_signal = 3

# change ftp settings
if change_proxy_signal == 1:
    subprocess.run(['gsettings'
                       , 'set'
                       , 'org.gnome.system.proxy.ftp'
                       , 'host'
                       , '192.168.18.67'
                    ])
