import eel
import pyautogui
import pygame
import time
from datetime import datetime

file = '1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

pyautogui.FAILSAFE = True
eel.init("web")

@eel.expose
def mouse(x):
    # Движение мышкой на 15 минут
    if x == 15:
        # Даем 10 секунд что бы зайти в нужную программу 
        time.sleep(10)
        # Цыкл работает 15 минут
        for _ in range(15):
            # Движение влево (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    

            # Движение вниз (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вправа (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вверх (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
            
        # Запускаем мелодию после окончания цыкла (15 минут)
        pygame.mixer.music.play()
        # Осталавниваем мелодию (если двигаем мышкой)
        while True:
            x = pyautogui.position()
            time.sleep(1)
            if pyautogui.position() != x:
                pygame.mixer.music.pause()
                break
    
    # Движение мышкой на 30 минут
    elif x == 30:
        # Даем 10 секунд что бы зайти в нужную программу 
        time.sleep(10)
        # Цыкл работает 30 минут
        for _ in range(30):
            # Движение влево (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    

            # Движение вниз (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вправа (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вверх (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
            
        # Запускаем мелодию после окончания цыкла (30 минут)
        pygame.mixer.music.play()
        # Осталавниваем мелодию (если двигаем мышкой)
        while True:
            x = pyautogui.position()
            time.sleep(1)
            if pyautogui.position() != x:
                pygame.mixer.music.pause()
                break

    # Движение мышкой на 1 час
    elif x == 1:
        # Даем 10 секунд что бы зайти в нужную программу 
        time.sleep(10)
        # Цыкл работает 1 час
        for _ in range(60):
            # Движение влево (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    

            # Движение вниз (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вправа (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вверх (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
            
        # Запускаем мелодию после окончания цыкла (1 час)
        pygame.mixer.music.play()
        # Осталавниваем мелодию (если двигаем мышкой)
        while True:
            x = pyautogui.position()
            time.sleep(1)
            if pyautogui.position() != x:
                pygame.mixer.music.pause()
                break

    # Движение мышкой 2 часа
    elif x == 2:
        # Даем 10 секунд что бы зайти в нужную программу 
        time.sleep(10)
        # Цыкл работает 2 часа
        for _ in range(120):
            # Движение влево (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    

            # Движение вниз (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вправа (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вверх (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
            
        # Запускаем мелодию после окончания цыкла (2 часа)
        pygame.mixer.music.play()
        # Осталавниваем мелодию (если двигаем мышкой)
        while True:
            x = pyautogui.position()
            time.sleep(1)
            if pyautogui.position() != x:
                pygame.mixer.music.pause()
                break

    # Движение мышкой до 6 часов вечера      
    elif x == 6:
        # Даем 10 секунд что бы зайти в нужную программу 
        time.sleep(10)
        # Цыкл рфботает до 6 часов вечера
        while datetime.now().hour != 18:
            # Движение влево (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    

            # Движение вниз (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вправа (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
                
            # Движение вверх (занимает 5 секунд)
            for _ in range(5):
                pyautogui.move(-10,-10,duration=0.5)
                for _ in range(1):
                    x = pyautogui.position()
                    time.sleep(0.5)
                    if pyautogui.position() != x:
                        return
            
            # Пауза (занимает 10 секунд)
            for _ in range(10):
                x = pyautogui.position()
                time.sleep(1)
                if pyautogui.position() != x:
                    return    
            
        # Запускаем мелодию после окончания цыкла (в 18:00)
        pygame.mixer.music.play()
        # Осталавниваем мелодию (если двигаем мышкой)
        while True:
            x = pyautogui.position()
            time.sleep(1)
            if pyautogui.position() != x:
                pygame.mixer.music.pause()
                break
    


eel.start("main.html", size=(450, 370))
    





    