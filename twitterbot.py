#!/usr/bin/env python
# -*- coding:utf-8 -*-


from bottle import route, run, template, request
from datetime import datetime

usertweet_list = []

@route('/hello/', method='GET')
@route('/hello/', method='POST')
def hello():

	# 箱を作る
	tweet_dict = {}
	
	# ツイートを箱のツイート部分に入れる
	tweet = request.forms.get('tweet')
	tweet_dict['tweet'] = tweet
	
	# ユーザーを箱のユーザー部分に入れる
	user = request.forms.get('user')
	tweet_dict['user'] = user
	
	current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	tweet_dict['current_time'] = current_time
	
	usertweet_list.append(tweet_dict)
	return template('hello', usertweet_list=usertweet_list)

run(host='localhost', port=8080, debug=True, reloader=True)

