from fastapi import APIRouter

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.note import Note
from config.config import conn

note = APIRouter()
templates = Jinja2Templates(directory="templates")

db = conn.get_database("FastAPi")
notes_collection = db.get_collection("Notes")

@note.get("/", response_class=HTMLResponse)
async def read_notes(request: Request):
    all_notes = notes_collection.find()
    newNotes= []
    for note in all_notes:
        newNotes.append({
            "id": note["_id"],
            "title": note["title"],
            "desc": note['desc']
        })
    print(all_notes)
    print(newNotes)
    return templates.TemplateResponse("index.html", {"request": request, "notes": newNotes})

@note.post("/notes")
async def create_note(request: Request):
    note = await request.form()
    note_dict = dict(note)
    print(note_dict)
    result = conn.FastAPi.Notes.insert_one(note_dict)
    inserted_note = conn.FastAPi.Notes.find_one({"_id": result.inserted_id})
    print(result)
    print(inserted_note)
    return {"status": "done"}
