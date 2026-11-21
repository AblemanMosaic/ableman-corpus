#!/usr/bin/env python3
"""Serve the repository locally without changing it."""

from __future__ import annotations

import argparse
import functools
import http.server
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(args.root.resolve()))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    print(f"Ableman corpus local preview: http://127.0.0.1:{args.port}/site/", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
