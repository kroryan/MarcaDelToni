#!/usr/bin/env python3
"""
Marca de Agua VISIBLE - Versión Simple
Sin dependencias complicadas
"""

import tkinter as tk
from tkinter import font, messagebox, simpledialog
import threading
import time
import sys

class MarcaDeAguaVisible:
    def __init__(self):
        # === CONFIGURACIÓN ===
        self.text = "🌟 OPERATE ENSERIO, COMO PUEDE SER¡¡¡  🌟"
        self.font_size = 64
        self.text_color = "#FFD700"  # Oro brillante
        self.bg_color = "#000080"    # Azul oscuro
        self.border_color = "#FF4500"  # Naranja brillante
        self.transparency = 0.9      # Muy visible
        self.transparency_levels = [0.6, 0.8, 0.95]
        self.current_transparency_index = 2
        
        # Variables de estado
        self.hidden = False
        self.blinking = False
        self.rotating = False
        
        # Crear la ventana principal
        self.root = tk.Tk()
        self.setup_window()
        self.create_gui()
        self.create_controls()
        
        print("🚀 Marca de Agua VISIBLE Iniciada!")
        print("📖 Controles disponibles:")
        print("   • Botón 'Ocultar/Mostrar': Toggle visibilidad")
        print("   • Botón 'Transparencia': Cambiar opacidad")
        print("   • Botón 'Parpadeo': Activar/desactivar parpadeo")
        print("   • Botón 'Cerrar': Salir")
        print("   • Clic y arrastrar: Mover la ventana")
    
    def setup_window(self):
        """Configurar la ventana principal"""
        self.root.title("Marca de Agua")
        self.root.configure(bg='black')  # Fondo negro que será invisible
        self.root.attributes('-topmost', True)  # Siempre encima
        self.root.attributes('-alpha', self.transparency)  # Transparencia
        self.root.overrideredirect(True)  # Sin bordes
        self.root.wm_attributes('-transparentcolor', 'black')  # Hacer negro invisible
        
        # PANTALLA COMPLETA
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Permitir arrastrar la ventana
        self.root.bind('<Button-1>', self.start_drag)
        self.root.bind('<B1-Motion>', self.drag_window)
    
    def start_drag(self, event):
        """Iniciar arrastre de ventana"""
        self.start_x = event.x
        self.start_y = event.y
    
    def drag_window(self, event):
        """Arrastrar ventana"""
        x = self.root.winfo_x() + (event.x - self.start_x)
        y = self.root.winfo_y() + (event.y - self.start_y)
        self.root.geometry(f"+{x}+{y}")
    
    def create_gui(self):
        """Crear la interfaz gráfica"""
        # Etiqueta de texto principal (SIN FRAME, FONDO INVISIBLE)
        self.label = tk.Label(
            self.root,
            text=self.text,
            fg=self.text_color,
            bg='black',  # Fondo negro invisible
            font=('Arial Black', self.font_size, 'bold'),
            anchor='center',
            justify='center'
        )
        self.label.pack(expand=True, fill='both')
        
        # Bind para arrastrar el texto
        self.label.bind('<Button-1>', self.start_drag)
        self.label.bind('<B1-Motion>', self.drag_window)
    
    def create_controls(self):
        """Crear menú desplegable compacto y elegante"""
        # Frame principal del menú (compacto)
        self.menu_frame = tk.Frame(self.root, bg='#2C2C2C', relief='raised', bd=2)
        self.menu_frame.place(x=10, y=10)
        
        # Botón principal del menú (hamburguesa)
        self.menu_button = tk.Button(
            self.menu_frame,
            text="☰ MENÚ",
            command=self.toggle_menu,
            bg='#4169E1',
            fg='white',
            font=('Arial', 12, 'bold'),
            relief='raised',
            bd=2,
            padx=15,
            pady=8,
            width=12
        )
        self.menu_button.pack(padx=5, pady=5)
        
        # Frame para opciones del menú (inicialmente oculto)
        self.options_frame = tk.Frame(self.menu_frame, bg='#2C2C2C')
        
        # Variable para controlar si el menú está abierto
        self.menu_open = False
        
        # Crear todas las opciones del menú
        self.create_menu_options()
    
    def create_menu_options(self):
        """Crear todas las opciones del menú desplegable"""
        # Estilo para botones del menú
        btn_style = {
            'bg': '#5A5A5A',
            'fg': 'white',
            'font': ('Arial', 9, 'normal'),
            'relief': 'flat',
            'bd': 1,
            'padx': 10,
            'pady': 3,
            'width': 16,
            'anchor': 'w'
        }
        
        # Botones del menú
        options = [
            ("👁️  Mostrar/Ocultar", self.toggle_visibility),
            ("🎨  Transparencia", self.cycle_transparency),
            ("✨  Parpadeo", self.toggle_blinking),
            ("🎯  Cambiar Color", self.change_colors),
            ("📏  Tamaño +", self.increase_size),
            ("📏  Tamaño -", self.decrease_size),
            ("📝  Editar Texto", self.edit_text),
            ("🔄  Resetear", self.reset_settings),
            ("❌  Cerrar", self.quit_app)
        ]
        
        for text, command in options:
            btn = tk.Button(
                self.options_frame,
                text=text,
                command=command,
                **btn_style
            )
            btn.pack(fill='x', padx=2, pady=1)
            
            # Efectos hover
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#6B6B6B'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#5A5A5A'))
    
    def toggle_menu(self):
        """Abrir/cerrar el menú desplegable"""
        if self.menu_open:
            # Cerrar menú
            self.options_frame.pack_forget()
            self.menu_button.configure(text="☰ MENÚ", bg='#4169E1')
            self.menu_open = False
            print("📋 Menú cerrado")
        else:
            # Abrir menú
            self.options_frame.pack(fill='x', padx=5, pady=(0, 5))
            self.menu_button.configure(text="✕ CERRAR", bg='#DC143C')
            self.menu_open = True
            print("📋 Menú abierto")
    
    def toggle_visibility(self):
        """Alternar visibilidad de la marca de agua"""
        if self.hidden:
            self.root.deiconify()
            self.root.attributes('-alpha', self.transparency)
            self.hidden = False
            print("👁️  Marca de agua mostrada")
        else:
            self.root.withdraw()
            self.hidden = True
            print("🙈 Marca de agua oculta")
    
    def cycle_transparency(self):
        """Cambiar nivel de transparencia"""
        self.current_transparency_index = (self.current_transparency_index + 1) % len(self.transparency_levels)
        self.transparency = self.transparency_levels[self.current_transparency_index]
        
        if not self.hidden:
            self.root.attributes('-alpha', self.transparency)
        
        percentage = int(self.transparency * 100)
        print(f"🎨 Transparencia cambiada a {percentage}%")
    
    def toggle_blinking(self):
        """Activar/desactivar parpadeo"""
        self.blinking = not self.blinking
        if self.blinking:
            self.start_blinking()
            print("✨ Parpadeo activado")
        else:
            print("🔇 Parpadeo desactivado")
    
    def start_blinking(self):
        """Iniciar efecto de parpadeo"""
        def blink():
            while self.blinking and not self.hidden:
                try:
                    # Cambiar color del texto
                    colors = ['#FFD700', '#FF4500', '#00FF00', '#FF1493', '#00FFFF']
                    for color in colors:
                        if not self.blinking:
                            break
                        self.label.configure(fg=color)
                        self.root.update()
                        time.sleep(0.3)
                except:
                    break
            # Restaurar color original
            self.label.configure(fg=self.text_color)
        
        threading.Thread(target=blink, daemon=True).start()
    
    def change_colors(self):
        """Cambiar esquema de colores"""
        color_schemes = [
            {'bg': '#000080', 'text': '#FFD700', 'border': '#FF4500'},  # Azul/Oro
            {'bg': '#8B0000', 'text': '#00FF00', 'border': '#FFFF00'},  # Rojo/Verde
            {'bg': '#2F4F4F', 'text': '#FF69B4', 'border': '#00CED1'},  # Gris/Rosa
            {'bg': '#4B0082', 'text': '#FFE4E1', 'border': '#FF6347'},  # Púrpura/Blanco
        ]
        
        import random
        scheme = random.choice(color_schemes)
        
        self.bg_color = scheme['bg']
        self.text_color = scheme['text']
        self.border_color = scheme['border']
        
        self.root.configure(bg='black')  # Fondo invisible
        self.label.configure(bg='black', fg=self.text_color)  # Actualizar fondo
        
        print(f"🎯 Colores cambiados: Fondo={self.bg_color}, Texto={self.text_color}")
    
    def increase_size(self):
        """Aumentar tamaño del texto"""
        if self.font_size < 120:
            self.font_size += 10
            self.label.configure(font=('Arial Black', self.font_size, 'bold'))
            print(f"📏 Tamaño aumentado a {self.font_size}")
    
    def decrease_size(self):
        """Disminuir tamaño del texto"""
        if self.font_size > 20:
            self.font_size -= 10
            self.label.configure(font=('Arial Black', self.font_size, 'bold'))
            print(f"📏 Tamaño reducido a {self.font_size}")
    
    def edit_text(self):
        """Editar el texto de la marca de agua"""
        from tkinter import simpledialog
        new_text = simpledialog.askstring(
            "Editar Texto", 
            "Ingresa el nuevo texto:", 
            initialvalue=self.text
        )
        if new_text:
            self.text = new_text
            self.label.configure(text=self.text)
            print(f"📝 Texto cambiado a: {self.text}")
    
    def reset_settings(self):
        """Resetear todas las configuraciones"""
        self.text = "🌟 TONY ERES MAS FEO QUE PEGARLE A UN PADRE  🌟"
        self.font_size = 64
        self.text_color = "#FFD700"
        self.transparency = 0.9
        self.current_transparency_index = 2
        
        self.label.configure(
            text=self.text,
            fg=self.text_color,
            font=('Arial Black', self.font_size, 'bold')
        )
        self.root.attributes('-alpha', self.transparency)
        
        # Cerrar menú si está abierto
        if self.menu_open:
            self.toggle_menu()
        
        print("🔄 Configuraciones reseteadas")
    
    def quit_app(self):
        """Cerrar la aplicación"""
        print("👋 Cerrando marca de agua...")
        self.blinking = False
        try:
            self.root.quit()
            self.root.destroy()
        except:
            pass
        sys.exit(0)
    
    def run(self):
        """Ejecutar la aplicación"""
        try:
            # Protocolo para cerrar ventana
            self.root.protocol("WM_DELETE_WINDOW", self.quit_app)
            
            # Mostrar mensaje inicial
            self.root.after(1000, lambda: messagebox.showinfo(
                "Marca de Agua Activa", 
                "¡La marca de agua está funcionando!\n\n" +
                "• Usa los botones para controlarla\n" +
                "• Arrastra la ventana para moverla\n" +
                "• Siempre está encima de otras ventanas"
            ))
            
            # Iniciar loop principal
            self.root.mainloop()
            
        except KeyboardInterrupt:
            self.quit_app()
        except Exception as e:
            print(f"❌ Error: {e}")
            self.quit_app()

def main():
    """Función principal"""
    print("🎯 Iniciando Marca de Agua VISIBLE...")
    print("=" * 50)
    
    try:
        app = MarcaDeAguaVisible()
        app.run()
    except Exception as e:
        print(f"❌ Error fatal: {e}")
        input("Presiona Enter para salir...")

if __name__ == "__main__":
    main()
