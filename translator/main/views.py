from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from translate import Translator
from translate import Translator

def home(request):
    if request.method == "POST":
        # text = request.POST["translate"]
        # language = request.POST["language"]

        text = request.POST.get("translate", "").strip()
        language = request.POST.get("language", "").strip()


        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        return HttpResponse(translation)
    return render(request, "main/index.html")