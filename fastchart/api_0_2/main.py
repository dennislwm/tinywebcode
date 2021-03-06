# generated by fastapi-codegen:
#   filename:  fxgit-FastChart-0.2.0-resolved.yaml
#   timestamp: 2021-01-20T03:10:35+00:00

from __future__ import annotations

from typing import Optional

from fastapi import FastAPI

app = FastAPI(
    title='FastChart API',
    description='stock chart as a service',
    contact={'name': 'dennislwm', 'url': 'https://github.com/dennislwm'},
    version='0.2.0',
)


@app.get('/{symbol}', response_model=None)
def get_symbol(
    symbol: str, main: Optional[str] = None, sub: Optional[str] = None
) -> None:
    """
    Fastchart is an alternative to TradingView
    """
    pass
