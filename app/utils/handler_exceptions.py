from fastapi import HTTPException


def raise_http_exception(func):
    async def wrapper(*args, **kwargs):
        result = await func(*args, **kwargs)
        if result.get("error"):
            raise HTTPException(status_code=result["status_code"], detail=result["error"])
        return result['response']
    return wrapper
