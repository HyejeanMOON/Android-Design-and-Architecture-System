# Material 3 UI/UX

Identify the page task, information hierarchy, primary action, Back behavior, and relevant exceptional paths before choosing components. Stay within the requested feature. Label fake preview data; do not add fictional business entry points.

## Components and theme

Prefer standard M3 components and the existing design system in new or explicitly migrated areas. XML uses compatible Material Components; Compose uses M3. Follow [legacy interoperability](legacy-hybrid.md) when old themes coexist; do not replace the global theme. Use semantic colors and on-colors, typography, shape, and spacing from existing resources or tokens. Not every clickable item needs to be a Card.

Check light and dark themes supported by the product. Enable dynamic color when appropriate for platform and brand, with a static fallback. Brand customization is allowed. Do not introduce experimental APIs or an Expressive redesign by default.

Represent initial loading, refresh, empty, error, validation, permission, submit, and completion states where relevant. States can coexist; failed refresh need not erase content. Do not force every state into every screen.

## Accessibility and adaptation

- Interactive targets generally need at least 48dp × 48dp; separate visual icon size from touch area without overlapping targets. Aim for 4.5:1 contrast for body text and 3:1 for large text; check real foreground, background, and alpha rather than trusting token names.
- Name meaningful icons and avoid reading decorative icons twice. Add semantics, roles, state, and actions to custom controls; check reading order and focus. A contentDescription alone does not finish accessibility work.
- Support font scaling, long copy, resources, quantity/format conventions, and RTL. Avoid fixed heights that clip text or concatenated translated sentences. Errors should offer actionable recovery, not just a code.
- Choose layout and suitable navigation/columns from available window space while keeping existing destinations. Check relevant rotation, multi-window, fold, and reading width; do not classify only by device model.
- Handle system bar, cutout, and IME insets at the correct boundary without duplicate padding. Check Back and edge-to-edge behavior against the target system; do not lower targetSdk to evade adaptation. Motion should convey meaning and respect system settings.

Check affected light/dark modes, large text, relevant windows and exceptional states, plus key TalkBack/keyboard flows. If rendering is unavailable, state that it was not verified; do not claim complete guideline compliance.

Sources: [Material 3](https://m3.material.io/foundations), [Compose](https://developer.android.com/develop/ui/compose/designsystems/material3), [Views](https://developer.android.com/develop/ui/views/theming/look-and-feel), [Accessibility](https://developer.android.com/develop/ui/compose/accessibility/api-defaults), [Adaptive UI](https://developer.android.com/develop/ui/compose/layouts/adaptive).
