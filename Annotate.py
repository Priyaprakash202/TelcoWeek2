from pydantic import BaseModel
from typing import Annotated
from annotated_types import Gt


class MyClass(BaseModel):
    age: Annotated[int, Gt(18)]

# Valid input
obj1 = MyClass(age=20)
print(obj1)