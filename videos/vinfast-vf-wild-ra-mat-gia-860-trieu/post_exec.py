#!/usr/bin/env python3
"""POST to the Apps Script exec endpoint and correctly resolve its 302
'echo' redirect (GET the Location, do NOT resend the POST body)."""
import json, sys, urllib.request, urllib.error

EXEC = "https://script.google.com/macros/s/AKfycbzDb2gLI8f2KBOMH1R6hgQdNkGoFa5BlEf5SUY8aOYQ5jF_bVK6G5bck8i7pVRopV0FlQ/exec"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def post_exec(payload, timeout=300):
    data = json.dumps(payload).encode("utf-8")
    opener = urllib.request.build_opener(NoRedirect)
    req = urllib.request.Request(EXEC, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try:
        resp = opener.open(req, timeout=timeout)
        # No redirect (rare) -- read directly.
        return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            location = e.headers.get("Location")
            if not location:
                raise RuntimeError(f"Redirect {e.code} with no Location header")
            with urllib.request.urlopen(location, timeout=timeout) as resp2:
                return json.loads(resp2.read().decode())
        raise


if __name__ == "__main__":
    payload = json.loads(sys.argv[1])
    result = post_exec(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
