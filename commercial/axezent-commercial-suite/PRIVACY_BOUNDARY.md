# Licensing Telemetry Privacy Boundary

This document describes the intended telemetry boundary for AXEZENT entitlement checks. The customer-facing privacy notice is the [AXEZENT Privacy Policy](./PRIVACY_POLICY.md).

## Intended entitlement telemetry

The entitlement client is designed to transmit only:

- product ID;
- license key or account token;
- installation ID;
- application version; and
- request timestamp.

A production service may also process minimal security information reasonably necessary to authenticate the request, prevent abuse, investigate failures, and record entitlement status.

## Excluded research content

The entitlement client is not designed to transmit:

- customer proofs;
- source code;
- research files;
- prompts;
- unpublished mathematics; or
- other user research content

as licensing or payment telemetry.

If a customer intentionally submits research content to a separate paid analysis or support service, that processing is governed by the stated service scope and the Privacy Policy rather than this licensing-telemetry list.

## Deployment requirements

Before a production entitlement service is used for general paid access, the deployment should have:

- documented retention and deletion practices;
- access controls and secret management;
- HTTPS and appropriate transport security;
- reasonable logging and monitoring;
- a process for privacy and security requests; and
- contracts or terms appropriate to third-party processors used by the service.
