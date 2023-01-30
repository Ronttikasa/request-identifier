class RequestIdentifier:
    """Class responsible for identifying and validating a request URI
    """
    
    def __init__(self):
        self._allowed_paths = ["login", "confirm", "sign"]
        self._scheme = "visma-identity"
        self._uri = ""
        self._uri_parts = []
        self._path = ""
        self._parameters = {}
        self._error_msg = ""

    def _parse_uri(self):
        """Build a list of keywords in the URI: scheme, path and parameters.

        Returns:
            False if input is not a string, otherwise True
        """
        if not type(self._uri) == str:
            return False
          
        part = ""
        for char in self._uri:
            if char in "/:?&":
                self._uri_parts.append(part)
                part = ""
                continue
            part += char
        self._uri_parts.append(part)

        self._uri_parts = [part for part in self._uri_parts if part]
        return True

    def _validate_scheme(self):
        """Validates that uri scheme is correct.
        
        Returns:
            True if scheme is correct, False if not.
        """

        if self._uri.startswith(self._scheme):
            return True
        return False

    def _validate_path(self):
        """Validate that uri path is allowed.
        
        Returns:
            Value of path if path is allowed, None if not.
        """

        path = self._uri_parts[1]

        if path in self._allowed_paths:
            self._path = path
            return path
        return None

    def _validate_parameters(self):
        """Check the validity of parameters of the request.

        Returns:
            True if parameters meet the criteria, False if not.
        """
        for part in self._uri_parts:
            if part in self._allowed_paths or part == self._scheme:
                continue
            part = part.split("=")
            self._parameters[part[0]] = part[1]

        if not "source" in self._parameters.keys():
            return False
        if not any(char.isalpha() for char in self._parameters["source"]):
            return False

        if self._path == "login":
            if not len(self._parameters) == 1:
                return False

        if self._path == "confirm":
            if not len(self._parameters) == 2:
                return False
            if not "paymentnumber" in self._parameters.keys():
                return False
            if not self._parameters["paymentnumber"].isdigit():
                return False

        if self._path == "sign":
            if not len(self._parameters) == 2:
                return False
            if not "documentid" in self._parameters.keys():
                return False
            if not any(char.isalpha() for char in self._parameters["documentid"]):
                return False

        return True         

    def identify(self, uri):
        """Identify the path and parameters of a request URI.

        Args:
            uri (str): The request URI to be identified

        Returns:
            tuple: Request path (str), request parameters (dict), error message (str)
        """
        self._uri = uri
        if not self._parse_uri():
            self._error_msg = "Input must be a String"
        if not self._validate_scheme():
            self._error_msg = "Incorrect scheme"
        if not self._validate_path():
            self._error_msg = "Incorrect path"
        if not self._validate_parameters():
            self._error_msg = "Incorrect parameters"
        return self._path, self._parameters, self._error_msg


        
        