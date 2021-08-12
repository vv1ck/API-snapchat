import requests,time
r = requests.session()
TIM = time.time()




def reporting():
	
	user = 'your username'
	TRG = 'target'
	account_token = 'Token_your_account'


	url = 'https://app.snapchat.com/reporting/inapp/v1/user'
	auth_Token='v8:0188602275FABD0FC79BD401CE818EC1:8C2CACF1237C19763BE4A2CD387F3968EBB2C7C7A787CB569B8E8C9682D964FA2DE8AC400EBEC2197604B9E2E45915A73EA40C647C214141A6840ED20DA4ECEC7EE6796FE264B6E43C83C1ACA1F5BC0E864D3FF56080DA0E89F5521552D884A26F9953968B6044ADE50DB11082653571EBDE681B429323BE2EAE5FCEEA2BF1ABE58D21CBCE8A287A27AF14FDCC7885E220E92BA3375FF2D3DC287C4E8E6022FED911DDC7DA299A943A6ED3B69A6723285FB3764F79DAE58CF77596055421735F440607B9D466DE4DA46A5945F097D912C6F4A127C834143FD01F2DC70F3E02D92AA1558114402A46A8AB9BAA5AB47279D78EBE95D77F3466AA95B06CA4ED2EF839D7962BCEF8F32522F2797EE96380CA8FA77AF63B6BC41296A58D094CDB12C4'
	
	head={
		'Host': 'app.snapchat.com',
		'X-Snapchat-Uuid': '328E59AD-7DF6-4AAA-B9F5-6128F97659C8',
		'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
		'Accept': '*/*',
		'Accept-Locale': 'ar_SA@calendar=gregorian',
		'X-Snapchat-Client-Auth-Token':auth_Token,
		'Content-Length': '223',
		'User-Agent': 'Snapchat/10.47.1.1 (iPhone11,2; iOS 13.2.3; gzip)',
		'Accept-Language': 'ar-SA;q=1, en-SA;q=0.9',
		'Accept-Encoding': 'gzip, deflate',
		'Connection': 'close'}
	
	data={
	'context':'',
	'friend_link_type': '1',
	'reason_id':'report_user_reason_theyre_creepy_or_annoying',
	'reported': TRG,
	'req_token': account_token,
	'timestamp': TIM,
	'username': user,}
	
	req=r.post(url,headers=head,data=data)
	print(req)
	print(req.text)

reporting()
