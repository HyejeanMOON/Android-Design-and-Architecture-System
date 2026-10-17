# Security and privacy

Check data, capabilities, and attack surfaces actually touched by the task. A routine layout edit does not trigger a full-project security refactor. For Play declarations, see [Google Play](google-play-release.md); a security check does not itself start a release process.

## Data and permissions

- Collect only data needed for a defined function. Identify purpose, recipients, storage, retention, and deletion. Include analytics, ads, crash tooling, and third-party SDK access.
- Request permissions when the relevant user action needs them, with sensible denial, revocation, and permanent-denial paths. Prefer a system picker or grant mechanism when it satisfies the task rather than broad storage, contacts, or location access.
- Check system permission behavior and applicable Play policy before claiming sensitive capability eligibility; declaring a permission is insufficient.
- Review private storage, backups/exports, and logs together. Private directories do not mean all data is encrypted; DataStore is not an encrypted credential vault.

## Credentials and network

- Do not place confidential server secrets in source, resources, BuildConfig, or app packages. Restrict client-identifying API keys according to service rules; obfuscation is not secrecy.
- Choose platform-supported credential storage for the threat model and lifetime. When protecting keys, use platform facilities such as Android Keystore and handle invalidation/recreation. Do not invent cryptography or adopt deprecated libraries as permanent templates.
- Preserve HTTPS and certificate validation; never trust all certificates or hosts. Restrict debug certificates and cleartext exceptions to debug. Pin certificates only with a defined threat model and rotation plan.
- Redact logs, crash context, and network interceptors. Do not record passwords, tokens, full personal data, or leak authenticated URLs to analytics.

## Platform entry points and identity

- Minimize visibility of exported components, Intents, PendingIntents, URIs, ContentProviders, and FileProviders. Validate callers, inputs, and grant scope.
- Deep-link/App Link parameters are not trusted identity or authorization. Server-validated sessions, payments, and resource access cannot rely solely on hidden UI or a client Boolean.
- Enable WebView capabilities only when needed; validate navigation destinations and JS bridge exposure. Do not enable file access, arbitrary domains, or sensitive bridges to untrusted pages by default.
- Logout, account switch, and deletion must address tokens, in-flight requests, and sensitive local data. Account deletion is more than logout, clearing cache, or disabling an account.

## Verification and delivery

Check relevant release configuration and merged Manifest, permission denial/revocation, unauthorized inputs, wrong-account behavior, and logs. Report real fixes and limits; using a library alone does not prove security. Policy declarations must follow actual data flows and server facts; never invent privacy promises.

Sources: [Android security best practices](https://developer.android.com/privacy-and-security/security-best-practices), [Play Data safety](https://support.google.com/googleplay/android-developer/answer/10787469), [Account deletion policy](https://support.google.com/googleplay/android-developer/answer/13327111). This is not a complete audit for every business scenario.
