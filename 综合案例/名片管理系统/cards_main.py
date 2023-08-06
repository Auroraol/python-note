# -*-coding = utf-8 -*-
# @time: 2021/11/29 14:05
# @fAuthor:
# @File: cards_main.py
# @Software:PyCharm
import cards_tools


# 不用计数器，直接指定为True，就能不停循环，只有用户主动选择0时才退出循环因此在输入0的代码下方用break主动退出
while True:
    #  显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作")
    print("您选择的操作是【%s】"%action_str)

# 1，2，3是针对名片进了个操作
# 0是退出系统
# 其他内容输入错误，需要提示用户

# 1，2，3是针对名片进了个操作
    if action_str in ["1","2","3"]:
           #  新增名片
        if action_str == "1":
               cards_tools.new_cards()
           #  显示全部
        elif action_str == "2":
               cards_tools.show_caeds()
           #  查询名片
        elif action_str == "3":
               cards_tools.search_caeds()


# 0是退出系统
    elif action_str =="0":
            # 不用计数器，直接指定为True，就能不停循环，只有用户主动选择0时才退出循环因此在输入0的代码下方用break主动退出
        print("欢迎下次使用【名片管理系统】")
        break
        # pass关键字不会执行任何操作
        pass
# 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新输入")


