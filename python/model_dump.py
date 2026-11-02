from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str

user = User(id=1, name="Priya")

# 1. Python Dictionary mein convert karna
python_dict = user.model_dump()
print(python_dict, type(python_dict)) 
# Output: {'id': 1, 'name': 'Priya'} <class 'dict'>

# 2. JSON String mein convert karna
json_string = user.model_dump_json()
print(json_string, type(json_string)) 
# Output: {"id":1,"name":"Priya"} <class 'str'>