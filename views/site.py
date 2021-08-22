import http

from fastapi import APIRouter, Form
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND

router = APIRouter()
templates = Jinja2Templates('templates')



@router.get('/')
def index(request: Request):
    num = 0
    messages = {num: {
        'text': 'Тест',
        'num': num
    }
    }
    return templates.TemplateResponse('index.html', {'request': request, 'messages': messages})


# @router.post('/')
# async def create_message(message: str = Form(...)):
#     global num
#     messages[num] = {'text': '', 'num': num}
#     messages[num]['text'] = message
#     messages[num]['num'] += 1
#     num += 1
#     print(messages)
#     return  RedirectResponse('/', status_code=HTTP_302_FOUND)
