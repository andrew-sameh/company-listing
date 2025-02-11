from fastapi import APIRouter, HTTPException, Query, Depends, Request
from fastapi.responses import JSONResponse
from schema.company import Company

router = APIRouter()


@router.get("/ticker/{ticker}", response_model=Company, status_code=200)
async def get_companies(request: Request, ticker: str):
    """
    Retrieve a list of companies with optional filtering by cik, ticker, or exchange.
    """
    state = request.app.state
    for com in state.data:
        if com[2] == ticker:
            state.score[com[2]] += 1
            return Company(cik=com[0], name=com[1], ticker=com[2], exchange=com[3])
    raise HTTPException(status_code=404, detail="Company not found")


@router.get("/activity")
async def get_activity(request: Request):
    """
    Retrieve a list of companies with optional filtering by cik, ticker, or exchange.
    """
    state = request.app.state
    return JSONResponse(
        content=state.score,
        status_code=200
    )
