from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QVBoxLayout
)
from random import shuffle


class Button(QPushButton):
    def __init__(self, text="") -> None:
        super().__init__(text)
        self.setFont(QFont('Algerian', 40, QFont.Weight.Bold))
        self.setFixedSize(100, 100)
        self.giveStyle()

    def giveStyle(self, color: str = "#e6e6e6"):
        self.setStyleSheet(f"""
            QPushButton {{
                border: 2px solid black;
                padding: 10px;
                border-radius: 12px; 
                color: #000;
                background-color: {color};
                font-size: 40px;
            }}
            QPushButton:hover {{
                background-color: #66cc00;
                font-size: 55px;    
                border: 2px solid "#bc8f5b";
                color: #F9E400;             
            }}
            QPushButton:pressed {{
                background-color: #003cb4;                 
            }}
        """)


class PauseNewGame(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__(text)
        self.setFixedSize(150, 50)
        self.giveStyle()

    def giveStyle(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #333A73;
                font-size: 22px;
                color: #EFECEC;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #D04848;
                font-size: 28px;
                color: white;
                font-weight: bold;
            }
        """)


class Puzzle(QWidget):
    def __init__(self, size: int) -> None:
        super().__init__()
        self.size = size
        self.original = list(map(str, range(1, self.size**2))) + [" "]
        self.setStyleSheet("background: #7C00FE")
        self.initUI()
        self.setLayout(self.vbox)

    def initUI(self):
        self.isStarted = False
        self.matrix = list()

        self.vbox = QVBoxLayout()
        self.grid = QGridLayout()

        self.timeLabel = QLabel("Time: 0 sec")
        self.timeLabel.setStyleSheet("font-size: 25px")
        self.timer = QTimer(self)
        self.counter = 0

        self.movesLabel = QLabel("Moves: 0")
        self.movesLabel.setStyleSheet("font-size: 25px")
        self.setMove()

        self.pause = PauseNewGame("Pause")
        self.pause.setCheckable(True)
        self.newGame = PauseNewGame("New Game")

        self.pause.pressed.connect(self.pauseWin)
        self.newGame.pressed.connect(self.startOver)

        self.numbers = self.generate()
        idx = 0
        for i in range(self.size):
            row = list()
            for j in range(self.size):
                btn = Button(self.numbers[idx])
                if btn.text() == " ":
                    btn.hide()
                row.append(btn)
                self.grid.addWidget(btn, i, j)
                btn.clicked.connect(self.modify)
                idx += 1
            self.matrix.append(row)
        self.isInOrder()

        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.timeLabel)
        self.hbox.addStretch()
        self.hbox.addWidget(self.movesLabel)

        self.vbox.addLayout(self.hbox)
        self.vbox.addSpacing(30)
        self.vbox.addLayout(self.grid)

        self.hbox2 = QVBoxLayout()
        self.hbox2.addWidget(self.pause)
        self.hbox2.addWidget(self.newGame)

        self.vbox.addSpacing(20)
        self.vbox.addLayout(self.hbox2)

    def generate(self):
        lst = list(map(str, range(1, self.size**2))) + [" "]
        shuffle(lst)
        return lst

    def setTimer(self):
        self.counter = 0
        self.timer.start(1000)
        self.timer.timeout.connect(self.updateTime)

    def updateTime(self):
        self.counter += 1
        self.timeLabel.setText(f"Time: {self.counter} sec")

    def setMove(self):
        self.moveCounter = 0
        self.moveCounterLabel = QLabel("0")
        self.moveCounterLabel.setStyleSheet("font-size: 25px")

    def updateMove(self):
        self.moveCounter += 1
        self.movesLabel.setText(f"Moves: {self.moveCounter}")

    def modify(self):
        if not self.isStarted:
            self.setTimer()
            self.isStarted = True

        btn = self.sender()
        for x in range(self.size):
            for y in range(self.size):
                if btn.text() == self.matrix[x][y].text():
                    if x + 1 < self.size and self.matrix[x + 1][y].text() == " ":
                        self.matrix[x + 1][y].setText(btn.text())
                        self.matrix[x + 1][y].show()
                        btn.hide()
                        btn.setText(' ')
                        self.updateMove()
                        self.isInOrder()
                    elif x > 0 and self.matrix[x - 1][y].text() == " ":
                        self.matrix[x - 1][y].setText(btn.text())
                        self.matrix[x - 1][y].show()
                        btn.hide()
                        btn.setText(' ')
                        self.updateMove()
                        self.isInOrder()
                    elif y > 0 and self.matrix[x][y - 1].text() == " ":
                        self.matrix[x][y - 1].setText(btn.text())
                        self.matrix[x][y - 1].show()
                        btn.hide()
                        btn.setText(' ')
                        self.updateMove()
                        self.isInOrder()
                    elif y + 1 < self.size and self.matrix[x][y + 1].text() == " ":
                        self.matrix[x][y + 1].setText(btn.text())
                        self.matrix[x][y + 1].show()
                        btn.hide()
                        btn.setText(' ')
                        self.updateMove()
                        self.isInOrder()

    def isInOrder(self):
        cnt = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y].text() == self.original[x * self.size + y]:
                    self.matrix[x][y].giveStyle("#FF7000")
                    cnt += 1
                else:
                    self.matrix[x][y].giveStyle()
        if cnt == self.size ** 2:
            self.close()
            self.win = YouWon()
            self.win.show()

    def pauseWin(self):
        if self.pause.isChecked():
            self.pause.setText("Pause")
            for btns in self.matrix:
                for btn in btns:
                    btn.setEnabled(True)
                    self.setStyleSheet("background: #7C00FE")
            self.timer.start()
        else:
            self.pause.setText("Resume")
            for btns in self.matrix:
                for btn in btns:
                    btn.setEnabled(False)
                    self.setStyleSheet("background: #A555EC")
            self.timer.stop()
        self.isInOrder()

    def startOver(self):
        self.win = Puzzle(self.size)
        self.win.show()
        self.close()


class YouWon(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet("background: #7C00FE")
        self.setFixedSize(1000, 560)
        self.logo = QLabel(self)
        pixmap = QPixmap("congrats.png")
        self.logo.setPixmap(pixmap.scaled(1000, 560, Qt.AspectRatioMode.KeepAspectRatio))


def main():
    app = QApplication([])
    puzzle = Puzzle(4)
    puzzle.show()
    app.exec()


if __name__ == "__main__":
    main()
