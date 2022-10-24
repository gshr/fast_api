from fastapi import FastAPI

app = FastAPI(title="My App")
from pydantic import    BaseModel
data =[
    {    "id" :2,
    "name": "ABC",
    "description": "abc@demo.com"
   
}
,{    "id" :3,
    "name": "DEF",
    "description": "abc@demo.com"
   
}
,{    "id" :5,
    "name": "GHI",
    "description": "abc@demo.com"
   }]


class Item(BaseModel):
    id :int
    name :str
    description :str

@app.get("/save/{id}")
def hello(id : int):
    print(data)
    for  i in data:
        if i['id'] == id:
            return i

    return {"message": "Data not found"}


@app.post("/save")
def add(item : Item):
    print(item)

    d = {
        "id": item.id,
        "name": item.name,
        "description":item.description
    }
    data.append(d)
    return {"message":  "Data saved successfully"}


@app.delete("/save/{id}")
def delete_data(id:int):
    if len(data) !=0:
        for i in data:
            if i['id'] == id:
                data.remove(i)

                return {"message":  "Data deleted"}

    return {"message":  "Data not found"}

        

