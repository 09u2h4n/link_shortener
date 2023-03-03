import requests
from urllib.parse import quote
from random import choices
from string import ascii_lowercase, digits

class urlShort(object):
    def __init__(self) -> None:
        base_is_url = "https://is.gd/"
        base_v_url = "https://v.gd/"
        if requests.get(url=base_is_url).status_code == 200:
            self.base_url = base_is_url
        else:
            self.base_url = base_v_url
        chars = ascii_lowercase+digits+"_"
        self.random_path = "".join(choices(chars, k=6))

    def short_link(self, link:str, path="random", logstats=False, proxies={}):
        if path.lower() == "random":
            short_url = self.random_path
        else:
            short_url = path
        if logstats:
            logstats = 1
        else:
            logstats = 0
        format = "simple"
        link = f"{link[0:8]}{quote(link[8:])}"
        main_url = f"{self.base_url}create.php?url={link}&format={format}&shorturl={short_url}&logstats={logstats}"
        response = requests.get(url=main_url,proxies=proxies)
        return response.text

    def lookup(self, link:str, proxies={}):
        format = "simple"
        url = f"{self.base_url}forward.php?shorturl={link}&format{format}"
        response = requests.get(url=url, proxies=proxies)
        return response.text
