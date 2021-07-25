# -*- coding: utf-8 -*-

from app.api import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000,reload=True, debug=True)



