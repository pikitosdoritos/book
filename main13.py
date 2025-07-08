#! python3
# main13.py - Запускає карту в браузері, витягуючи поштовий адрес із командного рядка чи буфера обміну


import webbrowser, sys, pyperclip

if len(sys.argv) > 1: 
    # Отримання поштового адресу із командного рядка
    address = ''.join(sys.argv[1:])

else:
    # Отримання поштового адресу з командного рядка
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

print(address)