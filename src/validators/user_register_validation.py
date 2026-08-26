from pydantic import BaseModel, Field

class UserInput(BaseModel):
    nome: str = Field(..., min_length=3)
    idade: int = Field(..., gt=0)