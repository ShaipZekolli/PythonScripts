from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon


class MainWindow():
    def __init__(self):
        
        self.window = QWidget()
        self.window.setWindowTitle("Zeko")
        self.window.setStyleSheet("background-color: black;")
        self.window.setWindowIcon(QIcon('icon.png'))
        self.window.showMaximized()

        # navbar
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        self.back_btn.setStyleSheet("color: white; background-color: black; border-style: outset; border-width: 1.5px; border-radius: 10px; border-color: #107c10; font: bold 12px; min-width: 2em;padding: 2px")
        
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)
        self.forward_btn.setStyleSheet("color: white; background-color: black; border-style: outset; border-width: 1.5px; border-radius: 10px; border-color: #107c10; font: bold 12px; min-width: 2em;padding: 2px")
        
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(33)
        self.url_bar.setStyleSheet("color: white; background-color: black; border-style: outset; border-width: 1px; border-radius: 10px; border-color: #107c10; font: bold 14px; padding: 2px")
        
        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        self.go_btn.setStyleSheet("color: white; background-color: black; border-style: outset; border-width: 1.5px; border-radius: 10px; border-color: #107c10; font: bold 14px; min-width: 4em;padding: 2px")
        
        self.src_btn = QPushButton("Src")
        self.src_btn.setMinimumHeight(30)
        self.src_btn.setStyleSheet("color: white; background-color: black; border-style: outset; border-width: 1.5px; border-radius: 10px; border-color: #107c10; font: bold 14px; min-width: 4em;padding: 2px")
        
        self.srcx_btn = QPushButton("")
        self.srcx_btn.setMaximumHeight(30)
        self.srcx_btn.setStyleSheet("background-color: black; min-width: 3em")
        self.srcxy_btn = QPushButton("")
        self.srcxy_btn.setMaximumHeight(30)
        self.srcxy_btn.setStyleSheet("background-color: black; min-width: 16em")
        
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)
        self.horizontal.addWidget(self.srcx_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.srcxy_btn)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.src_btn)
        
        self.browser = QWebEngineView()
        
        self.browser.settings().setAttribute(QWebEngineSettings.PluginsEnabled, False)
        self.browser.settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        self.browser.settings().setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        self.browser.page().fullScreenRequested.connect(QWebEngineFullScreenRequest.accept)
        
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.src_btn.clicked.connect(lambda: self.navigate2(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("http://google.com"))
        
        self.window.setLayout(self.layout)
        self.window.show()
        
    def navigate(self, url):
        if url.startswith("file"):
            url = url
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))
        elif not url.startswith("http"):
            url ="http://" + url
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))
        elif url.startswith("http"):
            url ="" + url
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))
    def navigate2(self, url):
        if url.startswith("http"):
            url ="view-source:" + url
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MainWindow()
app.exec_()