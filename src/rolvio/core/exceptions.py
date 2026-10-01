"""Rolvio core exception hierarchy."""

class RolvioError(Exception):
    """Base exception for all Rolvio errors."""
    pass

class ConfigurationError(RolvioError):
    """Raised when configuration is invalid or missing."""
    pass

class LifecycleError(RolvioError):
    """Raised when application startup/shutdown fails."""
    pass
