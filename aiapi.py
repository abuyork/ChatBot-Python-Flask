import openai
import config
openai.api_key = config.DevelopmentConfig.OPENAI_KEY


def get_Chat_response(msg):
    messages = []
    messages.append({"role": "system", "content": "You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = msg
    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    
    try:
        answer = response['choices'][0]['message']['content'].replace('\n','<br>')
    except:
        answer = 'Oops ! Try diferrent question.'
    return answer
    