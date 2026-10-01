import sys
from rolvio.core.exceptions import LifecycleError
from rolvio.core.config import get_settings
from rolvio.core.lifecycle import validate_python_version

def test_settings_initialization():
    """Verify that settings correctly load and application paths are created."""
    settings = get_settings()
    assert settings.paths.data_dir.exists()
    assert settings.paths.config_dir.exists()
    assert settings.paths.log_dir.exists()
    assert settings.env == "development"

def test_python_version_validator():
    """Verify python version validation runs without error on the required version."""
    major, minor = sys.version_info[:2]
    
    # In CI/Testing context, if it happens to run on 3.13, it should pass.
    if major == 3 and minor == 13:
        validate_python_version()
