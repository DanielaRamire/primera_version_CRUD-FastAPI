from pydantic import BaseModel
from typing import Optional

class ActorShema(BaseModel):
    act_id: Optional[str]
    act_fname: str
    act_Iname: str
    act_gender: str
