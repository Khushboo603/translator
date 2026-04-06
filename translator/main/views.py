from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages # added for newsletter
from .models import newslatteremail # added for newsletter

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
        # elif 'subscribe' in request.POST:
        #     email = newslatteremail()
        #     email.userEmail = request.POST.get("email")
        #     email.save()
        #     messages.info(request, 'You have successfully subscribed to your newslatter.')
        # elif 'unsubscribe' in request.POST:
        #     newslatteremail.objects.get(
        #         userEmail = request.POST.get("email")
        #     ).delete()
        #     messages.info(request, 'Sorry to see you!!!')
        elif 'subscribe' in request.POST:
            # email = newslatteremail()
            try:
                user_email = request.POST.get("email")

                if not user_email:
                    raise ValeError("Email is required")

                if newslatteremail.objects.filter(userEmail=user_email).exists():
                    messages.warning(request, "You are already subscribed!")
                else:
                    email = newslatteremail(userEmail=user_email)
                    email.save()
                    messages.success(request, 'You have successfully subscribed to your newslatter.')
            except Exception as e:
                messages.error(request, f"Something went wrong: {str(e)}")


        elif 'unsubscribe' in request.POST:
            try:
                user_email = request.POST.get("email")

                if not user_email:
                    raise ValeError("Email is required")


                obj = newslatteremail.objects.get(userEmail = user_email)
                obj.delete()
                messages.success(request, 'Sorry to see you!!!')
            
            except newslatteremail.DoesNotExist:
                messages.error(request, "Email not found!")

            except Exception as e:
                messages.error(request, f"Something went wrong: {str(e)}")
    return render(request, "main/index.html")