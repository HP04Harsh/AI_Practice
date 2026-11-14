from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class InsufficientFundsException(Exception):
    def __init__(self, balance: float, requested: float):
        self.balance = balance
        self.requested = requested

@app.exception_handler(InsufficientFundsException)
async def insufficient_funds_handler(request: Request, exc: InsufficientFundsException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Transaction Failed",
            "message": f"Aapka balance ({exc.balance}) kam hai. Aap {exc.requested} nikalna chahte hain."
        }
    )

@app.get("/withdraw/{amount}")
def withdraw_money(amount: float):
    current_balance = 500.0
    if amount > current_balance:
        raise InsufficientFundsException(balance=current_balance, requested=amount)
    return {"message": "Success! Paise nikal liye gaye hain."}