from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# from translate import Translator
from translate import Translator
import wikipedia

def home(request):
    # translated_text = ""
    # wiki_result = ""

    if request.method == "POST":
        # text = request.POST["translate"]
        # language = request.POST["language"]

        # # text = request.POST.get("translate", "").strip()
        # # language = request.POST.get("language", "").strip()


        # translator = Translator(to_lang=language)
        # translation = translator.translate(text)
        # return HttpResponse(translation)

        # print("line 21 >>>>",request.POST)
        if "translated_btn" in request.POST:
            text = request.POST["translate"]
            language =  request.POST["language"]

            try:
                translator = Translator(to_lang=language)
                translation = translator.translate(text)
            except Exception:
                translation = "Translation failed. Try different text or language."
            return HttpResponse(translation)
        elif "wiki_btn" in request.POST:
        #    print("line 36 >>>>",request.POST) 
            search = request.POST["search"]

            try:
                result = wikipedia.summary(search, sentences = 3)
            except:
                return HttpResponse("Wrong Input")
            return render(request,"main/index.html",{"result":result})
    return render(request, "main/index.html")