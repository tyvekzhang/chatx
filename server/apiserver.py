"""The main entrance of the program"""

import os
import sys
from pathlib import Path

import uvicorn
from fastapi_offline import FastAPIOffline
from starlette.middleware.cors import CORSMiddleware

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = str(Path(current_dir).parent)
sys.path.insert(0, project_dir)

from config.config import configs  # noqa
from server.controller.controller import router  # noqa

# Offline swagger docs
app = FastAPIOffline(
    title=configs.app_name,
    version=configs.version,
    openapi_url=f"{configs.api_version}/openapi.json",
    description=configs.app_desc,
    default_response_model_exclude_unset=True,
)

# Cors processing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add project routing
app.include_router(router, prefix=configs.api_version)

if __name__ == "__main__":
    uvicorn.run(
        app="server.apiserver:app",
        host=configs.host,
        port=configs.port,
        workers=configs.workers,
    )
