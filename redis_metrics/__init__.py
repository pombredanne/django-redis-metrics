__version__ = "0.8.1"

try:
    from .utils import gauge, metric, set_metric  # NOQA
except ImportError:  # pragma: no cover
    pass  # pragma: no cover
