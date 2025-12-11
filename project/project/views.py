from django.http import HttpResponse


class ViewsProject:
    def test_view(self, request):
        return HttpResponse("Essa é uma página de teste.")

    def home(self, request):
        return HttpResponse("Bem-vindo ao home page!")