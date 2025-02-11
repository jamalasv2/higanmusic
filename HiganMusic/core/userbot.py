from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="HiganAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="HiganAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"memulai assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("higanbanasupport")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "assistant dimulai")
            except:
                LOGGER(__name__).error(
                    "akun assistant 1 gagal mengakses grup log. pastikan kamu telah menambahkan akun assisten dan mempromosikannya sebagai admin!"
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"asisten dimulai sebagai {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("higanbanasupport")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "asisten dimulai")
            except:
                LOGGER(__name__).error(
                    "akun asisten 2 gagal mengakses grup log. pastikan kamu sudah menambahkan akun asisten dan mempromosikannya sebagai admin!"
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"asisten 2 dimulai sebagai {self.two.name}")


    async def stop(self):
        LOGGER(__name__).info(f"menghentikan asisten...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
        except:
            pass
