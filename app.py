from fastapi import FastAPI
from pydantic import BaseModel
from hybrid_logic import hybrid_decision
import uuid
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    text: str
    user_id: str | None = None


@app.post("/predict")
def predict(query: Query):

    # Agar user_id nahi diya → auto generate
    if not query.user_id:
        query.user_id = str(uuid.uuid4())

    predicted_category = "Unknown"   # Abhi ML nahi, rule based
    result = hybrid_decision(predicted_category, query.text, query.user_id)

    # User id bhi response me bhejo
    result["user_id"] = query.user_id
    return result
