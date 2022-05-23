#import os
#from PyQt5 import QtGui, QtCore

from act_4 import *

class Ui_act_4(QtWidgets.QMainWindow,Ui_act_4):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        #-------------------------
        #self.analizar.setText("Analizar")
        #conseguir valores
        #file = self.t_name.text()
        #message = self.t_text.text()
        #quantity = self.t_line.text()
        #-------------------------
        self.analizar.clicked.connect(self.Create_file)
        self.analizar.clicked.connect(self.Analyze)
        
    
    def Create_file(self):
        #ubication = "C:/Documents/Sistemas en chip/"
        #file_type = ".txt"
        #fileName = ubication + self.t_name.text() + file_type
        #fileName = self.t_name.text()
        line="\n"
        texto =  self.t_texto.text() + line
    
        f=open(self.t_name.text(), 'w')
        for i in range(int(self.t_line.text())):
            x = texto
            f.write(x)
        f.close()
        
    def Analyze(self):
        fileHandle = open(self.t_name.text(), "r")
        tot = 0
        cant=0
        vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        consonantes =[ 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y','Z', 'b','c', 'd', 'f', 'g' ,'h' ,'j' ,'k' ,'l' ,'m' ,'n' ,'ñ','p' ,'q' ,'r' ,'s' ,'t' ,'v' ,'w' ,'x' ,'y' ,'z' ]
        
        for char in fileHandle.read():
            if char in vocales:
                tot = tot+1
            elif char in consonantes:
                cant=cant+1
    
        fileHandle.close()
 
        self.t_nvocales.setText(str(tot))
        self.t_nconsonantes.setText(str(cant))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_act_4()
    window.show()
    app.exec_()