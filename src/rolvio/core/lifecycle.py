"""Rolvio application lifecycle management."""
import sys
import structlog
from PySide6.QtWidgets import QApplication
from rolvio.core.exceptions import LifecycleError
from rolvio.core.config import get_settings
from rolvio.observability.logging import configure_logging

logger = structlog.get_logger(__name__)

# Validate specifically for Python 3.13 as requested in PHASE_01 docs
REQUIRED_PYTHON_MAJOR = 3
REQUIRED_PYTHON_MINOR = 13

def validate_python_version():
    """Ensure we are running on Python 3.13.x"""
    major, minor = sys.version_info[:2]
    if major != REQUIRED_PYTHON_MAJOR or minor != REQUIRED_PYTHON_MINOR:
        raise LifecycleError(
            f"Unsupported Python version. Expected {REQUIRED_PYTHON_MAJOR}.{REQUIRED_PYTHON_MINOR}.x, "
            f"got {major}.{minor}.{sys.version_info.micro}"
        )

def startup() -> QApplication:
    """Initialize the application foundation."""
    validate_python_version()
    
    settings = get_settings()
    log_file = settings.paths.log_dir / "rolvio.log"
    configure_logging(log_file)
    
    logger.info("Starting Rolvio", env=settings.env, version="0.1.0")

    app = QApplication(sys.argv)
    app.setApplicationName("Rolvio")
    app.setOrganizationName("NORVI")
    return app

def shutdown(app: QApplication):
    """Gracefully shut down the application."""
    logger.info("Shutting down Rolvio")
    app.quit()
