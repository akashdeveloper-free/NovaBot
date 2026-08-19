# Architecture / UI Audit

Implemented: Single Master Message, persistent message ID, Back/Home stack, InlineKeyboard-only UI, modular features, isolated platform service placeholders, mock processing/result/error-capable structure.

Allowed exception: first /start creates the Master Message. User-authored URL/amount messages naturally exist; the bot does not answer them with navigation messages.

Not implemented: real APIs, yt-dlp, Stars payment processing, production file processing, external security scanning.

Developer rule: feature code must use NavigationEngine and must not bypass it to create menu messages.
