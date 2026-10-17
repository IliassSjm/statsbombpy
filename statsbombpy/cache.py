import os
from tempfile import mkdtemp

from requests_cache import CachedSession

from statsbombpy.config import CACHED_CALLS_SECS

# Cache statsbombpy's own requests only. requests_cache.install_cache() would
# patch requests for the whole program that imports statsbombpy.
session = CachedSession(
    os.path.join(mkdtemp(), "statsbombpy"),
    backend="sqlite",
    expire_after=CACHED_CALLS_SECS,
)
