"""Rolvio observability and logging foundation."""
import logging
import structlog
from pathlib import Path
from rolvio.security.redaction import redact_sensitive_data

def configure_logging(log_file_path: Path) -> None:
    """Configure structlog to output to console and file."""
    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Configure standard logging to route through structlog
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file_path, encoding='utf-8')
        ]
    )
    
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            redact_sensitive_data,
            structlog.dev.ConsoleRenderer(colors=False)
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
