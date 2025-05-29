# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define d = Character('Дракон', color="#f71a1a") # dragon
define n1 = Character(None, kind = nvl, what_color="#000000", size = 16) # narrator1
define n2 = Character(None, kind = nvl, what_color="#000000", size = 16) # narrator2

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    d "True Dragon!"
    
    nvl clear
    
    #jump global_map

    return
