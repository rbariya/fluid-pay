import requests


url_production = 'https://app.fluidpay.com/api'
url_sandbox = 'https://sandbox.fluidpay.com/api'
url_local_dev = 'http://localhost:8001/api'


def request(method, params, body, api_key):
	# url = ''
	# if environment == 'production':
	# 	url = url_production + '/' + '/'.join(params)
	# elif environment == 'sandbox':
	# 	url = url_sandbox + '/' + '/'.join(params)
	# elif enviroment == 'development':
	# 	url = url_local_dev + '/' + '/'.join(params)
	url = url_sandbox + '/' + '/'.join(params)
	headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'credentials': 'include',
			'Authorization': api_key
		}
	if method == 'GET':
		results = requests.get(url, headers=headers)
		print('get->',results)
	elif method == 'POST':
		print(body)
		results = requests.post(url, data=body, headers=headers)
		print('post->',results)
	elif method == 'DELETE':
		#TO:DO
		print('delete')
	return results.json()

# url = 'https://getsandbox.com/api/1/sandboxes/twilight-dawn-9515'
# api_key = 'api-3b16800e-56fd-45c3-8a05-cb4f1f3614c5'
# headers = {"API-Key": api_key}
# r = requests.get(url, headers)
# print(r.content)