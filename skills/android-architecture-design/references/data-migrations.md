# Data migrations and compatibility

Use this when changing database schema, configuration format, persistent models, cache keys, serialization, or server fields. Distinguish new installs, in-place upgrades, and upgrades from older supported versions. An empty database startup test is insufficient.

## Room

- Use the target project's actual Room version for schema versions and automatic/manual migrations. Export and retain historical schemas; distinguish flavors/variants when their databases differ.
- Check old data semantics for renames, defaults, NOT NULL constraints, indexes, foreign keys, and table splits. Schema validation alone does not prove records and relationships are correct.
- Cover every still-supported old-to-new database path, including direct upgrades across multiple versions. Use migration test tools for that Room version and realistic schema samples; do not copy APIs from a different major version.
- Do not delete a database, change its filename, or enable fallbackToDestructiveMigration just to make startup succeed. Consider destructive behavior only when the data is explicitly disposable and the user authorizes it, within a defined scope.
- For large migrations, check transaction behavior, duration, space, and failure recovery. Prioritize retaining user data; do not run a long migration on the main thread.

## Settings, files, and APIs

- SharedPreferences-to-DataStore and file-format migrations need a trigger, success marker, repeat-safe behavior, old-data retention/cleanup, and failure handling. Do not delete the source before confirming success.
- Handle renamed serialization fields, missing/null values, new enum values, and type changes according to the real contract. Meaningless defaults must not hide corrupt orders, amounts, or account information.
- Cache may expire by version, but user edits, drafts, and unsynced writes are not disposable cache. Consider identity binding, file paths, and encryption keys after backup restore.
- During rollout, old and new clients may access the backend concurrently. Confirm compatibility windows and callers before changing APIs, deep links, or persistent identifiers; updating a local DTO alone is insufficient.

## Upgrade, downgrade, and recovery

Record supported source versions, transformations, possible loss, and failure handling. Do not assume database downgrade works. Stopping rollout or reverting a backend does not imply an old APK can read a newer schema; a forward fix or prevalidated compatibility plan is usually needed.

Verify relevant old-version samples, missing/abnormal data, repeat runs, and core reads/writes after upgrade. Test interruption and restart when recovery is required. Redact test data; do not commit a user's production database.

Source: [Room migration guide](https://developer.android.com/training/data-storage/room/migrating-db-versions). API and settings migration strategies depend on the project's contracts and are plugin guidance.
