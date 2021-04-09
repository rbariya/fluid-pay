from utils import request


def create_user(res_body, key):
	param = ['user']
	return request('POST', param, res_body, key)


def get_user(user_id, key):
	params = ['user', user_id]
	return request('GET', params, {}, key)


def get_users(key):
	params = ['user']
	return request('GET', params, {}, key)


def delete_user(user_id, key):
	params = ['user', user_id]
	return request('DELETE', params, {}, key)
