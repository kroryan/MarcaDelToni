# 🌟 Marca del Toni - Texto Flotante para Windows

Una aplicación de marca de agua personalizable que muestra texto flotante transparente en tu pantalla de Windows. Perfecto para branding, recordatorios o simplemente diversión.

## 📋 Tabla de Contenidos
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Compilación](#-compilación)
- [Controles](#-controles)
- [Personalización](#-personalización)
- [Solución de Problemas](#-solución-de-problemas)
- [Créditos](#-créditos)

## ✨ Características

- 🎯 **Texto flotante personalizable** con fondo invisible
- 🎨 **Múltiples esquemas de colores** y efectos visuales
- 📏 **Tamaño de texto ajustable** en tiempo real
- 👁️ **Mostrar/ocultar** con un clic
- ✨ **Efecto de parpadeo** con colores parpadeantes
- 🔄 **Configuración reseteable** a valores por defecto
- 📝 **Editor de texto integrado** para cambiar el mensaje
- 🌈 **Múltiples niveles de transparencia**
- 📺 **Pantalla completa** automática
- 🖱️ **Menú desplegable** intuitivo
- 🔝 **Siempre visible** sobre otras ventanas
- 🎮 **Fácil de usar** sin conocimientos técnicos

## 🔧 Requisitos

### Para usar el .exe (Recomendado):
- Windows 7/8/10/11
- ¡Eso es todo! No necesitas instalar nada más

### Para ejecutar desde código fuente:
- Python 3.6 o superior
- PyInstaller (para compilar a .exe)
- Tkinter (incluido con Python)

## 📦 Instalación

### Opción 1: Usar el ejecutable (Más fácil)
1. Descarga `MarcaDelToni.exe` de la carpeta `dist/`
2. Ejecuta el archivo
3. ¡Listo!

### Opción 2: Desde código fuente
1. Clona o descarga este repositorio
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python marca_de_agua_visible.py
   ```

### Opción 3: Compilar tu propio .exe
1. Clona el repositorio e instala dependencias:
   ```bash
   git clone https://github.com/tu-usuario/marca-del-toni.git
   cd marca-del-toni
   pip install -r requirements.txt
   ```
2. Ejecuta el script de compilación:
   ```bash
   compilar_simple.bat
   ```
   O manualmente:
   ```bash
   pyinstaller --onefile --windowed --name="MarcaDelToni" marca_de_agua_visible.py
   ```
3. Tu .exe estará en la carpeta `dist/`

## 🚀 Uso

### Inicio Rápido
1. Ejecuta `MarcaDeAgua.exe` o `python marca_de_agua_visible.py`
2. Aparecerá texto flotante en tu pantalla
3. Busca el botón **"☰ MENÚ"** en la esquina superior izquierda
4. Haz clic para abrir las opciones

### Primera Ejecución
- El programa mostrará un mensaje de confirmación
- El texto aparecerá centrado en pantalla completa
- El fondo será completamente invisible
- Solo verás el texto flotando

## 🎮 Controles

### Menú Principal
Haz clic en **"☰ MENÚ"** para acceder a todas las opciones:

| Opción | Función | Descripción |
|--------|---------|-------------|
| **👁️ Mostrar/Ocultar** | Toggle visibilidad | Oculta o muestra la marca de agua |
| **🎨 Transparencia** | Cambiar opacidad | Cicla entre 60%, 80%, 95% |
| **✨ Parpadeo** | Efecto visual | Activa/desactiva colores parpadeantes |
| **🎯 Cambiar Color** | Esquemas de color | Cambia colores aleatoriamente |
| **📏 Tamaño +** | Aumentar texto | Hace el texto más grande |
| **📏 Tamaño -** | Reducir texto | Hace el texto más pequeño |
| **📝 Editar Texto** | Cambiar mensaje | Abre editor para nuevo texto |
| **🔄 Resetear** | Configuración original | Vuelve a configuración por defecto |
| **❌ Cerrar** | Salir | Cierra completamente la aplicación |

### Interacción con Mouse
- **Arrastrar**: Haz clic y arrastra el texto para moverlo
- **Clic derecho**: (Funcionalidad limitada debido a transparencia)

## 🎨 Personalización

### Cambiar el Texto
1. Abre el menú (**☰ MENÚ**)
2. Selecciona **📝 Editar Texto**
3. Escribe tu nuevo mensaje
4. Presiona **OK**

### Esquemas de Colores Disponibles
- **Azul/Oro**: Fondo azul, texto dorado (por defecto)
- **Rojo/Verde**: Fondo rojo, texto verde neón
- **Gris/Rosa**: Fondo gris, texto rosa brillante
- **Púrpura/Blanco**: Fondo púrpura, texto blanco

### Niveles de Transparencia
- **60%**: Muy transparente
- **80%**: Transparencia media
- **95%**: Casi opaco (por defecto)

### Rangos de Tamaño
- **Mínimo**: 20 puntos
- **Por defecto**: 64 puntos
- **Máximo**: 120 puntos

## 🔨 Compilación

### Instalación Rápida de Dependencias
```bash
pip install -r requirements.txt
```

### Compilación Automática
Usa uno de los scripts incluidos:

```bash
# Compilación simple
compilar_simple.bat

# Compilación avanzada (con más opciones)
compilar.bat
```

### Compilación Manual
```bash
pyinstaller --onefile --windowed --name="MarcaDelToni" marca_de_agua_visible.py
```

### Lista de Dependencias
El archivo `requirements.txt` incluye:
- `pyinstaller>=6.0.0` - Para compilar a .exe
- `tkinter` - Para la interfaz gráfica (incluido con Python)

### Parámetros de PyInstaller
- `--onefile`: Crea un solo archivo .exe
- `--windowed`: Sin ventana de consola
- `--name`: Nombre del ejecutable final

## 🐛 Solución de Problemas

### El texto no aparece
1. Verifica que la transparencia no esté al mínimo
2. Prueba cambiar colores con **🎯 Cambiar Color**
3. Resetea configuración con **🔄 Resetear**

### No veo el menú
- El botón **☰ MENÚ** está en la esquina superior izquierda
- Si no lo ves, presiona **Alt+Tab** para cambiar ventanas

### El programa se cierra inesperadamente
1. Ejecuta desde terminal para ver errores:
   ```bash
   python marca_de_agua_visible.py
   ```
2. Verifica que tengas Python 3.6+ instalado

### Problemas de transparencia
- La transparencia requiere Windows
- En sistemas muy antiguos puede no funcionar correctamente

### El .exe es muy grande
- Es normal, PyInstaller incluye Python completo
- Tamaño típico: 15-25 MB

## 📁 Estructura de Archivos

```
marca-del-toni/
├── marca_de_agua_visible.py    # Código fuente principal
├── requirements.txt            # Dependencias Python
├── compilar.bat                # Script de compilación avanzado
├── compilar_simple.bat         # Script de compilación simple
├── .gitignore                  # Archivos ignorados por Git
├── README.md                   # Este archivo
├── dist/                       # Ejecutables compilados
│   └── MarcaDelToni.exe       # Tu aplicación final
├── build/                      # Archivos temporales (ignorados)
└── MarcaDelToni.spec          # Configuración PyInstaller
```

## 💡 Consejos de Uso

### Para Presentaciones
1. Configura tu mensaje antes de presentar
2. Usa transparencia alta (95%)
3. Elige colores que contrasten con tu contenido

### Para Branding
1. Usa el nombre de tu empresa/canal
2. Coloca en una esquina con **📏 Tamaño -**
3. Usa transparencia media (80%)

### Para Recordatorios
1. Escribe tu recordatorio en **📝 Editar Texto**
2. Activa **✨ Parpadeo** para llamar la atención
3. Usa colores brillantes

## 🎯 Casos de Uso

- **Streamers**: Marca de agua en streams
- **Presentaciones**: Branding corporativo
- **Trabajo**: Recordatorios importantes
- **Diversión**: Mensajes graciosos flotantes
- **Productividad**: Frases motivacionales

## 🔄 Actualizaciones Futuras

Próximas características planeadas:
- [ ] Efectos de rotación
- [ ] Múltiples textos simultáneos
- [ ] Configuración de posición fija
- [ ] Soporte para imágenes
- [ ] Horarios programados
- [ ] Integración con hotkeys globales

## 📞 Soporte

Si tienes problemas:
1. Revisa la sección [Solución de Problemas](#-solución-de-problemas)
2. Verifica que tengas la versión correcta de Windows
3. Ejecuta desde terminal para ver mensajes de error

## 📄 Licencia

Este proyecto es de uso libre. Puedes modificar, distribuir y usar como desees.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres agregar características:
1. Haz un fork del proyecto
2. Crea una rama para tu característica
3. Envía un pull request

## 🎉 Créditos

- **Desarrollado en**: Python + Tkinter
- **Compilado con**: PyInstaller
- **Inspirado en**: AutoHotkey scripts
- **Diseño**: Interfaz minimalista y funcional

---

### 🚀 ¡Disfruta tu Marca de Agua personalizada!

**Versión**: 1.0  
**Última actualización**: Septiembre 2025  
**Compatibilidad**: Windows 7/8/10/11
