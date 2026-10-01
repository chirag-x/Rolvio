"""Rolvio main window shell."""
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rolvio by NORVI")
        self.resize(1024, 768)
        
        # Apply strict design system rules
        self.setStyleSheet("""
            QMainWindow {
                background-color: #070B12;
            }
            QLabel {
                color: #F5F7FA;
                font-family: 'Inter', 'Segoe UI', sans-serif;
                font-size: 24px;
            }
        """)
        
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        
        welcome_label = QLabel("Rolvio AI Career Agent")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(welcome_label)
        
        self.setCentralWidget(central_widget)
