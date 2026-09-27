# Digital Safety and Threat Modeling Knowledge

## Purpose and boundary
This module operationalizes the **defensive** half of `knowledge/ETHICS_AND_SAFETY.md`'s journalist threat model, and the **verification** half of checking a suspicious message or attachment a reporter has received.

It is strictly a **defender's** and **verifier's** toolkit. It does not, and will not, provide offensive techniques (exploitation, intrusion, credential theft, malware construction, social-engineering scripts to use *against* someone). Where a technique could serve either purpose, this file gives only the analysis/recognition half, never the construction half. This mirrors the boundary already set in `SKILL.md` rule 12 and `knowledge/OSINT.md`.

## Recognizing phishing and social-engineering attempts against the newsroom
Journalists and their sources are frequent phishing targets (credential-harvesting, account-takeover, malware-laced "leaked documents"). Recognition checklist:
- sender domain vs. claimed organization (look-alike domains, unusual subdomains);
- urgency or fear-based pressure to click/open immediately;
- a request to enter credentials on a page reached via an email/DM link rather than typed manually;
- an unsolicited attachment claiming to be leaked material — verify through a separate, trusted channel before opening;
- inconsistent sending infrastructure revealed in email headers (mismatched `From`/`Return-Path`/`Received` chains) — useful when *authenticating an inbound tip*, not for spoofing outbound mail.

## Verifying an inbound leak or tip's digital packaging
Before treating a leaked file as evidence:
- preserve the original file and its metadata unmodified; work from a copy (same rule as `knowledge/OSINT.md`'s digital evidence section);
- record how it was received, from whom, and when;
- check document metadata (author, editing history, software version) for internal consistency with the claimed origin;
- treat an executable, macro-enabled, or unusually-formatted attachment as a security risk to open only in an isolated/sandboxed environment reviewed by IT/security staff — never open it directly on a device that also holds source-identifying information.

## Account and communications hygiene (protective, not offensive)
Baseline practices worth confirming with a source or colleague, framed as protective guidance only:
- separate identities/devices for sensitive reporting versus daily use;
- hardware or app-based multi-factor authentication over SMS where possible;
- encrypted, disappearing-message channels for source contact, matched to the source's own risk tolerance and access;
- stripping identifying metadata (GPS EXIF, device IDs, author names in document properties) from files before they are shared or published, when that metadata is not itself the evidence;
- assuming that "already public" does not mean "safe to aggregate" — combining several individually-public data points can re-identify a source or victim (the same proportionality test as `knowledge/ETHICS_AND_SAFETY.md`).

## Digital forensics as a verification aid
Concepts borrowed from digital-forensics practice, used only for *authenticating evidence already lawfully in hand* (never for accessing a system the newsroom does not already have authorized access to):
- chain-of-custody logging (who touched a file, when, what changed);
- cryptographic hashing to prove a preserved copy has not been altered since capture;
- comparing file/document metadata against the claimed chronology as an internal-consistency check (same technique as `knowledge/VERIFICATION.md`'s document-verification section).

## What this module explicitly excludes
Consistent with `SKILL.md` rule 12 and the hard limits this skill operates under: no exploit code, no malware, no credential-phishing templates, no instructions for bypassing authentication, no offensive "red-team" playbooks, even if framed as being for a journalist's own testing. A newsroom that needs penetration testing of its own systems should engage a qualified, authorized security professional — this skill supports the *story*, not the intrusion.

## Source map
- S48 — Berkeley Protocol (digital evidence, legal framework, security).
- S20–S21 — journalist safety and press freedom context.
- Concepts of phishing recognition, digital forensics and threat-hunting are used here only in their defensive/verification form, adapted at a principle level from general cybersecurity-skill literature (see `CREDITS.md`); no offensive material from any source is reproduced or referenced.
