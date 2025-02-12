from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
OPERATOR = env.int("OPERATOR")
IP = env.str("ip")  # Xosting ip manzili
YUAN_BOT = env.str("YUAN_BOT")