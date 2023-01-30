from request_identifier import RequestIdentifier

class RequestClient:
    def __init__(self):
        self.identifier = RequestIdentifier()
    
    def ui(self):
        while True:
            uri = input("Input URI: ")
            if uri == "end":
                break
            print(self.identifier.identify(uri))

if __name__ == "__main__":
    client = RequestClient()
    client.ui()
            