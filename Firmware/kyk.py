import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# Define your rows and columns directly
keyboard.row_pins = (board.GP4, board.GP3, board.GP2, board.GP1, board.GP0)
keyboard.col_pins = (board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# One single flat list for Layer 0
keyboard.keymap = [
    [
        # Row 1
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.HOME,
        # Row 2
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLASH, KC.DELETE,
        # Row 3
        KC.CAPSLOCK, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.END, KC.PGUP,
        # Row 4
        KC.LSHIFT, KC.NO, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.RSHIFT, KC.UP, KC.PGDOWN,
        # Row 5
        KC.LCTRL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RALT, KC.RGUI, KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT,
    ]
]

keyboard.go()
