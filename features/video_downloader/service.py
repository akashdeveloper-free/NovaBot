class DownloaderService:
    async def inspect_url(self,platform,url): return {'platform':platform,'title':f'Demo {platform.title()} Media','url':url}
