from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def sayhello(request):
	print "got to ajax"
	return simplejson.dumps({'message':'Hello World'})