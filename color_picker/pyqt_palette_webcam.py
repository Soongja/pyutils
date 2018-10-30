import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QColorDialog
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'hair color picker'
        self.left = 200
        self.top = 200
        self.width = 200
        self.height = 80
        self.initUI()
        self.rgb = (0, 0, 0) # initial value

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Choose Color!', self)
        button.move(55, 30)
        button.clicked.connect(self.on_click)

        self.show()

    @pyqtSlot()
    def on_click(self):
        self.rgb = openColorDialog(self)


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def openColorDialog(self):
    color = QColorDialog.getColor()
    return hex_to_rgb(color.name())


if __name__ == '__main__':
    app = QApplication([])
    qt = App()

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        print(qt.rgb)
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        if ret:
            frame[:30, :] = [0, 0, 255]
            cv2.imshow('demo', frame)

            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()


