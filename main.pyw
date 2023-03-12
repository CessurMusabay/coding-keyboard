import customtkinter
import json
import pyautogui


class App:
    def load_keys(self):
        with open('./keys.json', 'r') as f:
            self.keys = json.load(f)

    def set_size(self):
        grid = int(len(self.keys) ** (1 / 2) // 1)
        self.grid = grid
        self.size = grid * self.button_size[0], grid * self.button_size[1]

    def initialize_app(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        app = customtkinter.CTk()
        app.iconbitmap("./images/keyboard.ico")
        app.title('Coding Keyboard')
        app.resizable(False, False)
        app.geometry(f'{self.size[0]}x{self.size[1]}')
        self.app = app

    def key_press(self, key):
        self.app.withdraw()
        pyautogui.typewrite(key)
        self.app.deiconify()

    def render_ui(self):
        for i in range(self.grid):
            for j in range(self.grid):
                key = self.keys[i * self.grid + j]
                button = customtkinter.CTkButton(
                    master=self.app,
                    text=key,
                    width=self.button_size[0],
                    height=self.button_size[1],
                    corner_radius=0,
                    command=lambda k=key: self.key_press(k),
                    font=self.font
                )
                button.grid(row=i, column=j)

    def __init__(self):
        self.keys = None
        self.size = None
        self.app = None
        self.grid = None
        self.initialized = False
        self.button_size = 50, 50

        self.load_keys()
        self.set_size()
        self.initialize_app()
        self.font = customtkinter.CTkFont(family='Roboto', size=30, weight='bold')
        self.render_ui()

    def run(self):
        self.app.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
