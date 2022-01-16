import sys

def main():
    if len(sys.argv) > 1:
        import openasis.cli.cli as cli
        cli.main()
    else:
        import openasis.desktop.desktop as desktop
        desktop.OpenasisApp().run()