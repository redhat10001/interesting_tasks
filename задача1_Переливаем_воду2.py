print()
'''
Требуется перелить воду из кувшина в чашку. объемы кувшина и чашки не меняются.
'''
# import sys


class Conteiner:
    def __init__(
        self, name: str, volume: int, current_volume: int, pour_out: int = 100
    ) -> None:
        self.__name = name
        self.__volume = volume
        self.current_volume = current_volume
        self.pour_out = pour_out

    # Метод принимает значение сколько
    # мы выливаем воды из сосуда
    def pour_out_liquid(self) -> int:
        if self.current_volume > 0:
            self.current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f'{self.__name} пустой')
            return 0

    # Метод принимает значение сколько
    # мы вливаем воды в чашку
    def pour_liquid(self, volume: int) -> None:
        if self.current_volume + volume <= self.__volume:
            self.current_volume += volume
        else:
            print(f'{self.__name} полна')
            # exit()

    # Метод передачи информации
    def info(self):
        print(f'{self.__name} = {self.current_volume}')


def main() -> None:
    kuvshin = Conteiner(name='kuvshin', volume=1000, current_volume=1000)
    chashka = Conteiner(name='chashka', volume=200, current_volume=0, pour_out=50)
    i = 0
    while i < 15:
        kuvshin.info()
        chashka.info()
        chashka.pour_liquid(kuvshin.pour_out_liquid())
        i += 1


if __name__ == '__main__':
    main()
