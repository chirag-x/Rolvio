"""Rolvio secure credential storage abstraction."""
import keyring
import keyring.errors
from abc import ABC, abstractmethod
import structlog

logger = structlog.get_logger(__name__)

class CredentialStore(ABC):
    """Abstract interface for secure secret storage."""
    
    @abstractmethod
    def set_secret(self, service: str, account: str, secret: str) -> None:
        """Securely store a secret."""
        pass
    
    @abstractmethod
    def get_secret(self, service: str, account: str) -> str | None:
        """Retrieve a securely stored secret."""
        pass

    @abstractmethod
    def delete_secret(self, service: str, account: str) -> None:
        """Delete a securely stored secret."""
        pass

class WindowsCredentialStore(CredentialStore):
    """Windows Credential Manager implementation using keyring."""
    
    def set_secret(self, service: str, account: str, secret: str) -> None:
        logger.debug("Storing secret securely", service=service, account=account)
        keyring.set_password(service, account, secret)

    def get_secret(self, service: str, account: str) -> str | None:
        logger.debug("Retrieving secure secret", service=service, account=account)
        return keyring.get_password(service, account)
        
    def delete_secret(self, service: str, account: str) -> None:
        logger.debug("Deleting secure secret", service=service, account=account)
        try:
            keyring.delete_password(service, account)
        except keyring.errors.PasswordDeleteError:
            # If it doesn't exist, it's effectively deleted
            pass
