from django.http import JsonResponse


def test(request):
    test_json = {'hello': 'world', 'this': 'is test'}
    return JsonResponse(test_json)
