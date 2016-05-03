import sample_application
import sys
import traceback

try:
    app = sample_application.SampleApplication()
    app.run()
except ValueError as err:
    print(err, file=sys.stderr)
    sys.exit(1)
except Exception as err:
    print(err, file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(2)
