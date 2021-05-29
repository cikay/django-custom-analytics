from django.http import HttpRequest


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        print("REQUEST IN CUSTOM MIDDLEWARE", request)
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('user_agent', request.user_agent)
        for key, value in request.user_agent.__dict__.items():
            print("key", key, "value", value)
        if request.user_agent.is_mobile:
            print("mobile")
        elif request.user_agent.is_tablet:
            print("Tablet")
        elif request.user_agent.is_pc:
            print("PC")
        elif request.user_agent.is_bot:
            print("Bot")
        else:
            print("bilinmeyen")
        print("user agent device family", request.user_agent.device.family)
        print("request.user_agent.browser.version_string",
              request.user_agent.browser.version_string)
        print("request.user_agent.os.family",
              request.user_agent.os.family)
        print("request.user_agent.os.version_string",
              request.user_agent.os.version_string)

        # http_request = from_rest_to_http_request(request)
        # Tracker.objects.create_from_request(
        #     request, "")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


def from_rest_to_http_request(rest_request):
    http_request = HttpRequest()
    return http_request
