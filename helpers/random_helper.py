from uuid import uuid4


def get_n_random_alphanumericals(n=10) -> str:
    return str(uuid4()).replace('-', '')[:n]
