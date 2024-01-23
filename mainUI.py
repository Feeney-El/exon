import sys, clash_restful, proxies_json_reader, os, time, json
from PyQt5 import QtCore, QtGui, QtWebSockets, QtNetwork
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QTableView,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTextBrowser,
    QCheckBox,
    QComboBox,
    QMenu,
    QStackedLayout
)


class Window(QWidget):
    def __init__(self):

        # if os.path.exists('file.txt'):
            # os.remove('file.txt')
        # self.start_log()

        super().__init__()
        self.setWindowTitle("PyV2clash")
        global_layout = QHBoxLayout()
        self.setLayout(global_layout)

        list_layout = QVBoxLayout()
        global_layout.addLayout(list_layout)

        button_layout = QVBoxLayout()
        global_layout.addLayout(button_layout)

        self.providers_combo_box = QComboBox()

        self.run_button = QPushButton(text="Run")
        self.run_button.setFixedSize(190, 60)
        self.setting_button = QPushButton(text="设置")
        self.setting_button.setFixedSize(190, 60)
        self.all_server_speed_button = QPushButton(text="全部节点测速")
        self.all_server_speed_button.setFixedSize(190, 60)
        self.logs_button = QPushButton(text="日志")
        self.logs_button.setFixedSize(190, 60)


        self.providers_combo_box.addItems(proxies_json_reader.get_providers_name())
        self.provider_combo_box_current_text = str(self.providers_combo_box.currentText())
        # servers_show_in_Qlist = proxies_json_reader.get_server_list_in_provider_group(provider_combo_box_current_text)

        list_layout.addWidget(self.providers_combo_box)
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.setting_button)

        button_layout.addWidget(self.logs_button)
        self.logs_button.clicked.connect(self.logs_window)






        button_layout.addWidget(self.all_server_speed_button)
        self.setting_button.clicked.connect(self.setting_window)

        self.servers_list = QListWidget()
        self.providers_combo_box.currentIndexChanged.connect(self.refresh_servers_in_list)

        self.servers_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.servers_list.customContextMenuRequested[QtCore.QPoint].connect(self.my_server_list_widget_context)

        self.refresh_servers_in_list()

    
        list_layout.addWidget(self.servers_list)


    def refresh_servers_in_list(self):

        selected_option = self.providers_combo_box.currentText()
        self.servers_list.clear()
        servers_items = proxies_json_reader.get_server_list_in_provider_group(provider_group_name=selected_option)
        self.servers_list.addItems(servers_items)


    def my_server_list_widget_context(self, point):

        popMenu = QMenu()
        set_as_running = popMenu.addAction('设为活动服务器')
        see_see_speed = popMenu.addAction('测个速看看')

        user_choice_in_context_menu = popMenu.exec_(self.servers_list.mapToGlobal(point))
        if user_choice_in_context_menu == set_as_running:
            context_menu_combobox_content = self.providers_combo_box.currentText()
            context_menu_list_widgets_content = self.servers_list.currentItem().text()
            print(context_menu_list_widgets_content, context_menu_combobox_content)
            clash_restful.ApiRequest.change_proxy(group_name=context_menu_combobox_content
                                            , server_name=context_menu_list_widgets_content)

        elif user_choice_in_context_menu == see_see_speed:
            context_menu_list_widgets_content = self.servers_list.currentItem().text()
            delay, meanDelay = clash_restful.ApiRequest.speed(context_menu_list_widgets_content)
            print("22222313131313313131313", delay, meanDelay)

            select_item = self.servers_list.selectedItems()
            for i in select_item:
                print(i.text())
                i.setText(i.text() + ' (%sms)' % delay)


    def setting_window(self):
        self.w = SettingWindow()

        self.w.show()
        # self.hide()

    def logs_window(self):

        self.l = LogsWindow()
        self.l.show()





class SettingWindow(QWidget):

    logs_level = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("settings")
        self.setFixedSize(400, 150)
        setting_layout = QVBoxLayout()

        self.setLayout(setting_layout)

        lan_layout = QHBoxLayout()
        setting_layout.addLayout(lan_layout)

        mode_layout = QHBoxLayout()
        setting_layout.addLayout(mode_layout)

        http_port_layout = QHBoxLayout()
        setting_layout.addLayout(http_port_layout)

        socks_port_layout = QHBoxLayout()
        setting_layout.addLayout(socks_port_layout)

        logs_layout = QHBoxLayout()
        setting_layout.addLayout(logs_layout)

        # self.setting_layout.addLayout()
        self.lan_label = QLabel(text="是否允许来自局域网的连接")

        self.lan_combobox = QComboBox()
        self.lan_combobox.addItems(['允许', '禁止'])
        self.lan_combobox.currentIndexChanged.connect(self.change_lan)

        lan_layout.addWidget(self.lan_label)
        lan_layout.addWidget(self.lan_combobox)

        self.mode = QLabel(text='代理模式')
        self.mode_combobox = QComboBox()
        self.mode_combobox.addItems(['直连', '规则', '全局'])
        self.mode_current = clash_restful.ApiRequest.get_config()["mode"]

        if self.mode_current == 'rule':
            self.mode_combobox.setCurrentIndex(1)
        elif self.mode_current == "global":
            self.mode_combobox.setCurrentIndex(2)
        else:
            self.mode_combobox.setCurrentIndex(0)
            
        self.mode_combobox.currentIndexChanged.connect(self.change_proxy_mode)

        mode_layout.addWidget(self.mode)
        mode_layout.addWidget(self.mode_combobox)

        self.http_label = QLabel(text='http端口号')
        self.http_port_show_in_label = str(clash_restful.ApiRequest.get_config()['port'])
        self.http_text = QLabel(text=self.http_port_show_in_label)
        http_port_layout.addWidget(self.http_label)
        http_port_layout.addWidget(self.http_text)

        self.socks_label = QLabel(text='socks端口号')
        self.socks_port_show_in_label = str(clash_restful.ApiRequest.get_config()['socks-port'])
        self.socks_text = QLabel(text=self.socks_port_show_in_label)
        socks_port_layout.addWidget(self.socks_label)
        socks_port_layout.addWidget(self.socks_text)


    def change_proxy_mode(self):
        mode_select = self.mode_combobox.currentIndex()
        if mode_select == 0:
            change_mode = "Direct"
        elif mode_select == 1:
            change_mode = "Rule"

        elif mode_select == 2:
            change_mode = "Global"
        clash_restful.ApiRequest.change_proxy_mode(change_to=change_mode)

    def logs_button_send_clicked(self):
        self.logs_level.emit(self.logs_level_combobox.currentText())

    def change_lan(self):
        lan_select = self.lan_combobox.currentIndex()
        lan_mode = True if lan_select == 0 else False
        clash_restful.ApiRequest.change_allow_lan(change_to=lan_mode)

class LogsWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("logs")
        self.setFixedSize(1400, 600)
        logs_layout = QVBoxLayout()
        self.setLayout(logs_layout)

        self.logs_label = QLabel(text="日志")
        self.logs_rich_text = QTextBrowser()
        self.logs_button = QPushButton('输出日志')

        self.socket = QtWebSockets.QWebSocket()
        self.socket.textMessageReceived.connect(self.handle_text_message_received)
        self.logs_button.clicked.connect(self.start_log_websocket)
        #
        self.logs_level_label = QLabel(text="日志等级")
        self.logs_level_combobox = QComboBox()
        self.logs_level_combobox.addItems(["debug", "info", "warning", "error", "silent"])

        logs_layout.addWidget(self.logs_level_label)
        logs_layout.addWidget(self.logs_level_combobox)

        logs_layout.addWidget(self.logs_label)
        logs_layout.addWidget(self.logs_rich_text)
        logs_layout.addWidget(self.logs_button)


    def start_log_websocket(self):

        if self.socket.state() == QtNetwork.QAbstractSocket.UnconnectedState:
            mode = self.logs_level_combobox.currentText()
            print('1111111222222222222', mode)
            url = "ws://127.0.0.1:9090/logs?level=%s&token=" % mode
            self.socket.open(QtCore.QUrl(url))
        # elif self.socket.state() == QtNetwork.QAbstractSocket.ConnectedState:
        #     self.socket.close()


    def handle_text_message_received(self, message):
        print(type(message))

        self.logs_rich_text.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
