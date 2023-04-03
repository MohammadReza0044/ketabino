import random
import string

def invoice_generator():
	allowed_chars = ''.join((string.ascii_letters, string.digits))
	unique_id = ''.join(random.choice(allowed_chars) for _ in range(6))
	return unique_id

