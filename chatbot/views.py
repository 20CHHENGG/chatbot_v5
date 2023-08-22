from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
import dotenv
import openai
dotenv_file = os.path.join(".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    
openai.api_key = os.environ['OPENAI_API_KEY']
# Create your views here.


def askOpenAI(message):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=message,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # print(response)
    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = askOpenAI(message)
        
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html',)


