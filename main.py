import webview
webview.create_window("AuraOS Desktop", html=open("src/main.html", "r").read(), fullscreen=True)
webview.start()