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
        self.move_mode = False  # Modo de movimiento del texto
        
        # Sistema de múltiples textos
        self.texts = [self.text]  # Lista de textos
        self.current_text_index = 0
        self.labels = []  # Lista de labels para múltiples textos
        
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
        print("   • Botón 'Modo Mover': Activar movimiento individual de textos")
        print("   • Botón 'Añadir Texto': Agregar textos adicionales")
        print("   • Botón 'Quitar Texto': Eliminar textos")
        print("   • Botón 'Lista Textos': Ver todos los textos activos")
        print("   • Botón 'Cerrar': Salir")
        print("   • Clic y arrastrar: Mover la ventana")
        print("   • Doble clic en texto: Editar texto individual")
    
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
        
        # Variables para el arrastre de ventana
        self.window_drag_data = {"x": 0, "y": 0}
        
        # NO bind directo en root para evitar conflictos
    
    def start_drag(self, event):
        """Iniciar arrastre de ventana (solo para áreas no-texto)"""
        self.window_drag_data["x"] = event.x
        self.window_drag_data["y"] = event.y
    
    def drag_window(self, event):
        """Arrastrar ventana completa (solo para áreas no-texto)"""
        x = self.root.winfo_x() + (event.x - self.window_drag_data["x"])
        y = self.root.winfo_y() + (event.y - self.window_drag_data["y"])
        self.root.geometry(f"+{x}+{y}")
    
    def create_gui(self):
        """Crear la interfaz gráfica"""
        # Frame contenedor para múltiples textos
        self.text_container = tk.Frame(self.root, bg='black')
        self.text_container.pack(expand=True, fill='both')
        
        # Hacer que el contenedor también sirva para arrastrar cuando no hay modo movimiento
        self.text_container.bind('<Button-1>', self.on_container_click)
        self.text_container.bind('<B1-Motion>', self.on_container_drag)
        
        # Crear el primer texto (principal)
        self.create_text_label(self.text, 0)
    
    def on_container_click(self, event):
        """Manejar clic en el contenedor (área vacía)"""
        if not self.move_mode:
            # Solo arrastrar ventana si no estamos en modo movimiento
            self.start_drag(event)
            print("🎯 Arrastrando ventana completa desde área vacía")
    
    def on_container_drag(self, event):
        """Manejar arrastre en el contenedor"""
        if not self.move_mode:
            self.drag_window(event)
    
    def create_text_label(self, text, index):
        """Crear una nueva etiqueta de texto"""
        label = tk.Label(
            self.text_container,
            text=text,
            fg=self.text_color,
            bg='black',  # Fondo negro invisible
            font=('Arial Black', self.font_size, 'bold'),
            anchor='center',
            justify='center'
        )
        
        # Posicionamiento dinámico para múltiples textos
        if index == 0:
            label.pack(expand=True, fill='both')
        else:
            # Textos adicionales se posicionan en lugares específicos
            positions = [
                {'relx': 0.2, 'rely': 0.3, 'anchor': 'center'},
                {'relx': 0.8, 'rely': 0.3, 'anchor': 'center'},
                {'relx': 0.5, 'rely': 0.7, 'anchor': 'center'},
                {'relx': 0.1, 'rely': 0.8, 'anchor': 'center'},
                {'relx': 0.9, 'rely': 0.8, 'anchor': 'center'}
            ]
            pos_index = (index - 1) % len(positions)
            label.place(**positions[pos_index])
        
        # Variables para el arrastre individual
        label.drag_data = {"x": 0, "y": 0}
        
        # Bind para manejo de eventos del texto
        label.bind('<Button-1>', lambda e, l=label: self.on_text_click(e, l))
        label.bind('<B1-Motion>', lambda e, l=label: self.on_text_drag(e, l))
        label.bind('<Double-Button-1>', lambda e, l=label: self.edit_individual_text(l))
        label.bind('<ButtonRelease-1>', lambda e, l=label: self.on_text_release(e, l))
        
        self.labels.append(label)
        
        # Si es el primer label, mantener referencia para compatibilidad
        if index == 0:
            self.label = label
        
        return label
    
    def on_text_click(self, event, label):
        """Manejar clic en texto"""
        if self.move_mode:
            # Modo movimiento: preparar para arrastrar texto
            label.drag_data["x"] = event.x
            label.drag_data["y"] = event.y
            print(f"🎯 Texto seleccionado para mover")
        else:
            # Modo normal: arrastrar ventana completa
            self.start_drag(event)
    
    def on_text_drag(self, event, label):
        """Manejar arrastre en texto"""
        if self.move_mode:
            # Modo movimiento: mover solo este texto
            self.drag_individual_text(event, label)
        else:
            # Modo normal: arrastrar ventana completa
            self.drag_window(event)
    
    def on_text_release(self, event, label):
        """Manejar liberación del clic en texto"""
        if self.move_mode:
            print(f"🎯 Texto posicionado")
    
    def drag_individual_text(self, event, label):
        """Arrastrar texto individual (solo en modo movimiento)"""
        try:
            # Calcular nueva posición relativa al contenedor
            container_x = self.text_container.winfo_x()
            container_y = self.text_container.winfo_y()
            container_width = self.text_container.winfo_width()
            container_height = self.text_container.winfo_height()
            
            # Posición del mouse relativa al contenedor
            mouse_x = event.x_root - container_x - self.root.winfo_x()
            mouse_y = event.y_root - container_y - self.root.winfo_y()
            
            # Convertir a posición relativa (0.0 a 1.0)
            if container_width > 0 and container_height > 0:
                rel_x = max(0.0, min(1.0, mouse_x / container_width))
                rel_y = max(0.0, min(1.0, mouse_y / container_height))
                
                # Actualizar posición del label
                label.place(relx=rel_x, rely=rel_y, anchor='center')
        except Exception as e:
            print(f"Error moviendo texto: {e}")
    
    def start_text_drag(self, event, label):
        """FUNCIÓN OBSOLETA - Mantenida para compatibilidad"""
        pass
    
    def drag_text(self, event, label):
        """FUNCIÓN OBSOLETA - Mantenida para compatibilidad"""
        pass
    
    def edit_individual_text(self, label):
        """Editar texto individual con doble clic"""
        from tkinter import simpledialog
        current_text = label.cget('text')
        new_text = simpledialog.askstring(
            "Editar Texto Individual", 
            "Ingresa el nuevo texto:", 
            initialvalue=current_text
        )
        if new_text:
            label.configure(text=new_text)
            # Actualizar en la lista de textos
            index = self.labels.index(label)
            if index < len(self.texts):
                self.texts[index] = new_text
            print(f"📝 Texto individual editado: {new_text}")
    
    def create_controls(self):
        """Crear menú desplegable compacto y elegante"""
        # Frame principal del menú (compacto)
        self.menu_frame = tk.Frame(self.root, bg='#2C2C2C', relief='raised', bd=2)
        self.menu_frame.place(x=10, y=10)
        
        # Hacer que el frame del menú sirva para arrastrar la ventana
        self.menu_frame.bind('<Button-1>', self.start_drag)
        self.menu_frame.bind('<B1-Motion>', self.drag_window)
        
        # Área de arrastre adicional en la esquina superior derecha
        self.drag_area = tk.Label(
            self.root,
            text="⚡ ARRASTRAR",
            bg='#2C2C2C',
            fg='white',
            font=('Arial', 8, 'bold'),
            relief='raised',
            bd=1,
            padx=5,
            pady=2
        )
        self.drag_area.place(x=self.root.winfo_screenwidth()-120, y=10)
        
        # Hacer que el área de arrastre funcione
        self.drag_area.bind('<Button-1>', self.start_drag)
        self.drag_area.bind('<B1-Motion>', self.drag_window)
        
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
            ("🎯  Modo Mover", self.toggle_move_mode),
            ("➕  Añadir Texto", self.add_new_text),
            ("🗑️  Quitar Texto", self.remove_text),
            ("📋  Lista Textos", self.show_texts_list),
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
                    # Cambiar color del texto en todas las etiquetas
                    colors = ['#FFD700', '#FF4500', '#00FF00', '#FF1493', '#00FFFF']
                    for color in colors:
                        if not self.blinking:
                            break
                        for label in self.labels:
                            label.configure(fg=color)
                        self.root.update()
                        time.sleep(0.3)
                except:
                    break
            # Restaurar color original en todas las etiquetas
            for label in self.labels:
                label.configure(fg=self.text_color)
        
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
        # Actualizar color en todas las etiquetas
        for label in self.labels:
            label.configure(bg='black', fg=self.text_color)
        
        print(f"🎯 Colores cambiados: Fondo={self.bg_color}, Texto={self.text_color}")
    
    def increase_size(self):
        """Aumentar tamaño del texto"""
        if self.font_size < 120:
            self.font_size += 10
            # Actualizar fuente en todas las etiquetas
            for label in self.labels:
                label.configure(font=('Arial Black', self.font_size, 'bold'))
            print(f"📏 Tamaño aumentado a {self.font_size}")
    
    def decrease_size(self):
        """Disminuir tamaño del texto"""
        if self.font_size > 20:
            self.font_size -= 10
            # Actualizar fuente en todas las etiquetas
            for label in self.labels:
                label.configure(font=('Arial Black', self.font_size, 'bold'))
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
            self.texts[0] = new_text  # Actualizar en la lista
            self.label.configure(text=self.text)
            print(f"📝 Texto cambiado a: {self.text}")
    
    def toggle_move_mode(self):
        """Activar/desactivar modo de movimiento de textos"""
        self.move_mode = not self.move_mode
        if self.move_mode:
            print("🎯 Modo movimiento ACTIVADO")
            print("   💡 Tip: Haz clic y arrastra cualquier texto para moverlo")
            print("   💡 Tip: Doble clic en un texto para editarlo")
            print("   💡 Tip: Haz clic en áreas vacías para mover toda la ventana")
            # Cambiar cursor para indicar modo de movimiento
            for label in self.labels:
                label.configure(cursor='fleur')
        else:
            print("🎯 Modo movimiento DESACTIVADO")
            print("   💡 Ahora puedes arrastrar toda la ventana desde cualquier texto")
            # Restaurar cursor normal
            for label in self.labels:
                label.configure(cursor='')
    
    def add_new_text(self):
        """Añadir un nuevo texto separado"""
        from tkinter import simpledialog
        new_text = simpledialog.askstring(
            "Nuevo Texto", 
            "Ingresa el texto a añadir:",
            initialvalue="🆕 Nuevo texto aquí"
        )
        if new_text:
            self.texts.append(new_text)
            index = len(self.texts) - 1
            new_label = self.create_text_label(new_text, index)
            print(f"➕ Nuevo texto añadido: {new_text}")
            print(f"📊 Total de textos: {len(self.texts)}")
    
    def remove_text(self):
        """Quitar un texto (excepto el principal)"""
        if len(self.labels) <= 1:
            print("❌ No se puede eliminar el texto principal")
            return
        
        from tkinter import simpledialog, messagebox
        
        # Mostrar lista de textos para seleccionar
        text_list = []
        for i, text in enumerate(self.texts):
            preview = text[:30] + "..." if len(text) > 30 else text
            text_list.append(f"{i+1}. {preview}")
        
        selection = simpledialog.askstring(
            "Quitar Texto",
            f"Textos disponibles:\n" + "\n".join(text_list) + "\n\n" +
            "Ingresa el número del texto a eliminar (No se puede eliminar el 1):"
        )
        
        try:
            index = int(selection) - 1
            if index == 0:
                messagebox.showwarning("Error", "No se puede eliminar el texto principal")
                return
            if 0 < index < len(self.labels):
                # Eliminar label
                self.labels[index].destroy()
                self.labels.pop(index)
                # Eliminar de la lista de textos
                removed_text = self.texts.pop(index)
                print(f"🗑️ Texto eliminado: {removed_text}")
                print(f"📊 Total de textos: {len(self.texts)}")
            else:
                messagebox.showerror("Error", "Número inválido")
        except (ValueError, IndexError):
            messagebox.showerror("Error", "Selección inválida")
    
    def show_texts_list(self):
        """Mostrar lista de todos los textos"""
        from tkinter import messagebox
        if not self.texts:
            messagebox.showinfo("Lista de Textos", "No hay textos activos")
            return
        
        text_list = []
        for i, text in enumerate(self.texts):
            status = "🟢 Activo" if i < len(self.labels) else "🔴 Inactivo"
            preview = text[:40] + "..." if len(text) > 40 else text
            text_list.append(f"{i+1}. {status} {preview}")
        
        message = "📋 LISTA DE TEXTOS ACTIVOS:\n\n" + "\n".join(text_list)
        message += f"\n\n📊 Total: {len(self.texts)} textos"
        message += f"\n🎯 Modo movimiento: {'ACTIVADO' if self.move_mode else 'DESACTIVADO'}"
        
        messagebox.showinfo("Lista de Textos", message)
    
    def reset_settings(self):
        """Resetear todas las configuraciones"""
        # Limpiar textos adicionales
        for i in range(len(self.labels) - 1, 0, -1):
            self.labels[i].destroy()
        
        # Resetear listas
        self.labels = self.labels[:1]  # Mantener solo el principal
        self.texts = [self.texts[0]]   # Mantener solo el texto principal
        
        # Resetear configuraciones
        self.text = "🌟 TONY ERES MAS FEO QUE PEGARLE A UN PADRE  🌟"
        self.texts[0] = self.text
        self.font_size = 64
        self.text_color = "#FFD700"
        self.transparency = 0.9
        self.current_transparency_index = 2
        self.move_mode = False
        
        # Actualizar label principal
        self.label.configure(
            text=self.text,
            fg=self.text_color,
            font=('Arial Black', self.font_size, 'bold'),
            cursor=''
        )
        self.root.attributes('-alpha', self.transparency)
        
        # Cerrar menú si está abierto
        if self.menu_open:
            self.toggle_menu()
        
        print("🔄 Configuraciones reseteadas")
        print("📊 Textos limpiados - Solo queda el texto principal")
    
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
                "🆕 NUEVAS FUNCIONES:\n" +
                "• 🎯 Modo Mover: Mueve textos individualmente\n" +
                "• ➕ Añadir textos múltiples y separados\n" +
                "• 📝 Doble clic para editar textos\n" +
                "• 📋 Ver lista completa de textos\n\n" +
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
