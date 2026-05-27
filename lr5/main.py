import sys

from PySide6.QtWidgets import (
    QApplication,
    QTableWidgetItem,
    QMessageBox
)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


# ЗАГРУЗКА UI

app = QApplication(sys.argv)

ui_file = QFile("main.ui")
ui_file.open(QFile.ReadOnly)

loader = QUiLoader()
window = loader.load(ui_file)

ui_file.close()


# НАСТРОЙКА ТАБЛИЦЫ

window.orders_table.setColumnCount(5)

window.orders_table.setHorizontalHeaderLabels([
    "Клиент",
    "Продукция",
    "Стоимость",
    "Дата",
    "Статус"
])


# ДОБАВЛЕНИЕ ЗАКАЗА

def add_order():

    client = window.client_input.text()

    product = window.product_combo.currentText()

    price = window.price_input.text()

    date = window.date_input.text()

    status = window.status_combo.currentText()


    # ПРОВЕРКА ПУСТЫХ ПОЛЕЙ

    if client == "" or price == "":
        QMessageBox.warning(
            window,
            "Ошибка",
            "Заполните все поля!"
        )
        return


    # ДОБАВЛЕНИЕ СТРОКИ

    row = window.orders_table.rowCount()

    window.orders_table.insertRow(row)

    window.orders_table.setItem(
        row, 0,
        QTableWidgetItem(client)
    )

    window.orders_table.setItem(
        row, 1,
        QTableWidgetItem(product)
    )

    window.orders_table.setItem(
        row, 2,
        QTableWidgetItem(price)
    )

    window.orders_table.setItem(
        row, 3,
        QTableWidgetItem(date)
    )

    window.orders_table.setItem(
        row, 4,
        QTableWidgetItem(status)
    )


# ОЧИСТКА ПОЛЕЙ ВВОДА

def clear_fields():

    window.client_input.clear()

    window.price_input.clear()


# УДАЛЕНИЕ ЗАКАЗА

def delete_order():

    current_row = window.orders_table.currentRow()

    if current_row >= 0:
        window.orders_table.removeRow(current_row)

    else:
        QMessageBox.warning(
            window,
            "Ошибка",
            "Выберите заказ!"
        )


# ИТОГОВАЯ СУММА

def total_price():

    rows = window.orders_table.rowCount()

    total = 0


    for row in range(rows):

        item = window.orders_table.item(row, 2)

        if item:

            total += int(item.text())


    QMessageBox.information(
        window,
        "Итог",
        f"Общая сумма заказов: {total} руб."
    )


# КНОПКИ

window.add_button.clicked.connect(add_order)

window.clear_button.clicked.connect(clear_fields)

window.delete_button.clicked.connect(delete_order)

window.total_button.clicked.connect(total_price)


# ЗАПУСК ОКНА

window.show()

sys.exit(app.exec())
