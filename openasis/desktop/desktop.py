from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QWidget
import openasis.core.core as core
import pyttsx3

class Window(QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.edit = QtWidgets.QLineEdit(self)
        self.edit.installEventFilter(self)
        self.text_area = QtWidgets.QTextEdit(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.edit)
        layout.addWidget(self.text_area)

    def eventFilter(self, widget, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            widget is self.edit):
            key = event.key()
            if key == QtCore.Qt.Key_Enter or key == QtCore.Qt.Key_Return:
                answer = core.take_query(self.edit.text())
                self.text_area.append(answer)
                self.edit.setText("")
                tts_engine = pyttsx3.init()
                tts_engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
                tts_engine.say(answer)
                tts_engine.runAndWait()

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 300, 300)
    window.show()
    sys.exit(app.exec_())

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))