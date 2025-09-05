#!/usr/bin/env python3
"""
Script para convertir SVG a ICO
"""

import cairosvg
from PIL import Image
import io

def svg_to_ico(svg_file, ico_file, sizes=[16, 32, 48, 64, 128, 256]):
    """Convertir SVG a ICO con múltiples tamaños"""
    print(f"🎨 Convirtiendo {svg_file} a {ico_file}...")
    
    # Lista para almacenar las imágenes en diferentes tamaños
    images = []
    
    for size in sizes:
        print(f"  📏 Generando tamaño {size}x{size}...")
        
        # Convertir SVG a PNG en memoria
        png_data = cairosvg.svg2png(
            url=svg_file,
            output_width=size,
            output_height=size
        )
        
        # Crear imagen PIL desde los datos PNG
        img = Image.open(io.BytesIO(png_data))
        
        # Convertir a RGBA si es necesario
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        images.append(img)
    
    # Guardar como ICO con múltiples tamaños
    images[0].save(
        ico_file,
        format='ICO',
        sizes=[(img.width, img.height) for img in images],
        append_images=images[1:]
    )
    
    print(f"✅ Icono guardado como {ico_file}")

if __name__ == "__main__":
    try:
        svg_to_ico('icono.svg', 'icono.ico')
        print("🎉 ¡Conversión completada exitosamente!")
    except Exception as e:
        print(f"❌ Error durante la conversión: {e}")
        print("💡 Asegúrate de que el archivo icono.svg existe")
