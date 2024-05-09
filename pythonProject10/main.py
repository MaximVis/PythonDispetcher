import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTabWidget, QTableWidget, \
    QTableWidgetItem, QDialog, QLabel, QLineEdit


class AmbulanceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Приложение Диспетчера Скорой Помощи")

        self.tabs = QTabWidget()

        self.calls_tab = QWidget()
        self.calls_table = QTableWidget()
        self.calls_table.setColumnCount(3)
        self.calls_table.setHorizontalHeaderLabels(["Адрес", "Количество пострадавших", "ФИО"])
        self.calls_tab_layout = QVBoxLayout()
        self.calls_tab_layout.addWidget(self.calls_table)
        self.calls_tab.setLayout(self.calls_tab_layout)

        self.stations_tab = QWidget()
        self.stations_table = QTableWidget()
        self.stations_table.setColumnCount(2)
        self.stations_table.setHorizontalHeaderLabels(["Адрес", "Контактная информация"])
        self.stations_tab_layout = QVBoxLayout()
        self.stations_tab_layout.addWidget(self.stations_table)
        self.stations_tab.setLayout(self.stations_tab_layout)

        self.medical_facilities_tab = QWidget()
        self.medical_facilities_table = QTableWidget()
        self.medical_facilities_table.setColumnCount(2)
        self.medical_facilities_table.setHorizontalHeaderLabels(["Доступные места", "Адрес"])
        self.medical_facilities_tab_layout = QVBoxLayout()
        self.medical_facilities_tab_layout.addWidget(self.medical_facilities_table)
        self.medical_facilities_tab.setLayout(self.medical_facilities_tab_layout)

        self.tabs.addTab(self.calls_tab, "Вызовы")
        self.tabs.addTab(self.stations_tab, "Подстанции")
        self.tabs.addTab(self.medical_facilities_tab, "Медицинские учреждения")

        add_call_button = QPushButton("Добавить вызов")
        add_call_button.clicked.connect(self.add_call_dialog)

        layout = QVBoxLayout()
        layout.addWidget(self.tabs)
        layout.addWidget(add_call_button)


        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Добавление начальных данных
        self.add_call("Ул. Ленина 15", "1", "Иванов И.И.")
        self.add_call("Пр. Мира 4", "1", "Иванов И.А.")
        self.add_station("Проспект Мира 6", "89993331243")
        self.add_station("Ул. Магистральная 9", "89993311243")
        self.add_station("ул. Ленина 1", "87773331243")
        self.add_medical_facility("32", "Пр. Карла-Маркса 10")
        self.add_medical_facility("46", "Ул. Масленикова 9")

    def add_call_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Добавить вызов")

        address_label = QLabel("Адрес:")
        address_input = QLineEdit()

        injured_label = QLabel("Количество пострадавших:")
        injured_input = QLineEdit()

        full_name_label = QLabel("ФИО:")
        full_name_input = QLineEdit()

        add_button = QPushButton("Добавить")
        add_button.clicked.connect(
            lambda: self.add_call(address_input.text(), injured_input.text(), full_name_input.text()))

        layout = QVBoxLayout()
        layout.addWidget(address_label)
        layout.addWidget(address_input)
        layout.addWidget(injured_label)
        layout.addWidget(injured_input)
        layout.addWidget(full_name_label)
        layout.addWidget(full_name_input)
        layout.addWidget(add_button)

        dialog.setLayout(layout)
        dialog.exec()

    def add_call(self, address, injured, full_name):
        row_position = self.calls_table.rowCount()
        self.calls_table.insertRow(row_position)

        self.calls_table.setItem(row_position, 0, QTableWidgetItem(address))
        self.calls_table.setItem(row_position, 1, QTableWidgetItem(injured))
        self.calls_table.setItem(row_position, 2, QTableWidgetItem(full_name))

    def add_station(self, address, contact_info):
        row_position = self.stations_table.rowCount()
        self.stations_table.insertRow(row_position)

        self.stations_table.setItem(row_position, 0, QTableWidgetItem(address))
        self.stations_table.setItem(row_position, 1, QTableWidgetItem(contact_info))

    def add_medical_facility(self, available_beds, address):
        row_position = self.medical_facilities_table.rowCount()
        self.medical_facilities_table.insertRow(row_position)

        self.medical_facilities_table.setItem(row_position, 0, QTableWidgetItem(available_beds))
        self.medical_facilities_table.setItem(row_position, 1, QTableWidgetItem(address))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ambulance_app = AmbulanceApp()
    ambulance_app.show()
    sys.exit(app.exec())
