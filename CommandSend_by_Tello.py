#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

tello_ip = '192.168.10.1'
tello_port = 8889

#udpソケット作成
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)

#コマンドモードを使うため'command'というテキストを投げる
socket.sendto('command'.encode('utf-8'),tello_address)

#10秒待機
time.sleep(10)
#離陸コマンド'takeoff'というテキストを送信
socket.sendto('takeoff'.encode('utf-8'),tello_address)

#10秒待機
time.sleep(10)
#着陸コマンド'land'というテキストを送信
socket.sendto('land'.encode('utf-8'),tello_address)
