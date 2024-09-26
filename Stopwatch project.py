import sys 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class stop_watch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0,0,0,0) #dung de dem gio
        self.timelabel = QLabel("00:00:00.00",self) #cac label hien tren man hinh
        self.startbutton = QPushButton("Start",self)
        self.stopbutton = QPushButton("Stop",self)
        self.resetbutton = QPushButton("Reset",self)

        self.timer = QTimer(self) #dung de cap nhat thoi gian

        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Stop Watch") #dat ten va noi xuat hien cho UI
        self.setGeometry(800,300,500,500)

        vbox = QVBoxLayout() #tao 1 layout de edit sau do add cac widget vao de sap xep theo thu tu tu tren xuong duoi
        vbox.addWidget(self.timelabel)
        vbox.addWidget(self.startbutton)
        vbox.addWidget(self.stopbutton)
        vbox.addWidget(self.resetbutton)

        self.setLayout(vbox) #set cac widget vua sap xep vao UI

        self.timelabel.setAlignment(Qt.AlignCenter) ## dat label hien thi thoi gian vao center

        hbox = QHBoxLayout()# tao 1 layout horizontal

        hbox.addWidget(self.startbutton) # add cac nut bam vao de sap xep theo chieu ngang
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)

        vbox.addLayout(hbox)#set cac nut bam theo chieu ngang (add them layout vao layout vbox co san)
        
        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                font-weight: bold;
                font-family: calibri;
                           }
                           
            QPushButton{
                    font-size: 50px;
                                                                              
                }
            QLabel{
                    font-size: 120px;
                    background-color: #3b56ed;
                    color: #000301;
                    border-radius: 20px;
                           }
                           """)
        
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display) #10ms update dong ho 1 lan
        
        

    
    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0) #reset bo dem gio 
        self.timelabel.setText(self.format_time(self.time)) #reset lai bo dem gio tren UI

    def format_time(self,time): #dung de cap nhat time label hien thi tren UI
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10) #add 10milisec moi lan duoc goi ham
        self.timelabel.setText(self.format_time(self.time)) #hien thi time moi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = stop_watch()                                                        
    stopwatch.show()
    sys.exit(app.exec_())
