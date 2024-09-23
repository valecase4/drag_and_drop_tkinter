from tkinter import *

class App(Tk):
    """
    Application
    """

    def __init__(self) -> None:
        super().__init__()

        self.title("Drag and Drop")
        self.geometry("400x400+100+100")
        self.resizable(False, False)

        self.widget = Frame(self, width=100, height=100, background="red", cursor="hand2")
        self.widget.place(x=0, y=0)

        self.start_x = 0
        self.start_y = 0

        self.widget.bind("<Button-1>", lambda e : self.on_start(e))
        self.widget.bind("<B1-Motion>", lambda e : self.on_drag(e))
    
    def on_start(self, event) -> None:
        """
        On start dragging
        """

        self.start_x = event.x
        self.start_y = event.y

        print("\n")
        print(f"Widget: x = {self.widget.winfo_x()}; y = {self.widget.winfo_y()}")
        print(self.start_x, self.start_y)
        print(f"Event: x = {event.x}; y = {event.y}")
        print("\n")

    def on_drag(self, event) -> None:
        """
        On dragging
        """

        x = self.widget.winfo_x() + event.x - self.start_x
        y = self.widget.winfo_y() + event.y - self.start_y

        print("\n")
        print(f"Widget: x = {self.widget.winfo_x()}; y = {self.widget.winfo_y()}")
        print(f"Event: x = {event.x}; y = {event.y}")
        print("\n")
        print(f"New x={x}; y={y}")

        self.widget.place(x=x, y=y)

if __name__ == '__main__':
    app = App()
    app.mainloop()