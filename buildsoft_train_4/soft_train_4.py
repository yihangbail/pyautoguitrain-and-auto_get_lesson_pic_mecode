import pyautogui as pi
import tkinter as tk
from tkinter import font as tkfont

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标位置监视器")
        self.root.geometry("300x120")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # 设置字体
        custom_font = tkfont.Font(family="Consolas", size=12)

        # 标签显示鼠标位置
        self.label = tk.Label(
            root,
            text="等待鼠标移动...",
            font=custom_font,
            bg="#f0f0f0",
            fg="#333",
            anchor="center"
        )
        self.label.pack(pady=20, padx=10, fill=tk.X)

        # 初始化上一次的位置
        self.last_x, self.last_y = pi.position()

        # 启动定时检测
        self.update_position()

    def update_position(self):
        x, y = pi.position()
        if x != self.last_x or y != self.last_y:
            self.label.config(text=f"鼠标位置: {x}, {y}")
            self.last_x, self.last_y = x, y
        # 每 100ms 检查一次，避免过快占用资源
        self.root.after(100, self.update_position)

    def on_closing(self):
        self.root.quit()

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = MouseTrackerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)  # 处理关闭事件
    root.mainloop()

#终端运行，生成.exe文件（pyinstaller --onefile --windowed --icon=app.ico mouse_tracker.py）