import httpx
from typing import List, Optional
from fastapi import HTTPException
from schema.company import Company
from core.config import settings



async def load_companies_data():
    try:
        async with httpx.AsyncClient() as client:
            agent_headers = {
                'User-Agent': 'Andrew Sameh (g.andrewsameh@gmail.com)'
            }
            response = await client.get(settings.PUBLIC_COMPANIES_API_URL,headers=agent_headers)
            json_data = response.json()
            return json_data['data']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading companies: {e}")