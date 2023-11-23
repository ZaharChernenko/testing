from django.http import HttpResponse


def helloRender(request):
    name = request.GET.get("name")
    message = request.GET.get("message")
    if name is not None and message is not None:
        return HttpResponse(f"<h1>Hello {name}! {message}!</h1>")
    elif name is None and message is not None:
        return HttpResponse("<h1>Привет, как тебя зовут?</h1>")
    elif name is not None and message is None:
        return HttpResponse(f"<h1>Hello {name}! Будем дружить?</h1>")
    return HttpResponse(f"<h1>Просто одинокий сайт...</h1>")
