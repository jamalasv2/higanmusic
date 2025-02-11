from HiganMusic.core.bot import Higanbana
from HiganMusic.core.dir import dirr
from HiganMusic.core.git import git
from HiganMusic.core.userbot import Userbot
from HiganMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Higanbana()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
