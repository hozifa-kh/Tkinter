import customtkinter as ctk
from PIL import Image
import darkdetect
from buttons import Button, ImageButton, NumButton, MathButton, MathImageButton
from settings import *
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

class Calculator(ctk.CTk):
    def __init__(self, is_dark):

        # setup
        super().__init__(fg_color = (WHITE, BLACK))
        ctk.set_appearance_mode(f'{'dark' if is_dark else 'light'}')
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}') 
        self.resizable(False, False)
        self.title('')
        self.iconbitmap('empty.ico')
        self.title_bar_color(is_dark)

        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')

        # data
        self.result_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')
        self.display_nums = []
        self.full_operation = []

        self.is_result = False
        self.font_size = 70
        self.zero_div = False

        # widgets
        self.create_widgets()

        # events
        self.result_label.bind('<Configure>', self.change_font_size)

        # run 
        self.mainloop()

    def create_widgets(self):
        '''Create all buttons and labels (Widgets)'''
        
        # fonts
        main_font = ctk.CTkFont(FONT, NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(FONT, OUTPUT_FONT_SIZE)

        # output labels
        self.formula_label = OutputLabel(self, 0, 'se', main_font, self.formula_string) # fomula
        self.result_label = OutputLabel(self, 1, 'e', result_font, self.result_string) # result

        # clear (AC) button
        Button(
            parent = self,
            func = self.clear,
            text = OPERATORS['clear']['text'],
            col = OPERATORS['clear']['col'],
            row = OPERATORS['clear']['row'],
            font = main_font)
        
        # percentage (%) button
        Button(
            parent = self,
            func = self.percent,
            text = OPERATORS['percent']['text'],
            col = OPERATORS['percent']['col'],
            row = OPERATORS['percent']['row'],
            font = main_font)

        # invert (+/-) Button
        invert_image = ctk.CTkImage(light_image = Image.open(OPERATORS['invert']['image path']['dark']),
                                    dark_image = Image.open(OPERATORS['invert']['image path']['light']))
        ImageButton(
            parent = self,
            func = self.invert,
            image = invert_image,
            col = OPERATORS['invert']['col'],
            row = OPERATORS['invert']['row'])
        
        # number buttons
        for num , data in NUM_POSITIONS.items():
            NumButton(
                parent = self,
                text = num,
                func = self.num_press,
                col = data['col'],
                row = data['row'],
                span = data['span'],
                font = main_font)

        # math buttons
        for operator, data in MATH_POSITIONS.items():
            if data['image path']:
                divide_image = ctk.CTkImage(
                    light_image = Image.open(data['image path']['dark']),
                    dark_image = Image.open(data['image path']['light']))
                MathImageButton(
                    parent = self,
                    operator = operator,
                    func = self.math_press,
                    col = data['col'],
                    row = data['row'],
                    image = divide_image)
            else:
                MathButton(
                parent = self,
                text = data['character'],
                operator = operator,
                func = self.math_press,
                col = data['col'],
                row = data['row'],
                font = main_font)
    
    def change_font_size(self, event):
        '''Decrease result font size so more numbers are visible'''
        if event.width > 370:
            self.font_size -= 2
            self.result_label.configure(font = ctk.CTkFont(FONT, self.font_size))

    def num_press(self, value):
        '''Add pressed number to the label'''
        if self.zero_div:
            self.clear()
            self.zero_div = False

        if len(self.display_nums) < 16:
                
            if self.is_result:
                self.display_nums.clear()
                self.formula_string.set('')
                self.is_result = False

            self.display_nums.append(str(value))
            full_number = ''.join(self.display_nums)
            self.result_string.set(full_number)

    def math_press(self, value):
        '''Execute the pressed operator (+, -, /, *, =)'''
        
        current_number = ''.join(self.display_nums)

        if current_number:
            self.full_operation.append(current_number)

            if value != '=':
                # update data
                self.full_operation.append(value)
                self.display_nums.clear()
                self.is_result = False

                # update output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operation))
            
            else:   # value == '='
                try:
                    formula = ' '.join(self.full_operation)
                    result = eval(formula)
                    
                    # format the result
                    if isinstance(result, float):

                        if result.is_integer():
                            result = int(result)
                        else:
                            result = round(result, 3)

                    # update data
                    self.full_operation.clear()  
                    self.display_nums= [str(result)]
                    self.is_result = True

                    # update output
                    self.result_string.set(result)
                    self.formula_string.set(formula)

                except ZeroDivisionError:
                    self.zero_div = True
                    self.clear()
                                           
    def clear(self):
        '''Restart and clear the screen'''
        # clear the output
        if self.zero_div:
            self.result_string.set('Cannot divide by Zero') 
        else:
            self.result_string.set(0)

        self.formula_string.set('')

        # clear the data
        self.display_nums.clear()
        self.full_operation.clear()
        
        # reset data
        self.font_size = 70
        self.result_label.configure(font = ctk.CTkFont(FONT, OUTPUT_FONT_SIZE))

    def percent(self):
        '''Divide the current value by 100'''

        if self.display_nums:
            # get the percent number
            current_number = float(''.join(self.display_nums))
            percent_number = current_number / 100

            # update the data and the output
            self.display_nums = list(str(percent_number))
            self.result_string.set(''.join(self.display_nums))

    def invert(self):
        '''Invert the current value sign'''

        current_number = ''.join(self.display_nums)
        if current_number:
            # check + or -
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                if self.display_nums[0] != '-':
                   self.display_nums[0] = self.display_nums[0][1:]
                else:                    
                    del self.display_nums[0]
            
            self.result_string.set(''.join(self.display_nums))

    def title_bar_color(self, is_dark):
        '''Change the Title Bar Color.
        Works for Windows 11 only'''

        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_BAR_HEX_COLORS['dark'] if is_dark else TITLE_BAR_HEX_COLORS['light']
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            pass

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master = parent, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)

if __name__ == "__main__":
    Calculator(darkdetect.isDark())