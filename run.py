import mainUI_clash, gui_constants, os, signal, subprocess, time

if gui_constants.LAUNCH_CLIENT_TYPE == "clash":
    sub_clash = subprocess.Popen([
        gui_constants.CURRENT_PYTHON_INTERPRETER
        , "./mainUI_clash.py"
    ])

    # while sub_clash.poll() is None:
    #     print(123)
    #     time.sleep(0.8)

    sub_clash.wait()

else:
    print(3)


