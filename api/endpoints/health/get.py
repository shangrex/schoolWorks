from fastapi.responses import PlainTextResponse

DOC = {200: {"text/plain": {"example": "OK"}}}


def get():
    return PlainTextResponse("OK", 200)
