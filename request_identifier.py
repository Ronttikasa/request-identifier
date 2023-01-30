class RequestIdentifier:
    def __init__(self):
        self._uri = ""

    def _validate_scheme(self):
        """Validates that uri scheme is correct.
        
        Returns True if scheme is correct, False if not."""

        if self._uri.startswith("visma-identity"):
            return True
        return False

    def _validate_path(self):
        """Validate that uri path is allowed.
        
        Returns True if path is allowed, False if not."""

        allowed_paths = ["login", "confirm", "sign"]
        uri_first_part = self._uri.split("?")[0]

        for path in allowed_paths:
            if uri_first_part.endswith(path):
                return True
        return False


        
        