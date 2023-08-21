import requests
class Client():
	def __init__(self):
		self.api="https://clck.ru/--"
	def get_link(self,url:str):
		return requests.post(f"{self.api}?url={url}").text