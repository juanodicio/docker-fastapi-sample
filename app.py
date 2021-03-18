import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from typing import List

app = FastAPI()


class SwitchType(str, Enum):
    blue = "blue"
    red = "red"
    brown = "brown"


class Keyboard(BaseModel):
    name: str
    brand: str
    switch_type: SwitchType


Keyboards = [
    Keyboard(name="K6", brand="Keychron", switch_type=SwitchType.blue),
    Keyboard(name="Origins Core Alloy", brand="Hyperx", switch_type=SwitchType.red),
    Keyboard(name="G915 TKL", brand="Logitech", switch_type=SwitchType.brown),
    Keyboard(name="Huntsman Mini", brand="Razer", switch_type=SwitchType.red),
    Keyboard(name="Ornata", brand="Razer", switch_type=SwitchType.brown)
]


@app.get("/keyboards", response_model=List[Keyboard])
async def keyboards_all():
    return Keyboards

uvicorn.run(app, host="0.0.0.0", port=8000)
