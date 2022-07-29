from fastapi import FastAPI, Request, Form, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import PlainTextResponse, RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates/")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="shorten_link_db"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers (shortlink VARCHAR(255), longlink VARCHAR(255))")
#sql = "INSERT INTO customers (shortlink, longlink) VALUES (%s, %s)"
#val = ("fb", "https://www.facebook.com/")
#mycursor.execute(sql, val)

#mydb.commit()


@app.get("/")
async def root(request: Request):
    #return templates.TemplateResponse('thehtml.html', context={'request': request, 'result': "pikachu"})
    response = RedirectResponse(url="/redirect")
    return response

@app.get("/redirect")
async def form_post(request: Request):
        result = "Type a short link and long link"
        return templates.TemplateResponse('thehtml.html', context={'request': request, 'result': result})
@app.post("/redirect")
async def form_post(request: Request, shortlink: str = Form(...), longlink: str = Form(...)):
        print("run from post")
        sql = "INSERT INTO customers (shortlink, longlink) VALUES (%s, %s)"
        val = (shortlink, longlink)
        mycursor.execute(sql, val)
        mydb.commit()
        result = "Linked successfully"
        return templates.TemplateResponse('thehtml.html', context={'request': request, 'result': result})

@app.get("/redirect/{shortlink}")
async def redirect(shortlink):
    #dict = {"me": 'https://www.facebook.com/'}
    sql = "SELECT * FROM customers WHERE shortlink = %s"
    mycursor.execute(sql,(shortlink, ))
    myresult = mycursor.fetchone()
    response = RedirectResponse(url=myresult[1])
    return response