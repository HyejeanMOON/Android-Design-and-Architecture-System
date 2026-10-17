# Task

Review the Compose source slice in `input/`. Product behavior requires one refresh each time this Route enters composition, without refreshing on ordinary recomposition. The existing minimal display need not be redesigned. Report evidence-backed problems only. Do not replace UI, DI, or navigation frameworks, and do not call BasicText a defect merely because it is a low-level component. State limits if no UI test was run.

The assembly layer provides the refresh callback, which triggers a real request. Only its interface appears here to isolate the backend. Do not invent errors because the full Repository or network implementation is absent.
