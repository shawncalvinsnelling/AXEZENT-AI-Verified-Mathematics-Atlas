"""Reference AXEZENT entitlement HTTP service.

For production, place behind HTTPS and a hardened reverse proxy/serverless
runtime. The signing secret is supplied only through AXZ_LICENSE_SECRET.
"""

from __future__ import annotations

import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from axezent_ai_verified_math.entitlements import verify_license


class Handler(BaseHTTPRequestHandler):
    server_version = "AXEZENTEntitlement/1.0"

    def _json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(body)))
        self.send_header("cache-control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self) -> None:  # noqa: N802
        if self.path != "/v1/entitlements/check":
            self._json(404, {"allowed": False, "reason": "not_found"})
            return

        try:
            length = int(self.headers.get("content-length", "0"))
            if length <= 0 or length > 16384:
                raise ValueError
            request = json.loads(self.rfile.read(length).decode("utf-8"))
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            self._json(400, {"allowed": False, "reason": "invalid_request"})
            return

        auth = self.headers.get("authorization", "")
        if not auth.startswith("Bearer "):
            self._json(401, {"allowed": False, "reason": "missing_entitlement"})
            return

        secret = os.environ.get("AXZ_LICENSE_SECRET")
        if not secret:
            self._json(503, {"allowed": False, "reason": "server_not_configured"})
            return

        product_id = request.get("productId")
        installation_id = request.get("installationId")
        if not isinstance(product_id, str) or not product_id:
            self._json(400, {"allowed": False, "reason": "missing_product"})
            return

        result = verify_license(
            secret,
            auth[7:].strip(),
            product_id=product_id,
            installation_id=installation_id if isinstance(installation_id, str) else None,
            now=int(time.time()),
        )
        self._json(200, result)

    def log_message(self, format: str, *args) -> None:
        # Avoid accidentally logging bearer tokens; default request-line logging is sufficient.
        super().log_message(format, *args)


def main() -> None:
    host = os.environ.get("AXZ_LICENSE_HOST", "127.0.0.1")
    port = int(os.environ.get("AXZ_LICENSE_PORT", "8787"))
    if not os.environ.get("AXZ_LICENSE_SECRET"):
        raise SystemExit("AXZ_LICENSE_SECRET is required")
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"AXEZENT entitlement service listening on {host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
