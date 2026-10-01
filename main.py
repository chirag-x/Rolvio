"""Rolvio application entry point.

Implementation begins during PHASE_01_PROJECT_FOUNDATION.
"""
import sys
from pathlib import Path

# Ensure the 'src' directory is in the Python path so 'rolvio' can be found
src_path = Path(__file__).parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


def main() -> None:
    try:
        from rolvio.core.lifecycle import startup, shutdown
        from rolvio.ui.main_window import MainWindow
        
        app = startup()
        
        window = MainWindow()
        window.show()
        
        exit_code = app.exec()
        
        shutdown(app)
        sys.exit(exit_code)
        
    except Exception as e:
        print(f"Fatal application error during startup: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
