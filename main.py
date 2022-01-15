import os
import sys

if len(sys.argv) > 1:
    import openasis.cli
    openasis.cli.main()
else:
    import openasis.app
    openasis.app.OpenasisApp().run()
