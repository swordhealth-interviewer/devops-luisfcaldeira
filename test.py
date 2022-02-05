def read_in_chunks(file_object, chunk_size=1):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open("Actors.txt") as f:
    for piece in read_in_chunks(f):
        print(piece)
