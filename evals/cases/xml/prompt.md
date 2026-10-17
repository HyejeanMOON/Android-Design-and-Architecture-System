# Task

Review only the XML screen slice in `input/`; do not edit. This app currently has only one instance of the screen, and RefreshHooks is an app-level refresh notification entry point. Check spelling and references after View destruction; explain trigger and impact without expanding into an architecture migration. The field spelling in ApiContract is a published external contract and must not be renamed directly.

The target Android project generates binding and R classes from its resources. These files are evaluation source slices with no local Gradle project. Do not claim device or full-app execution, or invent other architecture defects because the whole project was not supplied.
