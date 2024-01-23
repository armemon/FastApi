def noteConvertor(item) -> dict:
    return {
        "id": str(item._id),
        "title": item['title'],
        "desc": item['desc']
    }

def notesEntity(items) -> list:
    return [noteConvertor(item)  for item in items]
