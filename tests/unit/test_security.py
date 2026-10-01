from rolvio.security.redaction import redact_sensitive_data
from rolvio.security.credential_store import WindowsCredentialStore
from unittest.mock import patch

def test_log_redaction():
    event_dict = {
        "event": "User logged in",
        "username": "test@example.com",
        "password": "super_secret_password",
        "auth_key": "12345-abcde",
        "safe_token_id": "999"
    }
    
    redacted = redact_sensitive_data(None, "info", event_dict.copy())
    
    assert redacted["event"] == "User logged in"
    assert redacted["username"] == "test@example.com"
    assert redacted["password"] == "*** REDACTED ***"
    assert redacted["auth_key"] == "*** REDACTED ***"
    assert redacted["safe_token_id"] == "*** REDACTED ***"

@patch('rolvio.security.credential_store.keyring')
def test_windows_credential_store(mock_keyring):
    store = WindowsCredentialStore()
    
    # Test setting secret
    store.set_secret("Rolvio", "test_user", "my_secret")
    mock_keyring.set_password.assert_called_with("Rolvio", "test_user", "my_secret")
    
    # Test getting secret
    mock_keyring.get_password.return_value = "my_secret"
    val = store.get_secret("Rolvio", "test_user")
    assert val == "my_secret"
    mock_keyring.get_password.assert_called_with("Rolvio", "test_user")
    
    # Test deleting secret
    store.delete_secret("Rolvio", "test_user")
    mock_keyring.delete_password.assert_called_with("Rolvio", "test_user")
