import subprocess

change_proxy_signal = 1

class ChangeSystemProxiesSetting():
    def __init__(self):
        # windows: netsh winhttp set proxy <proxy>:<port>
      pass


   #  def __change_ftp(self):
   #      subprocess.run(['gsettings'
   #                         , 'set'
   #                         , 'org.gnome.system.proxy.ftp'
   #                         , 'host', 'localhost'
   #                      ])

      #   subprocess.run(['gsettings'
      #                      , 'set'
      #                      , 'org.gnome.system.proxy.ftp'
      #                      , 'port', '7890'
      #                   ])

    def __change_socks(self):
        subprocess.run(['netsh'
                           , 'winsock'
                           , 'set'
                           , 'proxy', 'localhost:7891'
                        # , 'port', '8979'
                        ])

     

    def __change_http_and_https(self):
        subprocess.run(['netsh'
                           , 'winhttp'
                           , 'set'
                           , 'proxy', 'localhost:7891'
                        # , 'port', '8979'
                        ])

   #      subprocess.run(['gsettings'
   #                         , 'set'
   #                         , 'org.gnome.system.proxy.http'
   #                         , 'port', '7890'
   #                      ])

   #  def __change_https(self):
   #      subprocess.run(['gsettings'
   #                         , 'set'
   #                         , 'org.gnome.system.proxy.https'
   #                         , 'host', 'localhost'
   #                      ])

   #      subprocess.run(['gsettings'
   #                         , 'set'
   #                         , 'org.gnome.system.proxy.https'
   #                         , 'port', '7890'
   #                      ])



    def run(self):
      #   self.__change_ftp()
        self.__change_socks()
      #   self.__change_https()
        self.__change_http_and_https()

    def recover(self):
        subprocess.run(['netsh'
                           , 'winhttp'
                           , 'reset'
                           , "proxy"
                        ])
        subprocess.run(['netsh'
                           , 'winsock'
                           , 'reset'
                           , "proxy"
                        ])