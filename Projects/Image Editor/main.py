import customtkinter as ctk
from image_widgets import * 
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter
from menu import Menu
from ttkbootstrap.toast import ToastNotification
import winsound

class App(ctk.CTk):
    def __init__(self):

        # setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800,500)
        self.init_parameters()

        # layout
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 2, uniform = 'a')
        self.columnconfigure(1, weight = 6, uniform = 'a')

        # canvas data
        self.image_width = 0
        self.image_height = 0
        self.canvas_width = 0
        self.canvas_height = 0

        # widgets
        self.image_import = ImageImport(self, self.import_image)

        # run
        self.mainloop()

    def init_parameters(self):
        # variables
        self.pos_vars = {
            'rotate': ctk.DoubleVar(value = ROTATE_DEFAULT),
            'zoom': ctk.DoubleVar(value = ZOOM_DEFAULT),
            'flip': ctk.StringVar(value = FLIP_OPTIONS[0])}
        
        self.color_vars = {
            'brightness': ctk.DoubleVar(value = BRIGHTNESS_DEFAULT),
            'grayscale': ctk.BooleanVar(value = GRAYSCALE_DEFAULT),
            'invert': ctk.BooleanVar(value = INVERT_DEFAULT),
            'vibrance': ctk.DoubleVar(value = VIBRANCE_DEFAULT)}
        
        self.effect_vars = {
            'blur': ctk.DoubleVar(value = BLUR_DEFAULT),
            'contrast': ctk.IntVar(value = CONTRAST_DEFAULT),
            'effect': ctk.StringVar(value = EFFECT_OPTIONS[0])}
        
        combined_list = list(self.pos_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values())
        for var in combined_list:
            var.trace('w', self.manipulate_image)

    def manipulate_image(self, *args):
        self.image = self.original

        # ----Position----
        # rotate
        if self.pos_vars['rotate'].get() != ROTATE_DEFAULT:
            self.image = self.image.rotate(self.pos_vars['rotate'].get())
        
        # zoom
        if self.pos_vars['zoom'].get() != ZOOM_DEFAULT:
            self.image = ImageOps.crop(image = self.image, border = self.pos_vars['zoom'].get())
        
        # flip
        if self.pos_vars['flip'].get() != FLIP_OPTIONS[0]:
            if self.pos_vars['flip'].get() == 'X':
                self.image = ImageOps.mirror(self.image)

            if self.pos_vars['flip'].get() == 'Y':
                self.image = ImageOps.flip(self.image)

            if self.pos_vars['flip'].get() == 'Both':
                self.image = ImageOps.mirror(self.image)
                self.image = ImageOps.flip(self.image)

        # ----Color----
        # brightness & vibrance
        if self.color_vars['brightness'].get() != BRIGHTNESS_DEFAULT:
            brightness_enhancer = ImageEnhance.Brightness(self.image)
            self.image = brightness_enhancer.enhance(self.color_vars['brightness'].get())

        if self.color_vars['vibrance'].get() != VIBRANCE_DEFAULT:
            vibrance_enhancer = ImageEnhance.Color(self.image)
            self.image = vibrance_enhancer.enhance(self.color_vars['vibrance'].get()) 

        # grayscale & invert(color)
        if self.color_vars['grayscale'].get():
            self.image = ImageOps.grayscale(self.image)
        
        if self.color_vars['invert'].get():
            self.image = ImageOps.invert(self.image)

        # ----Effects----
        # blur & contrast
        if self.effect_vars['blur'].get() != BLUR_DEFAULT:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.effect_vars['blur'].get()))
        if self.effect_vars['contrast'].get() != CONTRAST_DEFAULT:
            self.image = self.image.filter(ImageFilter.UnsharpMask(self.effect_vars['contrast'].get()))
        match self.effect_vars['effect'].get():
            case 'Emboss': self.image = self.image.filter(ImageFilter.EMBOSS)
            case 'Find edges': self.image = self.image.filter(ImageFilter.FIND_EDGES)
            case 'Contour': self.image = self.image.filter(ImageFilter.CONTOUR)
            case 'Edge enhance': self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)

        # place image
        self.place_image()

    def import_image(self, path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)

        self.image_import.grid_forget()
        self.image_output = ImageOutput(self, self.resize_image)
        self.close_button = CloseOutput(self, self.close_edit)
        self.menu = Menu(self, self.pos_vars, self.color_vars, self.effect_vars, self.export_image)
        
    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        
        self.image_import = ImageImport(self, self.import_image)

    def resize_image(self, event):
        
        # current canvas ratio
        canvas_ratio = event.width / event.height
        
        # update canvas attributes
        self.canvas_width = event.width
        self.canvas_height = event.height

        # resize
        if canvas_ratio > self.image_ratio: # canvas is wider than the image
            self.image_height = event.height
            self.image_width = self.image_height * self.image_ratio
        else: # canvas is taller than the image
            self.image_width = event.width
            self.image_height = self.image_width / self.image_ratio
        
        # place image
        self.place_image()

    def place_image(self):
        self.image_output.delete('all')
        resized_image = self.image.resize((int(self.image_width), int(self.image_height)))
        self.image_tk = ImageTk.PhotoImage(resized_image)

        self.image_output.create_image(self.canvas_width / 2, self.canvas_height / 2, image = self.image_tk)
    
    def export_image(self, name, file, path):
        # save image
        export_string = f'{path}/{name}.{file}'
        self.image.save(export_string)

        # Notification        
        self.save_toast()
    
    def save_toast(self):
        # pop sound
        winsound.MessageBeep(winsound.MB_ICONASTERISK)

        # message small window
        window = ctk.CTkToplevel()
        window.geometry('250x120')
        window.attributes('-topmost', True)
        window.title('')

        ctk.CTkLabel(window, text = 'Image Saved...', font = ('Arial', 18)).pack(expand = True, pady = 10)
        ctk.CTkButton(window, text = 'Close', command = window.destroy).pack(expand = True, pady = 10)

        window.mainloop()

if __name__ == '__main__':
    App()