import sys
import json
import requests
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget, QFileDialog,
    QMessageBox, QScrollArea, QGridLayout, QTableWidget, QTableWidgetItem,
    QStackedWidget, QFrame, QListWidgetItem
)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont, QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

API_BASE_URL = 'https://equipmentanalyzer.pythonanywhere.com/api'


class LoginWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        
        # Title
        title = QLabel("Login")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        layout.addSpacing(30)
        
        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumHeight(40)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        
        layout.addSpacing(10)
        
        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(40)
        self.password_input.returnPressed.connect(self.handle_login)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        
        layout.addSpacing(20)
        
        # Error label
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red; background-color: #fee; padding: 10px; border-radius: 5px;")
        self.error_label.setWordWrap(True)
        self.error_label.hide()
        layout.addWidget(self.error_label)
        
        # Login button
        login_btn = QPushButton("Login")
        login_btn.setMinimumHeight(40)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: #3B82F6;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #2563EB;
            }
        """)
        login_btn.clicked.connect(self.handle_login)
        layout.addWidget(login_btn)
        
        layout.addSpacing(10)
        
        # Register link
        register_btn = QPushButton("Don't have an account? Register")
        register_btn.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #3B82F6;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: #2563EB;
            }
        """)
        register_btn.clicked.connect(self.switch_to_register)
        layout.addWidget(register_btn)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            self.show_error("Please enter username and password")
            return
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/login/",
                json={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                data = response.json()
                self.parent.set_token(data.get('token'))
                self.parent.show_dashboard(data.get('last_uploads', []))
            else:
                error_data = response.json()
                self.show_error(error_data.get('error', 'Login failed'))
        except Exception as e:
            self.show_error(f"Connection error: {str(e)}")
    
    def show_error(self, message):
        self.error_label.setText(message)
        self.error_label.show()
    
    def switch_to_register(self):
        self.parent.show_register()


class RegisterWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 50, 50, 50)
        
        # Title
        title = QLabel("Register")
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        layout.addSpacing(30)
        
        # Username
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMinimumHeight(40)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username_input)
        
        layout.addSpacing(10)
        
        # Password
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMinimumHeight(40)
        self.password_input.returnPressed.connect(self.handle_register)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        
        layout.addSpacing(20)
        
        # Error label
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red; background-color: #fee; padding: 10px; border-radius: 5px;")
        self.error_label.setWordWrap(True)
        self.error_label.hide()
        layout.addWidget(self.error_label)
        
        # Register button
        register_btn = QPushButton("Register")
        register_btn.setMinimumHeight(40)
        register_btn.setStyleSheet("""
            QPushButton {
                background-color: #10B981;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #059669;
            }
        """)
        register_btn.clicked.connect(self.handle_register)
        layout.addWidget(register_btn)
        
        layout.addSpacing(10)
        
        # Login link
        login_btn = QPushButton("Already have an account? Login")
        login_btn.setStyleSheet("""
            QPushButton {
                background: none;
                border: none;
                color: #10B981;
                text-decoration: underline;
            }
            QPushButton:hover {
                color: #059669;
            }
        """)
        login_btn.clicked.connect(self.switch_to_login)
        layout.addWidget(login_btn)
        
        layout.addStretch()
        
        self.setLayout(layout)
    
    def handle_register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            self.show_error("Please enter username and password")
            return
        
        try:
            response = requests.post(
                f"{API_BASE_URL}/register/",
                json={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                data = response.json()
                self.parent.set_token(data.get('token'))
                self.parent.show_dashboard([])
            else:
                error_data = response.json()
                self.show_error(error_data.get('error', 'Registration failed'))
        except Exception as e:
            self.show_error(f"Connection error: {str(e)}")
    
    def show_error(self, message):
        self.error_label.setText(message)
        self.error_label.show()
    
    def switch_to_login(self):
        self.parent.show_login()


class PieChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(8, 6), facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(600, 400)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def plot(self, labels, values):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # Modern color palette
        colors = ['#FF6B9D', '#4ECDC4', '#FFE66D', '#95E1D3', '#A8E6CF', '#FF8B94', '#C7CEEA', '#FFDAB9']
        
        # Create pie chart with modern styling
        wedges, texts, autotexts = ax.pie(
            values, 
            labels=labels, 
            autopct='%1.1f%%',
            colors=colors[:len(labels)],
            startangle=90,
            pctdistance=0.85,
            explode=[0.05] * len(labels),  # Slightly separate slices
            shadow=True,
            textprops={'fontsize': 10, 'weight': 'bold'}
        )
        
        # Style the percentage text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(11)
            autotext.set_weight('bold')
        
        # Style the label text
        for text in texts:
            text.set_fontsize(11)
            text.set_weight('bold')
        
        ax.set_title('Type Distribution', fontsize=14, weight='bold', pad=20)
        
        # Equal aspect ratio ensures circular pie
        ax.axis('equal')
        
        self.figure.tight_layout()
        self.canvas.draw()


class BarChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(10, 6), facecolor='white')
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setMinimumSize(800, 500)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def plot(self, labels, flowrate, pressure, temperature):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        
        # Set background color
        ax.set_facecolor('#F8F9FA')
        self.figure.patch.set_facecolor('white')
        
        x = list(range(len(labels)))
        width = 0.25
        
        # Modern color palette with gradients
        color_flowrate = '#3B82F6'  # Blue
        color_pressure = '#10B981'   # Green
        color_temperature = '#F59E0B'  # Orange
        
        # Create bars with enhanced styling
        bars1 = ax.bar(
            [i - width for i in x], 
            flowrate, 
            width, 
            label='Avg Flowrate',
            color=color_flowrate,
            edgecolor='white',
            linewidth=1.5,
            alpha=0.9
        )
        
        bars2 = ax.bar(
            x, 
            pressure, 
            width, 
            label='Avg Pressure',
            color=color_pressure,
            edgecolor='white',
            linewidth=1.5,
            alpha=0.9
        )
        
        bars3 = ax.bar(
            [i + width for i in x], 
            temperature, 
            width, 
            label='Avg Temperature',
            color=color_temperature,
            edgecolor='white',
            linewidth=1.5,
            alpha=0.9
        )
        
        # Add value labels on top of bars
        def add_value_labels(bars):
            for bar in bars:
                height = bar.get_height()
                ax.text(
                    bar.get_x() + bar.get_width() / 2.,
                    height,
                    f'{height:.1f}',
                    ha='center',
                    va='bottom',
                    fontsize=8,
                    weight='bold',
                    color='#374151'
                )
        
        add_value_labels(bars1)
        add_value_labels(bars2)
        add_value_labels(bars3)
        
        # Customize axes
        ax.set_xlabel('Type', fontsize=12, weight='bold', color='#374151')
        ax.set_ylabel('Value', fontsize=12, weight='bold', color='#374151')
        ax.set_title('Per Type Statistics Comparison', fontsize=14, weight='bold', pad=20, color='#1F2937')
        
        # Set x-axis labels
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10, weight='bold')
        
        # Customize legend
        legend = ax.legend(
            loc='upper left',
            frameon=True,
            fancybox=True,
            shadow=True,
            fontsize=10,
            framealpha=0.95
        )
        legend.get_frame().set_facecolor('white')
        legend.get_frame().set_edgecolor('#E5E7EB')
        
        # Add grid for better readability
        ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.7, color='#9CA3AF')
        ax.set_axisbelow(True)
        
        # Style spines
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#E5E7EB')
        ax.spines['bottom'].set_color('#E5E7EB')
        
        # Customize tick colors
        ax.tick_params(colors='#6B7280', which='both')
        
        self.figure.tight_layout()
        self.canvas.draw()


class FileDetailWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        
        # Scroll area for content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        
        # Content widget
        content_widget = QWidget()
        self.content_layout = QVBoxLayout(content_widget)
        
        # Placeholder label
        self.placeholder = QLabel("Select a file from the sidebar or upload a new one")
        self.placeholder.setAlignment(Qt.AlignCenter)
        self.placeholder.setStyleSheet("color: gray; font-size: 16px; padding: 50px;")
        self.content_layout.addWidget(self.placeholder)
        
        scroll.setWidget(content_widget)
        main_layout.addWidget(scroll)
        
        self.setLayout(main_layout)
    
    def display_file_data(self, file_data):
        # Clear existing content
        while self.content_layout.count():
            child = self.content_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Overall Statistics
        stats_frame = QFrame()
        stats_frame.setStyleSheet("background-color: white; border-radius: 5px; padding: 10px;")
        stats_layout = QVBoxLayout(stats_frame)
        
        stats_title = QLabel("Overall Statistics")
        stats_title.setFont(QFont("Arial", 18, QFont.Bold))
        stats_layout.addWidget(stats_title)
        
        stats_grid = QGridLayout()
        
        stats_data = [
            ("Total Records", file_data.get('total_records', 0), "#DBEAFE", "#3B82F6"),
            ("Avg Flowrate", f"{file_data.get('avg_flowrate', 0):.2f}", "#D1FAE5", "#10B981"),
            ("Avg Pressure", f"{file_data.get('avg_pressure', 0):.2f}", "#FEF3C7", "#F59E0B"),
            ("Avg Temperature", f"{file_data.get('avg_temperature', 0):.2f}", "#FEE2E2", "#EF4444"),
        ]
        
        for i, (label, value, bg_color, text_color) in enumerate(stats_data):
            stat_widget = QFrame()
            stat_widget.setStyleSheet(f"background-color: {bg_color}; border-radius: 5px; padding: 15px;")
            stat_layout = QVBoxLayout(stat_widget)
            
            label_widget = QLabel(label)
            label_widget.setStyleSheet("color: #6B7280; font-size: 12px;")
            stat_layout.addWidget(label_widget)
            
            value_widget = QLabel(str(value))
            value_widget.setStyleSheet(f"color: {text_color}; font-size: 24px; font-weight: bold;")
            stat_layout.addWidget(value_widget)
            
            stats_grid.addWidget(stat_widget, 0, i)
        
        stats_layout.addLayout(stats_grid)
        self.content_layout.addWidget(stats_frame)
        
        # Type Distribution Chart
        if 'type_distribution' in file_data and file_data['type_distribution']:
            chart_frame = QFrame()
            chart_frame.setStyleSheet("background-color: white; border-radius: 5px; padding: 10px;")
            chart_layout = QVBoxLayout(chart_frame)
            
            chart_title = QLabel("Type Distribution")
            chart_title.setFont(QFont("Arial", 18, QFont.Bold))
            chart_layout.addWidget(chart_title)
            
            pie_chart = PieChartWidget()
            labels = list(file_data['type_distribution'].keys())
            values = list(file_data['type_distribution'].values())
            pie_chart.plot(labels, values)
            chart_layout.addWidget(pie_chart)
            
            self.content_layout.addWidget(chart_frame)
        
        # Per Type Stats Table
        if 'per_type_stats' in file_data and file_data['per_type_stats']:
            table_frame = QFrame()
            table_frame.setStyleSheet("background-color: white; border-radius: 5px; padding: 10px;")
            table_layout = QVBoxLayout(table_frame)
            
            table_title = QLabel("Per Type Statistics (Table)")
            table_title.setFont(QFont("Arial", 18, QFont.Bold))
            table_layout.addWidget(table_title)
            
            table = QTableWidget()
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(['Type', 'Count', 'Avg Flowrate', 'Avg Pressure', 'Avg Temperature'])
            
            per_type_stats = file_data['per_type_stats']
            table.setRowCount(len(per_type_stats))
            
            for row, (type_name, stats) in enumerate(per_type_stats.items()):
                table.setItem(row, 0, QTableWidgetItem(type_name))
                table.setItem(row, 1, QTableWidgetItem(str(stats.get('count', 0))))
                table.setItem(row, 2, QTableWidgetItem(f"{stats.get('avg_flowrate', 0):.2f}"))
                table.setItem(row, 3, QTableWidgetItem(f"{stats.get('avg_pressure', 0):.2f}"))
                table.setItem(row, 4, QTableWidgetItem(f"{stats.get('avg_temperature', 0):.2f}"))
            
            table.resizeColumnsToContents()
            table_layout.addWidget(table)
            
            self.content_layout.addWidget(table_frame)
            
            # Per Type Stats Chart
            bar_chart_frame = QFrame()
            bar_chart_frame.setStyleSheet("background-color: white; border-radius: 5px; padding: 10px;")
            bar_chart_layout = QVBoxLayout(bar_chart_frame)
            
            bar_chart_title = QLabel("Per Type Statistics (Chart)")
            bar_chart_title.setFont(QFont("Arial", 18, QFont.Bold))
            bar_chart_layout.addWidget(bar_chart_title)
            
            bar_chart = BarChartWidget()
            types = list(per_type_stats.keys())
            flowrates = [per_type_stats[t]['avg_flowrate'] for t in types]
            pressures = [per_type_stats[t]['avg_pressure'] for t in types]
            temperatures = [per_type_stats[t]['avg_temperature'] for t in types]
            bar_chart.plot(types, flowrates, pressures, temperatures)
            bar_chart_layout.addWidget(bar_chart)
            
            self.content_layout.addWidget(bar_chart_frame)
        
        self.content_layout.addStretch()


class DashboardWindow(QWidget):
    def __init__(self, parent=None, initial_uploads=None):
        super().__init__(parent)
        self.parent = parent
        self.uploads = initial_uploads or []
        self.selected_file = None
        self.init_ui()
        
        # Load initial uploads
        if self.uploads:
            self.update_upload_list()
    
    def init_ui(self):
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Sidebar
        sidebar = QFrame()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("background-color: #1F2937; color: white;")
        sidebar_layout = QVBoxLayout(sidebar)
        
        sidebar_title = QLabel("Recent Uploads")
        sidebar_title.setFont(QFont("Arial", 16, QFont.Bold))
        sidebar_title.setStyleSheet("padding: 15px; color: white;")
        sidebar_layout.addWidget(sidebar_title)
        
        self.upload_list = QListWidget()
        self.upload_list.setStyleSheet("""
            QListWidget {
                background-color: #1F2937;
                border: none;
                padding: 5px;
            }
            QListWidget::item {
                background-color: #374151;
                border-radius: 5px;
                padding: 10px;
                margin: 5px;
                color: white;
            }
            QListWidget::item:selected {
                background-color: #3B82F6;
            }
            QListWidget::item:hover {
                background-color: #4B5563;
            }
        """)
        self.upload_list.itemClicked.connect(self.on_file_selected)
        sidebar_layout.addWidget(self.upload_list)
        
        main_layout.addWidget(sidebar)
        
        # Main content area
        content_area = QWidget()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)
        
        # Header
        header = QFrame()
        header.setStyleSheet("background-color: white; border-bottom: 1px solid #E5E7EB;")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 15, 20, 15)
        
        header_title = QLabel("Chemical Equipment Parameter Visualizer")
        header_title.setFont(QFont("Arial", 18, QFont.Bold))
        header_layout.addWidget(header_title)
        
        header_layout.addStretch()
        
        logout_btn = QPushButton("Logout")
        logout_btn.setStyleSheet("""
            QPushButton {
                background-color: #EF4444;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #DC2626;
            }
        """)
        logout_btn.clicked.connect(self.handle_logout)
        header_layout.addWidget(logout_btn)
        
        content_layout.addWidget(header)
        
        # Scroll area for main content
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("background-color: #F3F4F6; border: none;")
        
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(20, 20, 20, 20)
        
        # Upload CSV section
        upload_frame = QFrame()
        upload_frame.setStyleSheet("background-color: white; border-radius: 5px; padding: 20px;")
        upload_layout = QVBoxLayout(upload_frame)
        
        upload_title = QLabel("Upload CSV File")
        upload_title.setFont(QFont("Arial", 18, QFont.Bold))
        upload_layout.addWidget(upload_title)
        
        self.file_label = QLabel("No file selected")
        self.file_label.setStyleSheet("color: gray; padding: 10px;")
        upload_layout.addWidget(self.file_label)
        
        btn_layout = QHBoxLayout()
        
        select_file_btn = QPushButton("Select File")
        select_file_btn.setStyleSheet("""
            QPushButton {
                background-color: #6B7280;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #4B5563;
            }
        """)
        select_file_btn.clicked.connect(self.select_file)
        btn_layout.addWidget(select_file_btn)
        
        self.upload_btn = QPushButton("Upload")
        self.upload_btn.setEnabled(False)
        self.upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #3B82F6;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px 20px;
                font-weight: bold;
            }
            QPushButton:hover:enabled {
                background-color: #2563EB;
            }
            QPushButton:disabled {
                background-color: #9CA3AF;
            }
        """)
        self.upload_btn.clicked.connect(self.upload_file)
        btn_layout.addWidget(self.upload_btn)
        
        btn_layout.addStretch()
        
        upload_layout.addLayout(btn_layout)
        scroll_layout.addWidget(upload_frame)
        
        # File detail section
        self.file_detail = FileDetailWidget()
        scroll_layout.addWidget(self.file_detail)
        
        scroll_layout.addStretch()
        
        scroll.setWidget(scroll_content)
        content_layout.addWidget(scroll)
        
        main_layout.addWidget(content_area)
        
        self.setLayout(main_layout)
        
        self.selected_file_path = None
    
    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select CSV File", "", "CSV Files (*.csv)"
        )
        if file_path:
            self.selected_file_path = file_path
            self.file_label.setText(f"Selected: {file_path.split('/')[-1]}")
            self.upload_btn.setEnabled(True)
    
    def upload_file(self):
        if not self.selected_file_path:
            return
        
        try:
            with open(self.selected_file_path, 'rb') as f:
                files = {'file': f}
                headers = {'Authorization': f'Token {self.parent.token}'}
                response = requests.post(
                    f"{API_BASE_URL}/upload_csv/",
                    files=files,
                    headers=headers
                )
            
            if response.status_code == 200:
                data = response.json()
                
                # Create new upload entry
                new_upload = {
                    'id': len(self.uploads) + 1,
                    'file_name': self.selected_file_path.split('/')[-1],
                    'uploaded_at': datetime.now().isoformat(),
                    'total_records': data['overall_stats']['total_records'],
                    'avg_flowrate': data['overall_stats']['avg_flowrate'],
                    'avg_pressure': data['overall_stats']['avg_pressure'],
                    'avg_temperature': data['overall_stats']['avg_temperature'],
                    'type_distribution': data['overall_stats']['type_distribution'],
                    'per_type_stats': data['per_type_stats'],
                }
                
                self.uploads.insert(0, new_upload)
                self.uploads = self.uploads[:5]  # Keep only last 5
                self.update_upload_list()
                
                # Select the new upload
                self.upload_list.setCurrentRow(0)
                self.on_file_selected(self.upload_list.item(0))
                
                # Reset upload UI
                self.selected_file_path = None
                self.file_label.setText("No file selected")
                self.upload_btn.setEnabled(False)
                
                QMessageBox.information(self, "Success", "File uploaded successfully!")
            else:
                error_data = response.json()
                QMessageBox.warning(self, "Error", error_data.get('error', 'Upload failed'))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Upload error: {str(e)}")
    
    def update_upload_list(self):
        self.upload_list.clear()
        for upload in self.uploads:
            item = QListWidgetItem(upload['file_name'])
            timestamp = upload.get('uploaded_at', '')
            if timestamp:
                timestamp = timestamp.split('.')[0].replace('T', ' ')
            item.setData(Qt.UserRole, upload)
            item.setToolTip(f"Uploaded: {timestamp}")
            self.upload_list.addItem(item)
    
    def on_file_selected(self, item):
        file_data = item.data(Qt.UserRole)
        self.selected_file = file_data
        self.file_detail.display_file_data(file_data)
    
    def handle_logout(self):
        self.parent.logout()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.token = None
        self.init_ui()
        self.setWindowTitle("Chemical Equipment Parameter Visualizer")
        
        # Get screen size and set window to 90% of screen
        screen = QApplication.desktop().screenGeometry()
        width = int(screen.width() * 0.9)
        height = int(screen.height() * 0.9)
        x = int((screen.width() - width) / 2)
        y = int((screen.height() - height) / 2)
        self.setGeometry(x, y, width, height)
        
        # Set minimum size
        self.setMinimumSize(1400, 900)
    
    def init_ui(self):
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # Create pages
        self.login_page = LoginWindow(self)
        self.register_page = RegisterWindow(self)
        
        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.register_page)
        
        # Show login page
        self.show_login()
    
    def set_token(self, token):
        self.token = token
    
    def show_login(self):
        self.stack.setCurrentWidget(self.login_page)
    
    def show_register(self):
        self.stack.setCurrentWidget(self.register_page)
    
    def show_dashboard(self, initial_uploads):
        # Remove old dashboard if exists
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            if isinstance(widget, DashboardWindow):
                self.stack.removeWidget(widget)
                widget.deleteLater()
                break
        
        # Create new dashboard
        self.dashboard_page = DashboardWindow(self, initial_uploads)
        self.stack.addWidget(self.dashboard_page)
        self.stack.setCurrentWidget(self.dashboard_page)
    
    def logout(self):
        self.token = None
        
        # Remove dashboard
        for i in range(self.stack.count()):
            widget = self.stack.widget(i)
            if isinstance(widget, DashboardWindow):
                self.stack.removeWidget(widget)
                widget.deleteLater()
                break
        
        # Clear input fields
        self.login_page.username_input.clear()
        self.login_page.password_input.clear()
        self.login_page.error_label.hide()
        
        self.show_login()


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Set color palette
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(243, 244, 246))
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, QColor(255, 255, 255))
    palette.setColor(QPalette.AlternateBase, QColor(243, 244, 246))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(59, 130, 246))
    palette.setColor(QPalette.Highlight, QColor(59, 130, 246))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()