from pydantic import BaseModel, Field
from typing import List

class Node(BaseModel):
    comment_id: int
    comment: List['Node'] = Field(default_factory=list)

Node.model_rebuild()

node = Node(
    comment_id=1,
    comment=[
        Node(comment_id=2, comment=[]),
        Node(comment_id=3, comment=[
            Node(comment_id=4, comment=[])
        ])
    ]
)
print(node.comment_id)  
print(node.comment)     
