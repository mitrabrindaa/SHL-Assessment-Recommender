from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

class Query(BaseModel):
    text: str
    max_duration: int = 60

app = FastAPI()
df = pd.read_csv("shl_products.csv")

@app.post("/recommend")
async def recommend(query: Query):
    results = df[
        df["name"].str.contains(query.text, case=False) &
        (df["duration"] <= query.max_duration)
    ]
    return results.to_dict("records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)