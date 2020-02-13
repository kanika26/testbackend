def cors_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = get_response(request)
        try:
            response["Access-Control-Allow-Origin"] = request.META["HTTP_ORIGIN"]
        except:
            pass
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
        response["Access-Control-Allow-Methods"] = "*"
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
