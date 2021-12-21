import os
from aip import AipOcr
from django.conf import settings

from .config import API_KEY,APP_ID,SECRET_KEY

class OCR(object):
    def __init__(self):
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    @staticmethod
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            content = fp.read()
            fp.close()
            return content

    def getResult(self, filePath, mode=0):
        '''
        返回OCR识别结果
        :param filePath: 图片路径
        :return: {'code': 0/1 （是否成功）,'text':str （信息）}
        '''
        image = OCR.get_file_content(filePath)

        options = {}
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["probability"] = "true"

        if mode == 0:
            "通用文字识别 高精度"
            res = self.client.basicAccurate(image,options)
        elif mode == 1:
            "手写文字"
            res = self.client.handwriting(image,options)
        elif mode == 2:
            "手写数字"
            res = self.client.numbers(image,options)
        else:
            raise KeyError("没有该模式！")

        output = {'code': 0,
                  'text': ''}
        # 出错情况
        if( 'error_code' in res):
            output['code'] = 0
            if(res['error_code'] == '17'):
                output['text'] = "每天流量超限额"
            else:
                output['text'] = '错误代码：{}'.format(res['error_code'])
        # 正常情况
        else:
            output['code'] = 1
            text = ''
            for elem in res['words_result']:
                text = text + elem['words'] + '\n'
            output['text'] = text
            txtPath = filePath.split('.')[0] + '.txt'
            with open(txtPath, 'w', encoding='utf-8') as f:
                f.write(text)

        return output


# if __name__ == '__main__':
#     test = OCR()
#     a = test.getResult('E:/Code/Python/django-project/smartocr/media/ocr/20211216/Remeber.png')
#     print(a['text'])