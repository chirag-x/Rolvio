"""Rolvio sensitive data redaction."""
from typing import Any, MutableMapping

SENSITIVE_KEY_FRAGMENTS = {
    "password",
    "secret",
    "token",
    "auth_key",
    "api_key",
    "credential"
}

def redact_sensitive_data(logger: Any, method_name: str, event_dict: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
    """Structlog processor to redact sensitive keys in logs."""
    for key, value in list(event_dict.items()):
        key_lower = key.lower()
        if any(fragment in key_lower for fragment in SENSITIVE_KEY_FRAGMENTS):
            event_dict[key] = "*** REDACTED ***"
    return event_dict
