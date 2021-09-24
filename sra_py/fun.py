import requests

SR = "https://some-random-api.ml"

class Meme():
	def __init__(self , meme_: dict):
		self.caption_ = meme_['caption']
		self.category_ = meme_['category']
		self.image_url_ = meme_['image']
		self.id__ = meme_['id']

	@property
	def image_url(self):
		return self.image_url_

	@property
	def category(self):
		return self.category_

	@property
	def caption(self):
		return self.caption_

	@property
	def id_(self):
		return self.id__

	def save(self):
		try:
			filename = self.image_url.split('/')[-1]
			r = requests.get(self.image_url , allow_redirects = True)
			open(filename , 'wb').write(r.content)
			return True
		except:
			return False

def meme():
	r = requests.request("GET", f"{SR}/meme").json()
	return Meme(r)

def joke():
	r = requests.request("GET", f"{SR}/joke").json()
	return r['joke']

def base64(text: str , mode):
	text = text.replace(' ', '%20')

	if mode == "encode":
		r = requests.request("GET", f"{SR}/base64?encode={text}").json()
		return r['base64']

	elif mode == "decode":
		r = requests.request("GET", f"{SR}/base64?decode={text}").json()
		return r['base64']

	else:
		raise NotFound("Invalid Mode")

def chat_bot(key , message):
	r = requests.request("GET", f"{SR}/chatbot?message={message}&key={key}").json()
	return r

def minecraft(username):
	r = requests.request("GET", f"{SR}/mc?username={username}").json()
	return r

def bot_token(id_=None):
	if id_ is None:
		r = requests.request("GET", f"{SR}/bottoken").json()
		return r['token']
	else:
		try:
			r = requests.request("GET", f"{SR}/bottoken?id={id_}").json()
			return r['token']
		except:
			raise NotFound("Invalid ID")

def lyrics(title: str):
	title = title.replace(' ', '%20')
	r = requests.request("GET", f"{SR}/lyrcis?title={title}").json()
	return r