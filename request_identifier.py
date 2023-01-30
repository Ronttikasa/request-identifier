class RequestIdentifier:
    def __init__(self):
        self._uri = ""

    def _set_uri(self, uri):
        self._uri = uri

    def _validate_scheme(self):
        """Validates that uri scheme is correct.
        
        Returns True if scheme is correct, False if not."""

        if self._uri.startswith("visma-identity"):
            return True
        return False

    def _validate_path(self):
        """Validate that uri path is allowed.
        
        Returns path if path is allowed, None if not."""

        allowed_paths = ["login", "confirm", "sign"]
        uri_first_part = self._uri.split("?")[0]

        for path in allowed_paths:
            if uri_first_part.endswith(path):
                return path
        return None

    def identify(self, uri):
        self._set_uri(uri)
        if not self._validate_scheme():
            return("Incorrect scheme")
        if not self._validate_path():
            return("Incorrect path")
        return("Yay!")


        
        