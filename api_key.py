from utils import request


def create_key(req_body, key):
	params = ['user', 'apikey']
	return request('POST', params, req_body, key)


def get_key(key):
	params = ['user', 'apikeys']
	return request('GET', params, {}, key)


def delete_key(api_key, key):
	params = ['user', 'apikey', api_key]
	return request('DELETE', params, {}, key)