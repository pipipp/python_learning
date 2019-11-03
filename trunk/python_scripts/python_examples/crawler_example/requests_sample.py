""" Request反反爬虫解决方案：
1:
使用随机请求头:
    from fake_useragent import UserAgent
    ua = UserAgent(use_cache_server=False)
    headers = {'User-Agent': ua.random}
2:
使用带请求参数的request，添加referer等：
    GET: params = {"wd": 'python'}
    POST: data = {"wd": 'python'}
3:
使用代理突破限制IP访问频率，或者减少访问频率（加延时）:
    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }
4:
使用Session保持会话状态：
    s = requests.Session()
    response = s.get(url)
5:
登陆网站时需要输入账户密码则调用auth参数传入即可:
    from requests.auth import HTTPBasicAuth
    response = requests.get(url, auth=HTTPBasicAuth('username', 'password'))
"""

import random
import requests
from requests.exceptions import ReadTimeout, ConnectionError, RequestException
from urllib.parse import urljoin, quote

GET = 'get'
POST = 'post'


class Crawler(object):

    def __init__(self, url=None):
        self.source_url = url

    @staticmethod
    def random_headers():
        ua_list = [
            # Chrome UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/73.0.3683.75 Safari/537.36',
            # IE UA
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            # Microsoft Edge UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        ]
        ua = random.choice(ua_list)
        return ua

    def get_web_page(self, request_url=None, purpose=GET):
        """
        请求网页数据并返回响应结果
        :param request_url: 请求的URL
        :param purpose: 请求的协议
        :return:
        """
        request_url = request_url or self.source_url
        headers = {
            "User-Agent": self.random_headers(),
        }
        try:
            if purpose == GET:
                response = requests.get(request_url, headers=headers, timeout=60)
            else:
                response = requests.post(request_url, headers=headers, timeout=60)

            if response.status_code == 200:
                return response
                # response.text # 网页源码 [type: str]
                # response.headers # 头部信息 [type: dict]
                # response.json() # json格式 [type: json]
                # response.content # 二进制数据 [type: bytes]
                # response.cookies # 网页cookies [type: dict]
                # response.history # 访问的历史记录 [type: list]
            else:
                return None
        except Exception as ex:
            print('Get web page error: {}'.format(ex))


    @staticmethod
    def main():
        # 中文转换字节码
        # like = quote('你好')
        # print(like)

        # 获取网页内容
        response = crawler.get_web_page(purpose=GET)
        if response:
            print('Response:\n{}'.format(response.text))


if __name__ == '__main__':
    resource_url = 'https://www.baidu.com'
    crawler = Crawler(url=resource_url)
    crawler.main()