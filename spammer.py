import pyautogui as ag
import time
a = 2
sex = ag.prompt(text='Whaddya Wanna spam?', title='oo' , default='Type Here')
input("Press enter to start spamming!")
time.sleep(5)
def spam(spamMessage):
    ag.write(spamMessage)
    ag.press("enter")
    #time.sleep(0.1)
    return
while a == 2:
    spam(sex)

