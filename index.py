from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from pymongo import MongoClient
# from fastapi.templating import Jinja2Templates

# templates = Jinja2Templates(directory="templates")


from routes.notes import note

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(note)


# client = MongoClient('mongodb+srv://armemon:armemon248@cluster0.2srucfq.mongodb.net')


# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )


# @app.get("/")
# def read_root():
#     all_notes = client.FastAPi.Notes.find()
#     newNotes= []
#     for note in all_notes:
#         newNotes.append({
#             "id": note["_id"],
#            "title": note["title"],
#            "desc": note['desc']
#         })
#     print(all_notes)
#     print(newNotes)
#     return templates.TemplateResponse("index.html", {"request": request, "notes": newNotes})


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = 'itmes'):
#     return {"item_id": item_id, "q": q}


# @app.get("/items2/{item_id}")
# def read_item2(item_id: int, q: str | None = 'items2'):
#     return {"item_id": item_id, "q": q}