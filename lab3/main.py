import tkinter as tk
import keyboard

class RasterizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Растровые алгоритмы")
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()
        for i in range(0, 600, 20):
            self.canvas.create_line(i, 0, i, 600, fill="lightgray")
            self.canvas.create_line(0, i, 600, i, fill="lightgray")
        self.draw_line_steps(50, 50, 200, 200, "yellow")
        self.draw_line_bresenham(50, 100, 200, 250, "green")
        self.draw_circle_bresenham(400, 150, 50, "red")
        keyboard.add_hotkey('+', self.zoom_in)
        keyboard.add_hotkey('-', self.zoom_out)
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonPress-1>", self.on_click)

    def draw_line_steps(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        x_increment = dx / steps
        y_increment = dy / steps
        x, y = x1, y1
        for _ in range(steps + 1):
            print(f"Line ({x}, {y})")
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color, outline="")
            x += x_increment
            y += y_increment

    def draw_line_bresenham(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        x, y = x1, y1
        d = 2 * dy - dx
        for _ in range(dx + 1):
            print(f"Bresenham ({x}, {y})")
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color, outline="")
            if d >= 0:
                y += 1
                d -= 2 * dx
            x += 1
            d += 2 * dy

    def draw_circle_bresenham(self, xc, yc, r, color):
        x = 0
        y = r
        d = 3 - 2 * r
        while x <= y:
            self.canvas.create_rectangle(xc + x, yc + y, xc + x + 2, yc + y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - x, yc + y, xc - x + 2, yc + y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + x, yc - y, xc + x + 2, yc - y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - x, yc - y, xc - x + 2, yc - y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + y, yc + x, xc + y + 2, yc + x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - y, yc + x, xc - y + 2, yc + x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + y, yc - x, xc + y + 2, yc - x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - y, yc - x, xc - y + 2, yc - x + 2, fill=color, outline="")
            x += 1
            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            self.canvas.create_rectangle(xc + x, yc + y, xc + x + 2, yc + y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - x, yc + y, xc - x + 2, yc + y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + x, yc - y, xc + x + 2, yc - y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - x, yc - y, xc - x + 2, yc - y + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + y, yc + x, xc + y + 2, yc + x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - y, yc + x, xc - y + 2, yc + x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc + y, yc - x, xc + y + 2, yc - x + 2, fill=color, outline="")
            self.canvas.create_rectangle(xc - y, yc - x, xc - y + 2, yc - x + 2, fill=color, outline="")

    def zoom_in(self):
        self.canvas.scale(tk.ALL, 300, 300, 1.25, 1.25)

    def zoom_out(self):
        self.canvas.scale(tk.ALL, 300, 300, 0.75, 0.75)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(tk.ALL, dx, dy)
        self.start_x = event.x
        self.start_y = event.y


if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizationApp(root)
    root.mainloop()