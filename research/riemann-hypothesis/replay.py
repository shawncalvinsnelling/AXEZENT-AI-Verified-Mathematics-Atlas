"""Run actual finite-domain verification; never infer RH from a PASS."""
from pathlib import Path
import json
import subprocess
import sys
from check_integrity import check

ROOT = Path(__file__).resolve().parent

def run():
    check()
    out = ROOT / "_replay"
    out.mkdir(exist_ok=True)
    def execute(arguments, log):
        result = subprocess.run([sys.executable, *arguments], cwd=ROOT,
                                text=True, capture_output=True, timeout=180)
        text = result.stdout + result.stderr
        (out / log).write_text(text, encoding="utf-8")
        print(text, end="")
        if result.returncode:
            raise RuntimeError(f"Subprocess failed: {arguments}; exit {result.returncode}")
    execute(["-m", "unittest", "discover", "-s", ".", "-p", "test_certificate.py", "-v"], "tests.txt")
    execute(["certify_finite_envelope.py", "--output", str(out / "normal.json")], "normal.txt")
    execute(["-O", "certify_finite_envelope.py", "--output", str(out / "optimized.json")], "optimized.txt")
    expected = json.loads((ROOT / "receipts/finite_envelope_receipt.json").read_text(encoding="utf-8"))
    if expected.get("scope") != "FINITE_DOMAIN_ALL_REAL_X_NOT_RH" or expected.get("formal_kernel_verified") is not False:
        raise RuntimeError("Incorrect expected scope")
    for name in ("normal.json", "optimized.json"):
        actual = json.loads((out / name).read_text(encoding="utf-8"))
        if actual != expected:
            raise RuntimeError(f"Frozen receipt mismatch: {name}")
    summary = {"status": "PASS_RH_FINITE_REPLAY_NOT_RH_PROOF",
               "x_min": 256, "x_max": 1048576, "unit_tests": 17,
               "reproductions": 2, "rh_proved": False,
               "formal_kernel_verified": False,
               "ordered_exact_cell_sha256": expected["ordered_exact_cell_sha256"]}
    (out / "SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(summary["status"])
    return summary

if __name__ == "__main__":
    run()
