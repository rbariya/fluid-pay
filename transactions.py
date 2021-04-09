from utils import request


def do_transaction(res_body, key):
	param = ['transaction']
	return request('POST', param, reqBody, key)


def get_transaction_status(transaction_id, key):
	param = ['transaction', transactionID]
	return request('GET', param, {}, key)

def refund_transaction(res_body, transaction_id, key):
	param = ['transaction', transactionID, 'refund']
	return request('POST', param, reqBody, key)