
from typing import Optional,List
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    class Config:  # serialize our sql obj to json
        orm_mode = True


# class Item(BaseModel):
#     Student_F_Name: str
#     Student_L_name: str
#     Student_Id:int
#     GPA:float
#     class Config:
#         orm_mode=True

class User(BaseModel):
    id:int
    name:str
    email: str
    password: str
    class Config:
        orm_mode=True

class ShowUser(BaseModel):
    name: str
    email: str
    items: List[Item] = []

    class Config: # serialize our sql obj to json
        orm_mode = True

class ShowItem(BaseModel):
        id: int
        name: str
        description: Optional[str] = None # required
        price: float # int
        tax: Optional[float] = None
        owner: User
class Config: # serialize our sql obj to json
    orm_mode = True
# هدف منه هو ان هنا ابي استخدم المودل حق الايتم شو اليوزر ايتمز الايتم اللي متصل بهذا اليوز برجعها من الايتم ارجعها ك ليست 
#/ class ShowUser(BaseModel):
#     name: str
#     email: str
#     items: List[Item] = []
#     class Config: # serialize our sql obj to json
#         orm_mode = True

