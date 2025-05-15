from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout
from PySide6.QtGui import QColor

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyOverlayKit.overlay import Overlay

if __name__ == "__main__":
    app = QApplication([])

    # 1. Create an instance of the Overlay
    overlay = Overlay(
        show_close_button=True,
        close_behavior="exit",
        close_button_color="#3C8DBC",
        close_button_hover_color="#1F5A7A",
        rounded=True,
        corner_radius=20
    )
    overlay.set_background_opacity(0.5)
    overlay.set_overall_opacity(0.9)
    overlay.set_geometry(100, 100, 400, 200)

    # 2. Create a grid layout and set it to the overlay
    grid_layout = QGridLayout()
    overlay.setLayout(grid_layout)

    label1 = QLabel("Label 1")
    label2 = QLabel("Label 2")
    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")

    grid_layout.addWidget(label1, 0, 0)   # Row 0, Column 0
    grid_layout.addWidget(button1, 0, 1)  # Row 0, Column 1
    grid_layout.addWidget(label2, 1, 0)   # Row 1, Column 0
    grid_layout.addWidget(button2, 1, 1)  # Row 1, Column 1

    # 3. Show the overlay
    overlay.show()

    app.exec()
