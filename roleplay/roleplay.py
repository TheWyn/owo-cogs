import random
from random import randint

import aiohttp
import discord
from redbot.core import commands

wasted = [
    "https://cdn.weeb.sh/images/B1VnoJFDZ.gif",
    "https://cdn.weeb.sh/images/B1qosktwb.gif",
    "https://cdn.weeb.sh/images/r11as1tvZ.gif",
    "https://cdn.weeb.sh/images/B1qosktwb.gif",
    "https://cdn.weeb.sh/images/HyXTiyKw-.gif",
    "https://cdn.weeb.sh/images/BJO2j1Fv-.gif"
]


class Roleplay(commands.Cog):
    """Interact with people!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hugs a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("hug")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("kiss")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slaps a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("slap")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} slaps {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def nya(self, ctx, *, user: discord.Member):
        """Give you or someone else cat girls"""

        user = user or ctx.author

        nekos = await self.fetch_nekos_image("neko")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**Have some cute cat girls {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, user: discord.Member):
        """Pats a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("pat")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feeds a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("feed")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("tickle")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, *, user: discord.Member):
        """Pokes a user"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("poke")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("smug")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} is smug**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def baka(self, ctx, *, user: discord.Member):
        """Baka!"""

        author = ctx.message.author

        nekos = await self.fetch_nekos_life("baka")

        mn = len(nekos)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{author.mention} thinks you're an idiot {user.mention}**"
        embed.set_image(url=nekos[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def wasted(self, ctx, *, user: discord.Member):
        """Waste a user"""

        author = ctx.message.author

        # Build Embed
        embed = discord.Embed()
        embed.colour = discord.Colour(0x4fe0e0)
        embed.description = f"**{user.mention} got WASTED by {author.mention}**"
        embed.set_image(url=random.choice(wasted))
        await ctx.send(embed=embed)

    async def fetch_nekos_life(self, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nekos.dev/api/v3/images/sfw/gif/{rp_action}/?count=20") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError):
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]

    async def fetch_nekos_image(self, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nekos.dev/api/v3/images/sfw/img/{rp_action}/?count=20") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError):
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]
