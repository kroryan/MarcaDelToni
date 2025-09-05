#!/usr/bin/env python3
"""
Script simple para convertir SVG a ICO usando conversión alternativa
"""

from PIL import Image, ImageDraw
import os

def create_simple_ico():
    """Crear un icono simple basado en el concepto del SVG"""
    print("🎨 Creando icono simple para la aplicación...")
    
    # Crear una imagen base de 256x256
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))  # Fondo transparente
    draw = ImageDraw.Draw(img)
    
    # Colores del tema de la aplicación
    bg_color = (65, 105, 225)  # Azul del botón
    text_color = (255, 215, 0)  # Oro del texto
    border_color = (255, 69, 0)  # Naranja del borde
    
    # Dibujar un círculo de fondo
    margin = 20
    draw.ellipse([margin, margin, size-margin, size-margin], 
                fill=bg_color, outline=border_color, width=8)
    
    # Dibujar una "W" estilizada para "Watermark" (Marca de agua)
    try:
        # Intentar usar una fuente del sistema
        from PIL import ImageFont
        try:
            font = ImageFont.truetype("arial.ttf", 120)
        except:
            try:
                font = ImageFont.truetype("Arial.ttf", 120)
            except:
                font = ImageFont.load_default()
    except:
        font = None
    
    # Dibujar texto "W"
    text = "W"
    if font:
        # Calcular posición centrada
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size - text_width) // 2
        y = (size - text_height) // 2 - 10
        
        # Dibujar sombra
        draw.text((x+3, y+3), text, fill=(0, 0, 0, 128), font=font)
        # Dibujar texto principal
        draw.text((x, y), text, fill=text_color, font=font)
    else:
        # Fallback: dibujar formas simples
        center_x, center_y = size // 2, size // 2
        # Dibujar una "W" con líneas
        points = [
            (center_x - 40, center_y - 40),
            (center_x - 20, center_y + 40),
            (center_x, center_y - 20),
            (center_x + 20, center_y + 40),
            (center_x + 40, center_y - 40)
        ]
        for i in range(len(points) - 1):
            draw.line([points[i], points[i + 1]], fill=text_color, width=12)
    
    # Crear diferentes tamaños
    sizes = [16, 32, 48, 64, 128, 256]
    images = []
    
    for s in sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        images.append(resized)
    
    # Guardar como ICO
    ico_path = 'icono.ico'
    images[0].save(
        ico_path,
        format='ICO',
        sizes=[(s, s) for s in sizes],
        append_images=images[1:]
    )
    
    print(f"✅ Icono guardado como {ico_path}")
    return ico_path

if __name__ == "__main__":
    try:
        create_simple_ico()
        print("🎉 ¡Icono creado exitosamente!")
    except Exception as e:
        print(f"❌ Error: {e}")
