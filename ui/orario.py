from PyQt5.QtCore import QTime

from ui.orarioUi import Ui_MainWindow


# our class
class OrarioWindow(Ui_MainWindow):
    def __init__(self):
        super(OrarioWindow).__init__()

    def setupUi(self, Dialog):
        super(OrarioWindow, self).setupUi(Dialog)

        #  adding functions to buttons from here
        self.calcola.clicked.connect(self._calcola)

    def _calcola(self):
        start_time = self.startTime.time()
        start_lunch = self.startBreak.time()
        duration_lunch = self.durationBreak.time()
        end_lunch = start_lunch.addSecs(duration_lunch.hour()*3600 + duration_lunch.minute() * 60 + duration_lunch.second())
        duration_work = self.durationWork.time()
        end_time = start_time.addSecs(duration_work.hour()*3600 + duration_work.minute() * 60 + duration_work.second())\
                             .addSecs(duration_lunch.hour()*3600 + duration_lunch.minute() * 60 + duration_lunch.second())
        self.endTime.setTime(end_time)
        message = "{0} - {1}  ||||| {2} - {3}".format(start_time.toString(), start_lunch.toString(), end_lunch.toString(), end_time.toString())
        self.resultLabel.setText(message)

