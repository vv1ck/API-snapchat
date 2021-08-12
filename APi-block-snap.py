
# APi block followers



username = 'your user'
addUSR = 'frind user'
account_token = 'Token_your_account'
id_your_frind = 'id_your_frind'




url = 'https://app.snapchat.com/bq/friend'


headers = {
'Host': 'app.snapchat.com',
'X-Snapchat-Uuid': 'E302C4E6-9ADE-4B37-B071-0807F079AB71',
'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
'Accept': 'application/x-protobuf',
'Accept-Locale': 'ar_SA@calendar=gregorian',
'X-Snapchat-Client-Auth-Token': 'v8:8286DABBD850AD978BEFA39734EB9517:8C2CACF1237C19763BE4A2CD387F3968EBB2C7C7A787CB569B8E8C9682D964FA2DE8AC400EBEC2197604B9E2E45915A73EA40C647C214141A6840ED20DA4ECEC7EE6796FE264B6E43C83C1ACA1F5BC0E864D3FF56080DA0E89F5521552D884A26F9953968B6044ADE50DB11082653571EBDE681B429323BE2EAE5FCEEA2BF1ABE58D21CBCE8A287A27AF14FDCC7885E220E92BA3375FF2D3DC287C4E8E6022FED911DDC7DA299A943A6ED3B69A6723285FB3764F79DAE58CF77596055421735F440607B9D466DE4DA46A5945F097D912C6F4A127C834143FD01F2DC70F3E02D92AA1558114402A46A8AB9BAA5AB47279D78EBE95D77F3466AA95B06CA4ED2EF839D7962BCEF8F32522F2797EE96380CA8FA77AF63B6BC41296A58D094CDB12C4',
'Content-Length': '216',
'User-Agent': 'Snapchat/10.45.0.25 (iPhone11,2; iOS 13.2.3; gzip)',
'Accept-Language': 'ar-SA;q=1, en-SA;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'close'


data = {
'action': 'block',
'block_reason_id': '2',
'friend': addUSR,
'friend_id': id_your_frind,
req_token: account_token,
'timestamp': '',
'username': username}
