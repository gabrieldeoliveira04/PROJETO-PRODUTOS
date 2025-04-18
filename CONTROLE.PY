from PyQt5 import uic, QtWidgets
import mysql.connector
app = QtWidgets.QApplication([]) 
formulario = uic.loadUi("formulario.ui")

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)



def funcao_principal():
    Linha1 = formulario.lineEdit.text()
    Linha2 = formulario.lineEdit_2.text()
    Linha3 = formulario.lineEdit_3.text()

    disponivel = ""

    if formulario.radioButton.isChecked():
        print("DISPONÍVEL PARA VENDA")
        disponivel = "sim"
    elif formulario.radioButton_2.isChecked():
        print("NÃO DISPONÍVEL PARA VENDA")
        disponivel = "não"

    print("Nome do produto:", Linha1)
    print("Descrição:", Linha2)
    print("Valor:", Linha3)


    cursor = banco.cursor()
    comando = "INSERT INTO produtos (id, Descrição, valor, nome_do_produto) VALUES (%s, %s, %s, %s)"
    dados = (str(Linha1), str(Linha2), str(Linha3), str(disponivel))
    cursor.execute(comando, dados)
    banco.commit()

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    print(dados)
    print("sucesso ao rodar função principal")
    cursor.close()


formulario.pushButton.clicked.connect(funcao_principal)
formulario.setGeometry(100, 100, 400, 300)  # Posição e tamanho fixos
formulario.show()


app.exec()
