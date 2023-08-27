from django.shortcuts import render, redirect
from django.http import JsonResponse
import os
import openai
openai.api_key = os.environ.get('OPENAI_API_KEY')
# Create your views here.
MODEL_ID = "gpt-3.5-turbo"

def askOpenAI(message):
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=[{"role":"system","content":message}],
    )
    # print(response)
    answer = response.choices[0].message.content.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = askOpenAI(message)
        
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html',)


