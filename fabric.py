import customtkinter as ctk
from typing import Callable, Optional


class ButtonFactory:
    def __init__(
        self,
        parent,
        *,
        height: int = 30,
        corner_radius: int = 14,
        fg_color: str = "#ffffff",
        hover_color: str = "#e9e9e9",
        text_color: str = "#0f2230",
        font: tuple = ("Segoe UI", 12, "bold"),
        pad_x: int = 18,
        pad_y: int = 6,
        fill: str = "x",
        expand: bool = False
    ):
        self.parent = parent
        self.style = dict(height=height, corner_radius=corner_radius,
                          fg_color=fg_color, hover_color=hover_color,
                          text_color=text_color, font=font)
        self.pack_opts = dict(padx=pad_x, pady=(pad_y, pad_y), fill=fill, expand=expand)

    def make(
        self,
        *,
        text: str,
        command: Callable,
        tooltip: Optional[str] = None,
        pack_overrides: Optional[dict] = None
    ) -> ctk.CTkButton:
        btn = ctk.CTkButton(self.parent, text=text, command=command, **self.style)
        opts = self.pack_opts.copy()
        if pack_overrides:
            opts.update(pack_overrides)
        btn.pack(**opts)
        if tooltip:
            _attach_simple_tooltip(self.parent, btn, tooltip)
        return btn

def _attach_simple_tooltip(parent, widget, text: str):
    tip = ctk.CTkToplevel(parent)
    tip.withdraw()
    tip.overrideredirect(True)
    tip.attributes("-topmost", True)
    lbl = ctk.CTkLabel(tip, text=text, padx=8, pady=6)
    lbl.pack()
    def enter(_):
        tip.deiconify()
        x = widget.winfo_rootx() + widget.winfo_width() + 6
        y = widget.winfo_rooty()
        tip.geometry(f"+{x}+{y}")
    def leave(_):
        tip.withdraw()
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)