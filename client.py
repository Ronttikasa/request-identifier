from request_identifier import RequestIdentifier

class RequestClient:
    def __init__(self):
        pass
    
    def ui(self):
        """Simple CLI for using the request identifier class
        """
        
        while True:
            uri = input("Input URI (type 'end' to exit): ")
            if uri == "end":
                break
            path, parameters, error_msg = RequestIdentifier().identify(uri)
            if error_msg:
                print(error_msg)
                continue
            print(f"path: {path}")
            for p in parameters:
                print(f"{p}: {parameters[p]}")

if __name__ == "__main__":
    client = RequestClient()
    client.ui()
            