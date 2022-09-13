
# import string


from typing import Union,List
from helpers import dostify

@dostify(errors=[])
def msg_box_info(msg_for_user:str):
    """Display a message box with an 'OK' button.

    Args:   
        msg_for_user (str): The message to display to the user.

    Examples:
        >>> msg_box_info('This is a demo message.')

    """
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    tk.messagebox.showinfo('PyBOTs', msg_for_user, parent=root)
    root.destroy()

