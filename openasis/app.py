import sys
from kivy.utils import platform

def main():
    if len(sys.argv) > 1:
        import openasis.cli.cli as cli
        cli.main()
    else:
        if platform == 'android' or platform == 'ios':
            import openasis.mobile.mobile as mobile
            mobile.OpenasisApp().run()
        else:
            import openasis.desktop.desktop as desktop
            desktop.main()