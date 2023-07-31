from fastapi import FastAPI
from pydantic import BaseModel
import get_simple_data_filter
import uvicorn


app = FastAPI()


class Value(BaseModel):
    input: dict


@app.post('/')
def Value_gen(inp: Value):
    global output

    b = get_simple_data_filter.data_filter(req_body=inp.input)
    return b

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
