# class Puppy:
#     n_puppies = 0
#     def __new__(cls):
#         if cls.n_puppies <= 9:
#             instance = object.__new__(cls)
#             cls.n_puppies += 1
#             return instance

class Puppy:
    n_puppies = 0

    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1