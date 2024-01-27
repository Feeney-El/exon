import json, shutil

class ActivateSubscribe(object):



    def active_config(self, file_name='config.yaml'):
        self.__move_file(file_name=file_name)


    def download_subs(self, link='', saving_name=''):
        self.__requests_file(link=link, save_file_name=saving_name)

    def __move_file(self, file_name="", file_link=""):
        shutil.copy('./config_yaml/%s' % file_name, './clash_bin/config.yaml')


    def __requests_file(self, link='', save_file_name=''):

        import requests

        subscribe_data = requests.get(link).content
        with open('./config_yaml/%s.yaml' % save_file_name, 'wb') as handler:
            handler.write(subscribe_data)




    
