from pyqtgraph.Qt.QtCore import Qt, QRect
from pyqtgraph.Qt.QtGui import QPainter, QColor, QMouseEvent, QRegion, QPainterPath
from pyqtgraph.Qt.QtWidgets import *
from pyqtgraph.Qt import QtWidgets

CLOSE_BEHAVIORS = {"close", "hide", "exit"}


class Overlay(QtWidgets.QWidget):
    def __init__(
            self,
            show_close_button=True,
            close_behavior: str = "exit",
            close_button_color="#FF4C4C",
            close_button_hover_color="darkred",
            rounded=False,
            corner_radius=15
    ):
        if close_behavior not in CLOSE_BEHAVIORS:
            raise ValueError(f"Invalid close_behavior: '{close_behavior}'. "
                             f"Expected one of: {', '.join(self.CLOSE_BEHAVIORS)}")
        self.close_behavior = close_behavior

        super().__init__()

        # Configuration
        self.show_close_button = show_close_button
        self.close_behavior = close_behavior
        self.close_button_color = close_button_color
        self.close_button_hover_color = close_button_hover_color
        self.rounded = rounded
        self.corner_radius = corner_radius

        self._drag_start_position = None
        self.bg_color = QColor(0, 0, 0, 100)

        self._setup_window_flags()
        self._setup_close_button()

    def _setup_window_flags(self):
        self.setWindowFlag(Qt.WindowType.Tool, True)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowType.WindowDoesNotAcceptFocus, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

    def _setup_close_button(self):
        self.close_button = QtWidgets.QPushButton("X", self)
        if self.rounded:
            self.close_button.setFixedSize(20, 20)
        else:
            self.close_button.setFixedSize(40, 20)
        self._apply_close_button_style()
        self.close_button.clicked.connect(self._handle_close_button)
        self.close_button.setVisible(self.show_close_button)

    def _handle_close_button(self):
        if self.close_behavior == "hide":
            self.hide()
        if self.close_behavior == "close":
            self.close()
        if self.close_behavior == "exit":
            QApplication.quit()

    def _apply_close_button_style(self):
        if self.rounded:
            style = f"""
            QPushButton {{
                background-color: {self.close_button_color};
                color: white;
                border: none;
                font-weight: bold;
                border-radius: {self.close_button.width() // 2}px;
            }}
            QPushButton:hover {{
                background-color: {self.close_button_hover_color};
            }}
            """
        else:
            style = f"""
            QPushButton {{
                background-color: {self.close_button_color};
                color: white;
                border: none;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {self.close_button_hover_color};
            }}
            """
        self.close_button.setStyleSheet(style)

    def set_background_color(self, color: QColor):
        self.bg_color = color
        self.update()

    def set_background_opacity(self, opacity: float):
        alpha = int(max(0.0, min(1.0, opacity)) * 255)  # Clamp between 0 and 1
        self.bg_color.setAlpha(alpha)
        self.update()  # Trigger repaint

    def set_overall_opacity(self, opacity: float):
        self.setWindowOpacity(opacity)

    def set_geometry(self, x: int, y: int, width: int, height: int):
        self.setGeometry(QRect(x, y, width, height))
        self.position_close_button()

    def set_size(self, width: int, height: int):
        self.resize(width, height)
        self.position_close_button()

    def set_close_behavior(self, behavior: str):
        if behavior not in CLOSE_BEHAVIORS:
            raise ValueError(f"Invalid close_behavior: '{behavior}'. "
                             f"Expected one of: {', '.join(CLOSE_BEHAVIORS)}")
        self.close_behavior = behavior

    def set_close_button_visibility(self, visible: bool):
        self.show_close_button = visible
        self.close_button.setVisible(visible)

    def set_close_button_colors(self, normal_color: str, hover_color: str):
        self.close_button_color = normal_color
        self.close_button_hover_color = hover_color
        self._apply_close_button_style()

    def set_rounded_corners(self, enabled: bool, radius: int = 15):
        self.rounded = enabled
        self.corner_radius = radius
        self._apply_close_button_style()  # update button style
        self.update()

    def position_close_button(self):
        if self.rounded:
            margin = 10
            btn_size = self.close_button.size()
            x = self.width() - btn_size.width() - margin
            y = margin
            self.close_button.move(x, y)
        else:
            self.close_button.move(self.width() - self.close_button.width() - 5, 5)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        if self.rounded:
            path = QPainterPath()
            path.addRoundedRect(0, 0, self.width(), self.height(), self.corner_radius, self.corner_radius)
            painter.setClipPath(path)

        painter.setBrush(self.bg_color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(self.rect())

    def add_widget(self, widget):
        if self.layout() is None:
            layout = QVBoxLayout(self)
            layout.setContentsMargins(10, 10, 10, 10)
            self.setLayout(layout)
        self.layout().addWidget(widget)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_position = event.globalPosition()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._drag_start_position:
            delta = event.globalPosition() - self._drag_start_position
            self.move(self.pos() + delta.toPoint())
            self._drag_start_position = event.globalPosition()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start_position = None
