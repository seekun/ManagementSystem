# import requests
# from lxml import etree
# import sys
# from bs4 import BeautifulSoup
# import io
# import re
# from PIL import Image
# from gevent import monkey
#
# monkey.patch_all()
# from keras.models import load_model
# from keras.backend import image_data_format
# import numpy as np
# import tensorflow as tf
#
# img_rows, img_cols = 12, 22
# if image_data_format() == 'channels_first':
#     input_shape = (1, img_rows, img_cols)
# else:
#     input_shape = (img_rows, img_cols, 1)
# import string
#
# CHRS = string.ascii_lowercase + string.digits
# model = load_model(r'./cnn_dama_final.h5')
# graph = tf.get_default_graph()
#
#
# def handle_split_image(image):
#     '''
#     input: image is PIL.Image.open return value
#     '''
#     im = image.point(lambda i: i != 43, mode='1')
#     ## 放大后滤波再二值
#     im = im.convert('L')  # .filter(ImageFilter.MedianFilter())
#     im = im.point(lambda i: i > 25, mode='1')
#     y_min, y_max = 0, 22  # im.height - 1 # 26
#     split_lines = [5, 17, 29, 41, 53]
#     ims = [im.crop([u, y_min, v, y_max]) for u, v in zip(split_lines[:-1], split_lines[1:])]
#     # w = w.crop(w.getbbox()) # 切掉白边 # 暂不需要
#     return ims
#
#
# def _predict_image(images):
#     global graph
#     Y = []
#     for i in range(4):
#         im = images[i]
#         test_input = np.concatenate(np.array(im))
#         test_input = test_input.reshape(1, *input_shape)
#         y_probs = None
#         with graph.as_default():
#             y_probs = model.predict(test_input)
#         y = CHRS[y_probs[0].argmax(-1)]
#         Y.append(y)
#         # plt.subplot(1,4,i+1)
#         # plt.imshow(im, interpolation='none')
#         # plt.title("Predicted {}".format(y))
#     return ''.join(Y)
#
#
# def getInfor(response, xpath):
#     content = response.content.decode('gb2312')  # 网页源码是gb2312要先解码
#     selector = etree.HTML(content)
#     infor = selector.xpath(xpath)[0]
#     return infor
#
#
# # main
#
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# studentnumber = 'E11614016'  # sys.argv[1]   input("请输入学号：")
# password = 'a123456'  # sys.argv[2]   input("请输入密码：")
# s = requests.session()
# url = "http://xk1.ahu.cn/default2.aspx"
# response = s.get(url.strip())
# selector = etree.HTML(response.content)
# __VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
# __EVENTVALIDATION = selector.xpath('//*[@id="form1"]/input/@value')[1]
# imgUrl = "http://xk1.ahu.cn/CheckCode.aspx"
# imgresponse = s.get(imgUrl.strip(), stream=True)
# # print(s.cookies)
# image = imgresponse.content
# image_file = io.BytesIO(image)
# image1 = Image.open(image_file)
# verify_code = _predict_image(handle_split_image(image1))
# # print('预测结果为:', verify_code)
# data = {
#     "__VIEWSTATE": __VIEWSTATE,
#     "__EVENTVALIDATION": __EVENTVALIDATION,
#     "txtUserName": studentnumber,
#     "TextBox2": password,
#     "txtSecretCode": verify_code,
#     "Button1": "",
#     "lbLanguage": "",
#     "RadioButtonList1": "%D1%A7%C9%FA"
# }
# headers = {
#     "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
# }
# response = s.post(url, data=data, headers=headers)
# pat = r'<title>(.*?)</title>'
# x = re.findall(pat, response.text)
# if ('alert' in response.text):
#     errorPat = r'alert\((.*?)\)'
#     getError = re.findall(errorPat, response.text)
#     # print(getError)
#     if (getError[0] == '验证码不正确！！'):
#         print('3')
#     elif (getError[0] == '密码错误！！'):
#         print('2')
#     elif (getError[0] == '用户名不存在或未按照要求参加教学活动！！'):
#         print('1')
# # 登陆教务系统
# if (sys.argv[3] == '1'):
#     # 得到登录信息，个人感觉有点多余。
#     # 获取学生基本信息
#     text = getInfor(response, '//*[@id="xhxm"]/text()')
#     text = text.replace(" ", "")
#     print(text)
#     kburl = "http://xk1.ahu.cn/xskbcx.aspx?xh=" + studentnumber + "&xm=1&gnmkdm=N121603"
#     headers = {
#         "Referer": "http://xk1.ahu.cn/xs_main.aspx?xh=" + studentnumber,
#         "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
#     }
#     response = s.get(kburl, headers=headers)
#     html = response.content.decode("gb2312")
#     selector = etree.HTML(html)
#     content = selector.xpath('//*[@id="Table1"]/tr/td/text()')
#     for each in content:
#         print(each)
# elif (sys.argv[3] == '2'):
#     cjurl = "http://xk1.ahu.cn/xskbcx.aspx?xh=" + studentnumber + "&xm=1&gnmkdm=N121603"
#     headers = {
#         "Referer": "http://xk1.ahu.cn/xscjcx.aspx?xh=" + studentnumber + "&xm=1&gnmkdm=N121605",
#         "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
#     }
#     dataCj = {
#         "ddlXN": "2017-2018",
#         "ddlXQ": "2"
#     }
#     response = s.get(cjurl, data=dataCj, headers=headers)
#     html = response.content.decode("gb2312")
