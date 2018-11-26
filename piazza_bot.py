from piazza_api import Piazza
from SyllableCounter import CountSyllables
from secrets import USER_NAME, USER_PASS


class PiazzaBot():
	def __init__(self):
		self.p = Piazza()
		self.p.user_login(USER_NAME, USER_PASS)
		self.uid = self.p.get_user_profile()['user_id']

		# classes = self.p.get_user_classes()

		self.si206 = self.p.network("jlp6m1ynp9713y")

	def do_bot(self):
		posts = self.si206.search_feed("lecture")

		for post in posts:
			id = post[u'id']
			print(self.si206.get_post(id)[u'history'][0][u'content'])
			print("\n\n")

			# pcontent = "I also had this question"
			# self.si206.create_followup(post, pcontent)




if __name__ == '__main__':
	bot = PiazzaBot()
	bot.do_bot()
