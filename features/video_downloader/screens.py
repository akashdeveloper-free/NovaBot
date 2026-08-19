from .keyboards import menu,platform,result
LABEL={'tiktok':'🎵 TikTok','youtube':'▶️ YouTube','facebook':'📘 Facebook','instagram':'📸 Instagram'}
def video_menu_screen(): return ('🎬 **Video Downloader**\n\nSelect a platform. Real APIs are intentionally not connected yet.',menu())
def platform_screen(platform_name): return (f"{LABEL[platform_name]} **Downloader**\n\nSend a public URL. This phase demonstrates only the Master Message flow.",platform(platform_name))
def processing_screen(platform_name='tiktok'): return (f"{LABEL.get(platform_name,platform_name)} **Processing**\n\n⏳ Preparing a mock result...",platform(platform_name))
def coming_soon_screen(platform_name='youtube'): return (f"🚧 {LABEL.get(platform_name,platform_name)} **Coming Soon**\n\nThe UI is ready. The real platform service will be connected later.", platform(platform_name))
def error_screen(): return ('⚠️ **Unable to process URL**\n\nThis UI phase uses mock services only.', menu())
def result_screen(platform_name='tiktok',title='Demo Media'): return (f"✅ {LABEL.get(platform_name,platform_name)} **Result**\n\n📌 **Title:** {title}\n👤 **Creator:** demo_creator\n⏱️ **Duration:** 00:45\n\nChoose a mock quality.",result(platform_name))
def register(navigation):
    navigation.register('VIDEO_MENU',video_menu_screen)
    for p in LABEL: navigation.register('VIDEO_'+p.upper(),lambda p=p: platform_screen(p))
    navigation.register('VIDEO_PROCESSING',processing_screen)
    navigation.register('VIDEO_RESULT',result_screen)
    navigation.register('VIDEO_ERROR',error_screen)
    navigation.register('VIDEO_COMING_SOON',coming_soon_screen)
