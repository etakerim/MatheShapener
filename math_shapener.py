import sys
from PySide.QtCore import Qt, QTimer
from PySide.QtGui import (QApplication, QHBoxLayout, QVBoxLayout, QFormLayout,
                          QWidget, QMainWindow, QLabel, QPainter,
                          QPushButton, QPalette, QComboBox, QIcon, QPixmap,
                          QCheckBox, QSpinBox, QGroupBox, QSplitter)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)

    def draw(self):
        pass # QPaintEvent


class MathShapener(QWidget):
    MSHAPES = ['Sínus', 'Kosínus', 'Lissajousova krivka', 
                'Vektor', 'Kruh', 'Ruža', 'Kochova krivka', 
                'Kochova vločka', 'Serpinského koberec', 
                'Fraktálový strom', 'Mandelbrotova množina', 
                'L-system (Korytnačka)']

    def __init__(self):
        super().__init__()
        self.mainlayout = QHBoxLayout()

        self.leftlayout = QVBoxLayout()
        self.leftlayout.addLayout(self.shape_select())
        self.canvas = Canvas()
        self.leftlayout.addWidget(self.canvas)
        
        self.rightlayout = QVBoxLayout()
        self.rightlayout.addWidget(self.xy_setting())
        
        self.mainlayout.addLayout(self.leftlayout, 4)
        self.mainlayout.addLayout(self.rightlayout, 2)
        self.setLayout(self.mainlayout)

    def xy_setting(self):
        coor = QGroupBox('Súradnice')
        self.posinfo_layout = QFormLayout()
        
        self.xlabel = QLabel('X: ')
        self.xdata = QSpinBox()
        self.xdata.setRange(0, 600)
        self.ylabel = QLabel('Y: ')
        self.ydata = QSpinBox()
        self.ydata.setRange(0, 600)

        self.posinfo_layout.addRow(self.xlabel, self.xdata)
        self.posinfo_layout.addRow(self.ylabel, self.ydata)
        coor.setLayout(self.posinfo_layout)
        return coor

    def shape_select(self):
        topmenu = QHBoxLayout()
        
        self.shapesel = QComboBox()
        self.shapesel.addItems(self.MSHAPES)
        self.isgridactive = QCheckBox('Mriežka')
        self.savebtn = QPushButton('Uložiť')
        
        topmenu.addWidget(self.shapesel, 5)
        topmenu.addWidget(self.savebtn, 2)
        topmenu.addWidget(self.isgridactive, 2)
        return topmenu


    def actions_global(self):
        # self.shapesel.activated('') = #func add widgets + their signals
        pass

class AppWindow(QMainWindow):
    def __init__(self, title, min_size):
        super().__init__()
        self.setWindowTitle(title)
        self.setMinimumSize(*min_size)
        self.app = MathShapener()
        self.setCentralWidget(self.app)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow('Mathematical Shape Sharpener', (600, 400))
    app.exec_()