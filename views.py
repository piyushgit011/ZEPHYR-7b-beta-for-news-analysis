from django.shortcuts import render
from langchain_community.document_loaders import NewsURLLoader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from langdetect import detect
from langchain_community.document_loaders import NewsURLLoader
import requests
import json
import nltk
nltk.download('punkt')
# Create your views here.

url = "https://8qu3wuuyqyzgqk-5000.proxy.runpod.net/v1/completions"


@csrf_exempt
def get_news_summary(request):
    if request.method == 'POST':
        try:
            news_url = request.POST.get('url')

            print(f"This is a URL {news_url}")
            loader = NewsURLLoader(urls=[news_url], nlp=True)
            data = loader.load()
            print(f"This is a Data {data}")

            if data and data[0].page_content:
                content = data[0].page_content

                prompt = f"{content}"
                
                data = {
                    "prompt": prompt,
                    "max_tokens": 400,
                    "temperature": 0.5,
                    "top_p": 0.9,
                    "guidance_scale" : 1,
                    "repetition_penalty" : 1.15,
                    "top_k": 20
                }

                print(data)

                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.post(url, headers=headers, json=data, verify=False)

                # Check if response is successful
                if response.status_code == 200:
                    try:
                        # Extracting the specific part of the JSON response
                        assistant_message = response.json()['choices'][0]['text']
                        print(assistant_message)
                        return JsonResponse({'response': assistant_message})
                    
                    except KeyError as e:
                        print(f"Key error: {e}")
                    except IndexError as e:
                        print(f"Index error: {e}")
                else:
                    print(f"Failed to get a successful response. Status code: {response.status_code}")

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})


