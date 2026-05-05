from pathlib import Path
import shutil
import re

ROOT = Path('/home/ubuntu/culinaria_live_app')
SOURCE_ICON = Path('/home/ubuntu/webdev-static-assets/culinaria-live-icon.png')
ASSETS = ROOT / 'assets' / 'images'
LOGO_URL = 'https://d2xsxph8kpxj0f.cloudfront.net/310519663628148319/RigkWFohVDZU8L8iY8h9Gq/culinaria-live-icon-6aLP4GdxVFYobpTebKRks4.png'

ASSETS.mkdir(parents=True, exist_ok=True)
for name in ['icon.png', 'splash-icon.png', 'favicon.png', 'android-icon-foreground.png']:
    shutil.copyfile(SOURCE_ICON, ASSETS / name)

config_path = ROOT / 'app.config.ts'
content = config_path.read_text(encoding='utf-8')
content = re.sub(r'appName: "[^"]*"', 'appName: "Culinária Live"', content)
content = re.sub(r'logoUrl: "[^"]*"', f'logoUrl: "{LOGO_URL}"', content)
content = content.replace('backgroundColor: "#E6F4FE"', 'backgroundColor: "#FF0000"')
content = content.replace('backgroundColor: "#ffffff"', 'backgroundColor: "#FF0000"')
content = content.replace('backgroundColor: "#000000"', 'backgroundColor: "#190A0A"')
config_path.write_text(content, encoding='utf-8')

print('Marca aplicada com ícone e app.config atualizados.')
