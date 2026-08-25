class contextosimples:
    def __enter__(self):
        print("estou no enter")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("estou no exit")

with contextosimples() as cs:
    print("Estou no with")