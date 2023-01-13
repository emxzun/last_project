

class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # print('Hellow')
        # request.hello = 'My name is Sam'
        response = self.get_response(request)

        return response
