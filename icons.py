#! Instalar o GTK
#todo https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe

#! Instalar Python 
#todo https://www.python.org/downloads/

#! Instalar biblioteclas pelo prompt
#todo pip install cairosvg Pillow

#! Alterar os caminhos das variaveis svg_folder e output_folder

#! Rodar o arquivo pelo prompt
#todo python icons.py

import os
from PIL import Image
import glob
import cairosvg

svg_folder = "C:\\Users\\GSperandio\\OneDrive - SEBRAE\\Área de trabalho\\Python\\newIcons"

output_folder = "C:\\Users\\GSperandio\\OneDrive - SEBRAE\\Área de trabalho\\Python\\newOutputo"

svg_files = glob.glob(os.path.join(svg_folder, '*.svg'))

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for svg_file in svg_files:
    png_file = os.path.splitext(os.path.basename(svg_file))[0] + '.png'
    png_path = os.path.join(output_folder, png_file)
    
    cairosvg.svg2png(url=svg_file, write_to=png_path)

gallery_html = '<html><body>'
for svg_file, png_file in zip(svg_files, os.listdir(output_folder)):
    gallery_html += f'<div><h2>{os.path.basename(svg_file)}</h2>'
    gallery_html += f'<img src="{png_file}" width="100"></div>'
gallery_html += '</body></html>'

gallery_html_path = os.path.join(output_folder, 'gallery.html')
with open(gallery_html_path, 'w') as f:
    f.write(gallery_html)

print(f'Galeria HTML gerada em: {gallery_html_path}')
