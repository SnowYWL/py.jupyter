#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import time
import random
import platform
import threading

def clear_screen():

    os_name = platform.system()
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


user_input = None

def get_input(prompt):

    global user_input
    user_input = input(prompt)

def memory_game():
    global user_input
    print("请选择难度级别（输入对应的数字）：\n1. 简单\n2. 中等\n3. 困难\n4. 非常困难")
    difficulty = input("你的选择是：")
    difficulty_level = int(difficulty)
    
    if difficulty_level == 1:
        n = 2
    elif difficulty_level == 2:
        n = 3
    elif difficulty_level == 3:
        n = 4
    elif difficulty_level == 4:
        n = 5
    else:
        print("无效的选择，游戏将使用默认难度（简单）.")
        n = 2

    numbers = [random.randint(0, 9) for _ in range(n)]
    round_passed = 0

    print("游戏开始！请记住下面的数字：")
    for number in numbers:
        print(number)
        time.sleep(1)
        clear_screen()

    try:
        while True:
            new_number = random.randint(0, 9)
            numbers.append(new_number)
            
            print(f"新的数字是：{new_number}")
            time.sleep(2)
            clear_screen()
            

            user_input = None
            input_thread = threading.Thread(target=get_input, args=("请输入之前的数字：",))
            input_thread.start()
            input_thread.join(timeout=2)  # 等待2秒
            
            if not input_thread.is_alive():
                expected_number = numbers[-n-1]
                if user_input is not None and int(user_input) == expected_number:
                    round_passed += 1
                    print("回合成功！进入下一回合。")
                    time.sleep(1)
                    clear_screen()
                else:
                    print(f"游戏失败！你通过了{round_passed}回合。正确数字是：{expected_number}")
                    break
            else:
                print(f"输入超时！游戏失败。你通过了{round_passed}回合。")
                break
    except Exception as e:
        print(f"游戏异常结束：{e}")
    finally:
        input("按任意键退出...")


memory_game()


# In[ ]:




