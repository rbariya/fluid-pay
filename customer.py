from utils import request


def create_customer(res_body, key):
	param = ['customer']
	return request('POST', param, res_body, key)

def get_customer(customer_id, key):
	param = ['customer', customerID]
	return request('GET', param, {}, key)

def update_customer(res_body, customer_id, key):
	param = ['customer', customerID]
	return request('POST', param, res_body, key)

def delete_customer(customer_id, key):
	param = ['customer', customer_id]
	return request('DELETE', param, {}, key)

