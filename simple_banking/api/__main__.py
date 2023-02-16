"""RestAPI entrypoint."""
import uvicorn

uvicorn.run(app="simple_banking.api.app:app", reload=True)
