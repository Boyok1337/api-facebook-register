from fastapi import FastAPI
from crud import register_account

app = FastAPI()


@app.post("/register-accounts/{count}")
def register_accounts(count: int):
    for _ in range(count):
        register_account()
    return {"message": f"{count} accounts registration initiated."}
