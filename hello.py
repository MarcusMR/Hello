import keyboard
i = 0
while 1:
    i = 1 + i
    print("hello world! {}".format(i))
    if keyboard.is_pressed('q'):
        break


    
    