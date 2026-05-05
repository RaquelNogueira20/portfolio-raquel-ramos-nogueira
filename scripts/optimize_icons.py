from pathlib import Path
from PIL import Image

ROOT = Path('/home/ubuntu/culinaria_live_app')
SOURCE = Path('/home/ubuntu/webdev-static-assets/culinaria-live-icon.png')
ASSETS = ROOT / 'assets' / 'images'

sizes = {
    'icon.png': 1024,
    'android-icon-foreground.png': 1024,
    'splash-icon.png': 512,
    'favicon.png': 256,
}

source = Image.open(SOURCE).convert('RGBA')
for filename, size in sizes.items():
    output = ASSETS / filename
    image = source.resize((size, size), Image.Resampling.LANCZOS)
    palette = image.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
    palette.save(output, format='PNG', optimize=True)
    print(f'{filename}: {output.stat().st_size / 1024:.1f} KB')
