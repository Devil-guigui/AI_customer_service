#!/user/bin/env python3
# -*- coding: utf-8 -*--

'''
文件描述：基于微信公众号实现AI客服
作者：鬼鬼
邮箱：guigui@wtugui.me
时间：2019-6-29 16:13
'''

import urllib.request
import urllib.parse
import os

#os.system("color 5F")
os.system("title 聊天机器人小程序 By:鬼鬼")

def get_robot_replay(question):
    '''
    函数功能：对于特定问题进行特定回复，对于非特定问题进行智能回复

    参数描述：
    question 聊天内容或问题

    返回值：str,回复内容
    '''

    if "你叫什么名字" in question:
        answer = "我叫鬼鬼"
    elif "你多少岁" in question:
        answer = "18岁哦"
    elif "你爸爸是谁" in question:
        answer = "鬼鬼"
    elif "你有多少钱" in question:
        answer = "很多很多哦"
    elif "你是GG还是MM" in question:
        answer = "你猜"
    else:
        try:
            # 调用NLP接口实现智能回复
            parms = urllib.parse.urlencode({'msg': question}).encode()  # 接口参数需要进行URL编码
            req = urllib.request.Request("http://api.itmojun.com/chat_robot",parms,method="POST")  #创建
            answer = urllib.request.urlopen(req).read().decode()  # 调用接口，（即向目标服务器发出HTTP请求，并获取服务器的响应数据）
        except Exception as e:
            answer = "AI机器人出现故障！（原因：%s）" % e
    return answer

if __name__ == '__main__':
    # 测试get_robot_replay函数
    # print(get_robot_replay("你叫什么名字"))
    # print(get_robot_replay("武汉天气如何"))
    # print(get_robot_replay("你到底是谁"))
    # print(get_robot_replay("你爸爸是谁"))
    # print(get_robot_replay("叫爸爸"))
    print("请输出任何内容开始和小魔仙聊天：")
    while True:
        question = input("\n我说：")
        answer = get_robot_replay(question)
        print("\n小魔仙说: %s" % answer)




