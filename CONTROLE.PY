from PyQt5 import  uic,QtWidgets

def funcao_principal():
  Linha1 = formulario.lineEdit.text()
  Linha2 = formulario.lineEdit_2.text()
  Linha3 = formulario.lineEdit_3.text()

  print("Nome do produto",Linha1)
  print("Descrição:",Linha2)
  print("valor:",Linha3)

  if formulario.radioButton.isChecked():
    print("DISPONÍVEL PARA VENDA")

  elif formulario.radioButton_2.isChecked():
   print("NÃO DISPONÍVEL PARA VENDA")

    




app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()