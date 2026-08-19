# NovaBot Master Architecture

MAIN_MENU is the root. Every branch returns with `nav:back` and can jump to root with `nav:home`.

```text
MAIN_MENU
├── VIDEO_DOWNLOADER
│   ├── TIKTOK
│   │   ├── Send URL
│   │   ├── Processing
│   │   └── Result
│   │       ├── HD (mock)
│   │       └── Normal (mock)
│   ├── YOUTUBE
│   ├── FACEBOOK
│   └── INSTAGRAM
├── DONATE_STARS
├── FILE_TOOLS
├── SECURITY_TOOLS
├── SETTINGS
└── HELP
```

## Layering

`router -> handler -> NavigationEngine -> screen + keyboard -> MasterMessageManager -> Telegram`

Backend later: `handler -> service -> API/engine -> result -> screen -> Master Message edit`.

Feature modules must never create menu messages themselves.
