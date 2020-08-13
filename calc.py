import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
  def __init__(self):
    self.display_string = ''

    # Call the base class constructor
    super().__init__()

    # Set the window title
    self.setWindowTitle('Calculator')

    # Set the main_window layout
    layout = qtw.QVBoxLayout()
    self.setLayout(layout)

    #Create the keypad
    self.create_keypad()

    # Display the main window
    self.show()

  def create_keypad(self):
    keypad = qtw.QWidget()
    keypad.setLayout(qtw.QGridLayout())

    # Text box to display the result
    self.txt_result = qtw.QLineEdit()

    # Buttons
    btn_result = qtw.QPushButton('Enter', clicked=self.press_enter)
    btn_clear = qtw.QPushButton('Clear', clicked=self.press_clear)

    btn_0 = qtw.QPushButton('0',clicked = lambda:self.press_number('0'))
    btn_1 = qtw.QPushButton('1',clicked = lambda:self.press_number('1'))
    btn_2 = qtw.QPushButton('2',clicked = lambda:self.press_number('2'))
    btn_3 = qtw.QPushButton('3',clicked = lambda:self.press_number('3'))
    btn_4 = qtw.QPushButton('4',clicked = lambda:self.press_number('4'))
    btn_5 = qtw.QPushButton('5',clicked = lambda:self.press_number('5'))
    btn_6 = qtw.QPushButton('6',clicked = lambda:self.press_number('6'))
    btn_7 = qtw.QPushButton('7',clicked = lambda:self.press_number('7'))
    btn_8 = qtw.QPushButton('8',clicked = lambda:self.press_number('8'))
    btn_9 = qtw.QPushButton('9',clicked = lambda:self.press_number('9'))

    btn_plus = qtw.QPushButton('+',clicked = lambda:self.press_number('+'))
    btn_mins = qtw.QPushButton('-',clicked = lambda:self.press_number('-'))
    btn_mult = qtw.QPushButton('*',clicked = lambda:self.press_number('*'))
    btn_divd = qtw.QPushButton('/',clicked = lambda:self.press_number('/'))

    # Adding buttons to the keypad layout
    keypad.layout().addWidget(self.txt_result,0, 0, 1, 4)
    keypad.layout().addWidget(btn_result,1, 0, 1, 2)
    keypad.layout().addWidget(btn_clear,1, 2, 1, 2)
    keypad.layout().addWidget(btn_9, 2, 0)
    keypad.layout().addWidget(btn_8, 2, 1)
    keypad.layout().addWidget(btn_7, 2, 2)
    keypad.layout().addWidget(btn_plus, 2, 3)
    keypad.layout().addWidget(btn_6, 3, 0)
    keypad.layout().addWidget(btn_5, 3, 1)
    keypad.layout().addWidget(btn_4, 3, 2,)
    keypad.layout().addWidget(btn_mins, 3, 3)
    keypad.layout().addWidget(btn_3, 4, 0)
    keypad.layout().addWidget(btn_2, 4, 1)
    keypad.layout().addWidget(btn_1, 4, 2)
    keypad.layout().addWidget(btn_mult, 4, 3,)
    keypad.layout().addWidget(btn_0, 5, 0, 1, 3)
    keypad.layout().addWidget(btn_divd, 5, 3)

    # Add keypad to the main_window layout
    self.layout().addWidget(keypad)

  def press_number(self,val):
    self.display_string += val
    self.txt_result.setText(self.display_string)

  def press_enter(self):
    self.txt_result.setText(str(eval(self.display_string)))

  def press_clear(self):
    self.txt_result.clear()
    self.display_string = ''

def main():
  #Instantiate the application
  app = qtw.QApplication([])

  #Instantiate the main window
  main_window = MainWindow()

  app.exec_()

if __name__ == "__main__":
  main()