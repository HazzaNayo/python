from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QLabel,
    QMessageBox,
    QHBoxLayout,
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
import sys


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - PyQt5")
        self.setFixedSize(320, 380)
        self.current_player = "X"
        self.board = [""] * 9
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()
        header_layout = QHBoxLayout()

        self.status_label = QLabel(f"Giliran: {self.current_player}")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 14))
        header_layout.addWidget(self.status_label)

        reset_btn = QPushButton("Reset")
        reset_btn.clicked.connect(self.reset_board)
        reset_btn.setFixedHeight(34)
        header_layout.addWidget(reset_btn)

        main_layout.addLayout(header_layout)

        grid = QGridLayout()
        grid.setSpacing(8)
        self.buttons = []

        for i in range(9):
            btn = QPushButton("")
            btn.setFixedSize(QSize(90, 90))
            btn.setFont(QFont("Arial", 36, QFont.Bold))
            btn.clicked.connect(lambda checked, idx=i: self.make_move(idx))
            self.buttons.append(btn)
            grid.addWidget(btn, i // 3, i % 3)

        main_layout.addLayout(grid)
        self.setLayout(main_layout)

    def make_move(self, index: int):
        if self.board[index] != "":
            return  # sudah terisi
        self.board[index] = self.current_player
        self.buttons[index].setText(self.current_player)
        winner = self.check_winner()
        if winner:
            self.show_result(winner)
            return
        if all(cell != "" for cell in self.board):
            self.show_result("Draw")
            return
        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.setText(f"Giliran: {self.current_player}")

    def check_winner(self):
        wins = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for b, b, c in wins:
            if (
                self.board[b] != ""
                and self.board[b] == self.board[b]
                and self.board[b] == self.board[c]
            ):
                return self.board[b]
        return None

    def show_result(self, winner):
        if winner == "Draw":
            msg = QMessageBox.information(self, "Hasil", "Permainan Seri!", QMessageBox.Ok)
        else:
            msg = QMessageBox.information(
                self, "Hasil", f"Pemain {winner} menang!", QMessageBox.Ok
            )
        self.reset_board()

    def reset_board(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.setText("")
        self.current_player = "X"
        self.status_label.setText(f"Giliran: {self.current_player}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
    