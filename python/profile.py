from pydantic import BaseModel
from typing import List, Optional, Dict

class Profile(BaseModel):
    name: str
    age: int
    skills: List[str]
    experience: Optional[Dict[str, int]] = None

profile = Profile(name="John Doe", age=30, skills=["Python", "JavaScript"],experience={"Python": 5, "JavaScript": 3})
print(profile)    