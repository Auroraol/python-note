# -*-coding = utf-8 -*-
# @time: 2021/11/29 14:08
# @fAuthor:
# @File: cards_tools.py
# @Software:PyCharm

# 记录所以名字的名片字典
cards_list = []


def show_menu():
    """显示功能菜单"""
    print("*" * 50)
    print("欢迎使用【名片管理系统】v 1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("*" * 50)


def new_cards():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    #     提示用户输入详细信息
    name_str = input("请输入姓名信息")
    phone_str = input("请输入电话")
    qq_str = input("请输入QQ")
    email_str = input("请输入邮箱")

    #     使用用户输入的信息建立一个名片字典
    cards_dict = {"name": name_str,
                  "phone": phone_str,
                  "qq": qq_str,
                  "email": email_str}
    #     把名片字典添加到列表中
    cards_list.append(cards_dict)
    print(cards_list)

    #     提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)


def show_caeds():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")
    #     判断列表中是否有记录，如果没有提示用户
    if len(cards_list) == 0:
        print("当前没有任何记录，请使用新增功能添加")
        # return可以返回一个函数的执行结果，同时下方的代码不会执行
        return

    #     打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")
    # 打印分隔线
    print("=" * 50)

    #   思路遍历名片列表依次输出字典信息
    for cards_dict in cards_list:
        # 打印对应值
        print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"], cards_dict["phone"], cards_dict["qq"], cards_dict["Email"]))


def search_caeds():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    #     1提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名")

    # 2遍历·名片列表，查询要搜索的·姓名，如果没有需要提示用户
    for cards_dict in cards_list:
        if cards_dict["name"] == find_name:
            print("姓名\t\t电梯\t\tqq\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"],
                                            cards_dict["phone"],
                                            cards_dict["qq"],
                                            cards_dict["email"]))
            #  针对找到的名片记录执行修改和删除的操作
            deal_card(cards_dict)

            break

    else:
        print("抱歉，没有找到%s" % find_name)


def deal_card(find_dictt):
    """处理查找到的名片

    :param find_dictt: 查找到的名片
    """
    print(find_dictt)
    action_str = input("请操作要执行的操作 "
                       " [1] 修改  [2] 删除  [0] 返回上一级")
    if action_str == "1":
        find_dictt["name"] = input_card_info(find_dictt["name"], "姓名: ")
        find_dictt["phone"] = input_card_info(find_dictt["phone"], "电话: ")
        find_dictt["qq"] = input_card_info(find_dictt["qq"], "qq: ")
        find_dictt["email"] = input_card_info(find_dictt["email"], "邮箱：")

        print("修改名片成功")
        pass
    elif action_str == "2":
        cards_list.remove(find_dictt)
        print("删除名片成功")
        pass


def input_card_info(dict_value, tip_message):
    """输入名片信息"""
    """
    :param dict_value: 
    :param tip_message: 
    :return: 
    """
    # 1提示用户输入内容
    result_str = input(tip_message)

    # 2针对用户输入进行判断，如果用户输入的内容直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3如果用户没有输入内容，返回字典中原有的值
    else:
        return dict_value
    pass
