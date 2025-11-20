class PrintableMixin:
    def print_info(self) -> None:
        print(f"Impression de {self.__class__.__name__} info :")
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")