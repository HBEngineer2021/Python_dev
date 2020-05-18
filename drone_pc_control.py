#TelloTC.py
# -*- coding: utf-8 -*-
"""
Fri June 13 23:34:08 2019

@author: Aoi Dougami
"""

#CONTROL MANUAL
""""""""""""""""""
" 1 2        9 0 "
"                "
"  W          I  "
"A S D F  H J K L"
"                "
""""""""""""""""""
#commandtype
"""
 1 : takeoff '離陸'
 2 : land　'着陸'
 9 : streamon 'カメラ起動'
 0 : streamoff　'カメラ停止'
 W : forward　'前'
 S : back '後'
 A : right　’右’
 D : left　’左’
 I : flip forward　’前転’
 K : flip back　’バク転’
 J : flip right　’右転’
 L : flip left　’左転’
 F : up　’上昇’
 H : down　’下降’
 回転コマンド追加
 
"""
from pynput import keyboard
import socket
import threading
import sys
import time
import cv2

host = ''
port = 9000
locaddr = (host,port) 
tello_ip = '192.168.10.1'
tello_port = 8889
tello_address = (tello_ip , tello_port)
tello_video = 11111 "カメラポート番号が違う"
tello_stream = (tello_ip , tello_video)
socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = socket.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except:
            pass
        
recvThread = threading.Thread(target=recv)
recvThread.setDaemon(True)
recvThread.start()

try:
    socket.sendto('command'.encode('utf-8'),tello_address)
except:
    pass

try:
    socket.sendto('speed 30'.encode(encoding="utf-8"),tello_address)
except:
    pass

class VideoCamera(object):
    def __init__(self, socket, algorithm, target_color, stream_only, is_test,
                 speed):
        self.video = cv2.VideoCapture('udp://127.0.0.1:11111')

# The key combination to check(ホットキー設定)
COMBINATIONS = [
    {keyboard.KeyCode(char='1')},
    {keyboard.Key.shift, keyboard.KeyCode(char='1')}
]
COMBINATIONS1 = [
    {keyboard.KeyCode(char='2')},
    {keyboard.Key.shift, keyboard.KeyCode(char='2')}
]
COMBINATIONS2 = [
    {keyboard.KeyCode(char='9')},
    {keyboard.Key.shift, keyboard.KeyCode(char='9')}
]
COMBINATIONS3 = [
    {keyboard.KeyCode(char='0')},
    {keyboard.Key.shift, keyboard.KeyCode(char='0')}
]
COMBINATIONS4 = [
    {keyboard.KeyCode(char='w')},
    {keyboard.Key.shift, keyboard.KeyCode(char='W')}
]
COMBINATIONS5 = [
    {keyboard.KeyCode(char='s')},
    {keyboard.Key.shift, keyboard.KeyCode(char='S')}
]
COMBINATIONS6 = [
    {keyboard.KeyCode(char='a')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')}
]
COMBINATIONS7 = [
    {keyboard.KeyCode(char='d')},
    {keyboard.Key.shift, keyboard.KeyCode(char='D')}
]
COMBINATIONS8 = [
    {keyboard.KeyCode(char='i')},
    {keyboard.Key.shift, keyboard.KeyCode(char='I')}
]
COMBINATIONS9 = [
    {keyboard.KeyCode(char='k')},
    {keyboard.Key.shift, keyboard.KeyCode(char='K')}
]
COMBINATIONS10 = [
    {keyboard.KeyCode(char='j')},
    {keyboard.Key.shift, keyboard.KeyCode(char='J')}
]
COMBINATIONS11 = [
    {keyboard.KeyCode(char='l')},
    {keyboard.Key.shift, keyboard.KeyCode(char='L')}
]
COMBINATIONS12 = [
    {keyboard.KeyCode(char='f')},
    {keyboard.Key.shift, keyboard.KeyCode(char='F')}
]
COMBINATIONS13 = [
    {keyboard.KeyCode(char='h')},
    {keyboard.Key.shift, keyboard.KeyCode(char='H')}
]

# The currently active modifiers（コマンド送信を設定）

current = set()

def execute():
        try:
            socket.sendto('takeoff'.encode(encoding='utf-8'),tello_address)
            print('takeoff')
        except:
            pass
def execute1():
        try:
            socket.sendto('land'.encode('utf-8'),tello_address)
            print('land')
        except:
            pass
def execute2():
        try:
            time.process_time()
            socket.sendto('streamon'.encode('utf-8'),tello_address)
            print('streamon')
        except:
            pass
def execute3():
        try:
            time.process_time()
            socket.sendto('streamoff'.encode('utf-8'),tello_address)    
            print('streamoff')
        except:
            pass
def execute4():
        try:
            time.process_time()
            socket.sendto('forward 60'.encode('utf-8'),tello_address)    
            print('forward')
        except:
            pass
def execute5():
        try:
            time.process_time()
            socket.sendto('back 60'.encode('utf-8'),tello_address)    
            print('back')
        except:
            pass
def execute6():
        try:
            time.process_time()
            socket.sendto('right 60'.encode('utf-8'),tello_address)    
            print('right')
        except:
            pass
def execute7():
        try:
            time.process_time()
            socket.sendto('left 60'.encode('utf-8'),tello_address)
            print('left')    
        except:
            pass
def execute8():
        try:
            socket.sendto('flip f'.encode('utf-8'),tello_address)
            print('flip forward')    
        except:
            pass
def execute9():
        try:
            time.process_time()
            socket.sendto('flip b'.encode('utf-8'),tello_address)
            print('flip back')
        except:
            pass
def execute10():
        try:
            time.process_time()
            socket.sendto('flip r'.encode('utf-8'),tello_address)
            print('flip right')
        except:
            pass
def execute11():
        try:
            time.process_time()
            socket.sendto('flip l'.encode('utf-8'),tello_address)
            print('flip left')
        except:
            pass
def execute12():
        try:
            time.process_time()
            socket.sendto('up 60'.encode('utf-8'),tello_address)
            print('up')
        except:
            pass
def execute13():
        try:
            time.process_time()
            socket.sendto('down 60'.encode('utf-8'),tello_address)
            print('down')
        except:
            pass

#キーを押した時のコマンド呼び出す
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
    elif any([key in COMBO for COMBO in COMBINATIONS1]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS1):
            execute1()
    elif any([key in COMBO for COMBO in COMBINATIONS2]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS2):
            execute2()
    elif any([key in COMBO for COMBO in COMBINATIONS3]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS3):
            execute3()
    elif any([key in COMBO for COMBO in COMBINATIONS4]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS4):
            execute4()
    elif any([key in COMBO for COMBO in COMBINATIONS5]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS5):
            execute5()
    elif any([key in COMBO for COMBO in COMBINATIONS6]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS6):
            execute6()
    elif any([key in COMBO for COMBO in COMBINATIONS7]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS7):
            execute7()        
    elif any([key in COMBO for COMBO in COMBINATIONS8]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS8):
            execute8() 
    elif any([key in COMBO for COMBO in COMBINATIONS9]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS9):
            execute9() 
    elif any([key in COMBO for COMBO in COMBINATIONS10]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS10):
            execute10() 
    elif any([key in COMBO for COMBO in COMBINATIONS11]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS11):
            execute11()
    elif any([key in COMBO for COMBO in COMBINATIONS12]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS12):
            execute12()
    elif any([key in COMBO for COMBO in COMBINATIONS13]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS13):
        execute13()
     
#呼び出したコマンドをドローンに送信する     
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS1]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS2]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS3]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS4]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS5]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS6]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS7]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS8]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS9]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS10]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS11]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS12]):
        current.remove(key)
    elif any([key in COMBO for COMBO in COMBINATIONS13]):
        current.remove(key)
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
