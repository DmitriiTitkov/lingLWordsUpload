import requests


class LinguaLeo():
    """This class is connector to lingualeo.com site. It provides basic authentication """
    def __init__(self, email, password='y7S5D9'):
        self.email = email
        self.password = password
        self.cookies = ""
        self.auth()

    def auth(self):
        url= "http://api.lingualeo.com/api/login"
        auth_paylod = {'email': self.email, 'password': self.password}
        auth_response = self.get_content(url, auth_paylod)
        self.cookies = auth_response.cookies

    def add_word(self, word):
        url = "http://api.lingualeo.com/addword"
        params = {"word": word}
        return self.get_content(url, params=params)

    def get_translate(self, word):
        url = "http://api.lingualeo.com/gettranslates"
        params = {"word": word}
        site_response = self.get_content(url, params)
        if not site_response.json()['error_msg'] and site_response.json()['translate']:
            return site_response.json()['translate'][0]['value']

    def get_content(self, url, data="", params=""):
        response = requests.post(url, data=data, params=params, cookies=self.cookies)
        return response



