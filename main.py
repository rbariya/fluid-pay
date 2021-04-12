# from api_key import create_key, get_key
# from customer import create_customer, get_customer, delete_customer
# from transactions import do_transaction, get_transaction_status, refund_transaction
# from users import create_user, get_user, get_users, delete_user
import requests

url_sandbox = 'https://sandbox.fluidpay.com/api'

class FluidPay(object):

	def __init__(self):
		self.api_key = 'settings.FLUID_PAY_API_KEY'
	

	def request_handler(self, req_method, params, body={}):
		url_sandbox = 'https://sandbox.fluidpay.com/api'
		# url = url_sandbox + '/' + '/'.join(params)
		
		url = f"{url_sandbox}/{'/'.join(params)}/"
		print(url)
		headers = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'credentials': 'include',
			'Authorization': self.api_key
		}
		if req_method == 'GET':
			results = requests.get(url, headers=headers)
			print('get->',results)
		elif req_method == 'POST':
			print(body)
			results = requests.post(url, data=body, headers=headers)
			print('post->',results)
		# elif req_method == 'DELETE':
		# 	#TO:DO
		# 	print('delete')
		return results.json()


	#implement in django views
	#api key
	# def create_key(self, req_body):
	# 	return create_key(req_body, self.api_key)

	# def get_key(self):
	# 	return get_key(self.api_key)


	# #users
	# def create_user(self, req_body):
	# 	return create_user(req_body, self.api_key)

	# def get_user(self, user_id):
	# 	return get_user(user_id, self.api_key)

	# def get_users(self):
	# 	return get_users(self.api_key)


	# #customer
	# def create_customer(self, req_body):
	# 	return create_customer(req_body, self.api_key)

	# def get_customer(self, customer_id):
	# 	return get_customer(customer_id, self.api_key)

	# def delete_customer(self, customer_id):
	# 	return delete_customer(customer_id, self.api_key)


	# # initiate transaction
	# def do_transaction(self, req_body):
	# 	return do_transaction(req_body, self.api_key)

	# def get_transaction_status(self, transaction_id):
	# 	return get_transaction_status(transaction_id, self.api_key)

	# def refund_transaction(self, transaction_id):
	# 	return refund_transaction(transaction_id, self.api_key)
raw = "{'username':'testmerchant43','name':'test user','phone':'6305555555','email':'info@website.com','timezone':'ETC/UTC','password':'Test12345678','status':'active','role':'admin'}"
print(raw)
fp = FluidPay()
fp.request_handler('GET',['users']) #get all users
fp.request_handler('POST', ['user'], body=raw) #for creting new user




# fp.create_key({
# 		'name': "{ name }",
#         'type': "api"
# 	})

# fp.create_user({
# 		'username': "testmerchant43",
# 	    'name': "test user",
# 	    'phone': "6305555555",
# 	    'email': "info@website.com",
# 	    'timezone': "ETC/UTC",
# 	    'password': "T@est12345678",
# 	    'status': "active",
# 	    'role': "admin",
# })