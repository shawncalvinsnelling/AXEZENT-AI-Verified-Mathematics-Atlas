# Preparation, execution and provenance

**Public review edition 0.1.0 · Shawn Calvin Snelling · 12 October 2026**

This module is prepared from `AXEZENT_RH_Certificate_Bridge_2026-10-12.zip` (archive SHA-256 `66fa9f7583fa9092d0807046cc6437e6c61856021aac957a178f0755d8249d28`). The original archive is retained unchanged in the conversation.

`certify_finite_envelope.py` and `test_certificate.py` are copied byte for byte from that archive. The frozen receipt is also unchanged. Their source hashes are recorded in this module's manifest.

The public mathematical note is an edited edition of the original `RH_Certificate_Bridge_Note.md`: it preserves Theorems A-C and the finite-domain computation, adds reviewer-oriented headings and explicit code pointers, and omits conversational material, the imagined fifty-person roster, and unrelated AHR/P-versus-NP discussion. No new all-scale bound or new mathematical result was inserted during publication preparation. The original note's SHA-256 is `e796a936916830a877b894d4c9ff10e60de3577d78d4cef0cc00f2232c337414`.

The source archive's 12 manifested files matched their hashes. Preparation replay on Linux/Python 3.13.5 ran the 17 tests successfully and regenerated the full finite receipt normally and with optimization. Both receipts matched the supplied receipt. This is an additional execution of the same implementation, not external specialist review or an independently authored verifier.

A new replay wrapper and file-integrity checker make reproduction easier. Module-local Git attributes require LF line endings so exact source hashes are stable across platforms. The CI workflow is configured for Ubuntu and Windows, Python 3.11 and 3.13. Workflow configuration is not evidence of a successful hosted run: consult the actual GitHub Actions run at the exact commit. No local Windows execution is claimed.

AI assistance: ChatGPT-assisted mathematical exposition, software preparation and internal checking. No historical-person panel participated. Standard background is cited in the note. No claim of historical priority, journal acceptance or prize eligibility is made.

Privacy: private conversation transcripts, email records, personal biographical/medical information, historical-agent rosters, and unrelated private project files are not part of this publication.

The existing repository license and root citation for other research are unchanged. This module has its own citation file. This publication does not install code on the author's laptop or submit anything to a journal or CMI.
