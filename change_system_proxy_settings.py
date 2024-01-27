import subprocess

change_proxy_signal = 1

class ChangeSystemProxiesSetting():
    def __init__(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy'
                           , 'mode', 'manual'
                        ])





    def __change_ftp(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.ftp'
                           , 'host', 'localhost'
                        ])

        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.ftp'
                           , 'port', '7890'
                        ])

    def __change_socks(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.socks'
                           , 'host', 'localhost'
                        # , 'port', '8979'
                        ])

        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.socks'
                        # , 'host', 'localhost'
                           , 'port', '7891'
                        ])

    def __change_http(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.http'
                           , 'host', 'localhost'
                        ])

        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.http'
                           , 'port', '7890'
                        ])

    def __change_https(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.https'
                           , 'host', 'localhost'
                        ])

        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy.https'
                           , 'port', '7890'
                        ])



    def run(self):
        self.__change_ftp()
        self.__change_socks()
        self.__change_https()
        self.__change_http()

    def recover(self):
        subprocess.run(['gsettings'
                           , 'set'
                           , 'org.gnome.system.proxy'
                           , 'mode', 'none'
                        ])