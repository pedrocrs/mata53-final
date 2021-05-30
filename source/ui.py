import sys
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, pyqtSlot
from functools import partial
from a_star import astar

class ExampleWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        #self.setMinimumSize(QSize(440, 240))    
        self.setWindowTitle("Algoritmo A*")
        
        #inserção grafo
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("0000100000\n0000100000\n0000100000\n0000100000\n0000100000\n0000100000\n0000100000\n0000000000\n0000100000\n0000000000\n")

        #inserção caminho início
        self.inicioLinha = QLineEdit(self)
        self.inicioColuna = QLineEdit(self)

        #inserção caminho fim

        self.finalLinha = QLineEdit(self)
        self.finalColuna = QLineEdit(self)

        #Labels
        self.lbSaida = QLabel()
        self.lbSaida.setText("Caminho:")

        self.lbCaminhoInicial = QLabel()
        self.lbCaminhoDestino = QLabel()
        self.lbCaminhoInicial.setText("Início do caminho:")
        self.lbCaminhoDestino.setText("Fim do caminho:")

        
        button = QPushButton('Enviar Matriz', self)
        button.setToolTip('Clique aqui para enviar a Matriz')
        button.clicked.connect(self.on_click)
        
        layout = QGridLayout()
        layout.addWidget(self.b,0,0)
        layout.addWidget(self.lbCaminhoInicial,1,0)
        layout.addWidget(self.inicioLinha,2,0)
        layout.addWidget(self.inicioColuna,3,0)
        layout.addWidget(self.lbCaminhoDestino,4,0)
        layout.addWidget(self.finalLinha,5,0)
        layout.addWidget(self.finalColuna,6,0) 
        layout.addWidget(button,7,0)
        layout.addWidget(self.lbSaida,8,0)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        self.show()

    
    @pyqtSlot()
    def on_click(self):
        if(len(self.inicioLinha.text()) == 0 or len(self.inicioColuna.text()) == 0 or len(self.finalLinha.text()) == 0 or len(self.finalColuna.text()) == 0 or len(self.b.toPlainText()) == 0):
            error = QMessageBox()
            error.setText("Prencha todos os campos!")
            error.exec_()
            return
        arrayMatriz = []
        lineMatriz = []
        arrayInicio = []
        arrayFinal = []
        matriz =(self.b.toPlainText())
        inicial = (int(self.inicioLinha.text()), int(self.inicioColuna.text()))
        fim = (int(self.finalLinha.text()), int(self.finalColuna.text()))
        print(inicial)
        print('\n')
        print(fim)
        for m in matriz:
            if m =='\n':
                arrayMatriz.append(lineMatriz)
                lineMatriz = []
            else:
                lineMatriz.append(int(m))

        caminho = astar(arrayMatriz, inicial, fim)
        self.lbSaida.setText(str(caminho))

        print(caminho)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )