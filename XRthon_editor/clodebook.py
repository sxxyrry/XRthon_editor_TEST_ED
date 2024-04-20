import os
import liner
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import shutil
import custom
import config
from folders import folder
from text import Edition_logs
from XRthon_main import _XRthon_main_


class Notebook:
    def __init__(self, parent : tk.Tk):
        self.parent: tk.Tk = parent
        self.parent.bind("<{}-n>".format(config.Settings().bigkey), lambda event: self.add_info_page())
        # self.parent.bind("<{}-w>".format(config.Settings().bigkey), lambda event: self.close_page())
        self.book = custom.CustomNotebook(parent)
        self.book.pack(side="top", fill="both", expand=True)
        self.frames = []
        self.frame_id = -1
        self.i = 0
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".XRn", filetypes=[("XRthon Files", "*.XRn"),
                                                                                     ("Text Documents", "*.XRn")])
        if file_path:
            with open(file_path, 'r', encoding='UTF-8') as f:
                content = f.read()
            try:
                content = self.frames[self.frame_id][1].load_content(content)
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
                return
            _XRthon_main_.var['breakpoints'] = []
    
    def save_file(self):
        file_path = os.path.join(filedialog.asksaveasfilename(initialfile="XRthon File.XRn", defaultextension=".XRn",
                                                      filetypes=[("XRthon_Files", "*.XRn"), ("Text Documents", "*.XRn")]))
        if file_path:
            try:
                content = self.frames[self.frame_id][1].get_text()
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
                return
            with open(file_path, 'w', encoding='UTF-8') as f:
                f.write(content)

    def run_file(self):
        if self.frame_id != -1:
            try:
                content = self.frames[self.frame_id][1].get_text()
            except:
                self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")
                return
            temp_file_path = f"temp.XRn"
            with open(os.path.join(folder, './temp/', temp_file_path), 'w', encoding='UTF-8') as f:
                f.write(content)
            
            with open(os.path.join(folder, './temp/', temp_file_path), 'r', encoding='UTF-8') as f:
                _XRthon_main_.XRthon_file(f, os.path.join(str(str(folder) + '\\temp\\' + temp_file_path)))
    
    def start_command_line(self):
        os.startfile(os.path.join(folder, './command_line.py'))
    
    def choose_file_and_run(self):
        file_path = filedialog.askopenfilename(defaultextension=".XRn", filetypes=[("XRthon Files", "*.XRn"),
                                                                                     ("Text Documents", "*.XRn")])
        if file_path == '':
            return
        with open(os.path.join(file_path), 'r', encoding='UTF-8') as f:
            _XRthon_main_.XRthon_file(f, os.path.join(file_path))

    def toggle_breakpoint(self):
        try:
            line_number = self.frames[self.frame_id][1].get_lineno_at_cursor()
            _XRthon_main_.var['breakpoints'].append(line_number + 1)
            if line_number in self.frames[self.frame_id][1].breakpoints:
                self.frames[self.frame_id][1].remove_breakpoint(line_number)
            else:
                self.frames[self.frame_id][1].set_breakpoint(line_number)
        except:
            self.show_popup("Sorry, you're not in the editor. ", "ERROR--ERROR")

    def add_updater(self, frame, line):
        self.frame_id = self.frames.index([frame, line])
    
    def add_page_(self):
        menubar = tk.Menu(self.parent)
        file_menu = tk.Menu(menubar, tearoff=0)
        run_menu = tk.Menu(menubar, tearoff=0)
        open_and_run_meun = tk.Menu(menubar, tearoff=0)
        open_XRthon_editor_meun = tk.Menu(menubar, tearoff=0)
        start_command_line = tk.Menu(menubar, tearoff=0)

        start_command_line.add_command(label="Start Command Line", command=self.start_command_line)

        open_XRthon_editor_meun.add_command(label="Open XRthon editor", command=self.add_page)

        open_and_run_meun.add_command(label="Open File and Run", command=self.choose_file_and_run)

        run_menu.add_command(label="Run", command=self.run_file)
        file_menu.add_command(label="Open ", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Set Breakpoint (Where the cursor is)", command=self.toggle_breakpoint)

        menubar.add_cascade(label="Start Command Line", menu=start_command_line)
        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Run", menu=run_menu)
        menubar.add_cascade(label="Open XRthon editor", menu=open_XRthon_editor_meun)
        menubar.add_cascade(label="Choose File and Run", menu=open_and_run_meun)
        
        self.parent.config(menu=menubar)

    def add_page(self):
        if self.i == 0:
            frame = tk.Frame(self.parent)
            line = liner.Liner(frame)
            line.pack(fill="both", expand=True)
            self.frames.append([frame, line])
            # frame.bind('<Visibility>', lambda event: self.add_updater(frame, line))
            frame.bind('<Configure>', lambda event: self.add_updater(frame, line))
            self.book.add(frame, text="XRthon File")
            self.book.protect_tab(len(self.frames) - 1)
            self.frame_id = len(self.frames) - 1

            self.book.select(self.frame_id)
        else:
            frame = tk.Frame(self.parent)
            line = liner.Liner(frame)
            line.pack(fill="both", expand=True)
            self.frames.append([frame, line])
            # frame.bind('<Visibility>', lambda event: self.add_updater(frame, line))
            frame.bind('<Configure>', lambda event: self.add_updater(frame, line))
            self.book.add(frame, text=f"XRthon File {self.i}")
            self.frame_id = len(self.frames) - 1

            self.book.select()

        self.i += 1

    def add_info_page(self, text="Information", title="Information"):
        frame = tk.Frame(self.parent)
        
        info_label = tk.Label(frame, text=text, wraplength=400, justify=tk.LEFT)
        info_label.pack(fill="both", expand=True)

        self.frames.append([frame, info_label])
        self.book.add(frame, text=title)
        self.book.protect_tab(len(self.frames) - 1)
        self.frame_id = len(self.frames) - 1

        self.book.select(self.frame_id)
    
    def show_popup(self, message, title):
        messagebox.showinfo(title, message)

    def update(self):
        if self.parent.wm_state() == "iconic":
            pass
        if self.frame_id == -1:
            return
        if isinstance(self.frames[self.frame_id][1], liner.Liner) and not isinstance(self.frames[self.frame_id][1], tk.Label): 
            self.frames[self.frame_id][1].redraw()

class USE_():
    def __init__(self):
        self.Version = self.V()
    
    def V(self):
        E_L_T = ''.join(Edition_logs)
        E_L_T_L = E_L_T.split('\n')
        L_ = []
        for text in E_L_T_L:
            if 'V' and 'BETA' in text:
                L_.append(text)
        text_1 = L_[len(L_) - 1].split(' > ')
        text_2 = text_1[1].split(' V')
        Version = text_2[0]
        return Version

    def __INIT__(self):
        try:
            root = tk.Tk(className=' XRthon editor ')
            root.geometry('800x600')
            book = Notebook(root)
            book.add_info_page(f'''This is a text (XRthon code) editor that I wrote with my friend LoveProgramming
If you click on the XRthon File page, the content of the XRthon File page will be used when you click back
Run code in command line
We very thank you for using XRthon Editor !!
Version: {self.Version}''', 'Start Screen')
            book.add_page()
            book.add_page_()
            book.book.select(0)
            while True:
                root.update()
                book.update()
                try:
                    os.remove(os.path.join(folder, './temp/', 'temp.XRn'))
                    self.dels()
                except PermissionError:
                    pass
                except FileNotFoundError:
                    pass
        except tk.TclError:
            quit()

    def dels(self):
        pycache_1 = os.path.join(folder, './__pycache__')
        pycache_2 = os.path.join(folder, './custom/__pycache__')
        if os.path.exists(pycache_1) and os.path.exists(pycache_2):
            shutil.rmtree(pycache_1)
            shutil.rmtree(pycache_2)

Use = USE_()
Use.dels()

if __name__ == "__main__":
    Use.dels()
    Use.__INIT__()
