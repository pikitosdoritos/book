# Бот автоклікер
import pyautogui
import time

# Автоклікер на точку екрана
time.sleep(3)

pyautogui.click(x=400, y=500)


# Автоклікер на кнопку (пошук об'єкту)
button = pyautogui.locateCenterOnScreen('Сюди картинку')

if button:
    pyautogui.click(button)

# Автоматизація клавіатури
pyautogui.press('space') # Натискає кнопку на клавіатурі
pyautogui.write('I`m bot') # Пише текст
pyautogui.write('I`m human', interval = 1) # Бот пише текст з інтервалом

