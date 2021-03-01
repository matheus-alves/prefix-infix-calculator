"""
This module contains the api logic
"""

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from calculator.domain.calculator import evaluate_expression

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
def form_get(request: Request):
    """
    Handles the get request
    :param request: the request parameters
    :return: the basic ui
    """
    result = ""
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post("/")
def form_post(request: Request, expression: str = Form(...), notation: str = Form(...)):
    """
    Handles the post request
    :param request: the request parameters
    :param expression: the expression provided by the user in the text box
    :param notation: the notation in which the expression is written in i.e. (prefix, infix)
    :return: the updated form with the result of the expression
    """
    result = evaluate_expression(expression, notation)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})
