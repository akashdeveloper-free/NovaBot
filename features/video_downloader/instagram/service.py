class InstagramService:
    """Future platform-specific backend. UI does not depend on implementation."""
    async def inspect(self,url): return {'title':'Mock Instagram','url':url}
