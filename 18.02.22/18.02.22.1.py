class Reader:
    __books_list = ['Dostoevsky', 'Tolstoy', 'Pushkin', 'Turgenev', 'Lermontov']
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def take_book(self, kname):
        if kname in self.__books_list:
            if len(self.books) < 2:
                self.books.append(self.__books_list.pop(self.__books_list.index(kname)))
            else:
                print(f'больше для {self.name} книг взять нельзя')
        else:
            print(f'{kname} - такой книги нет')

    
ivan = Reader('ivan')
ivan.take_book('Dostoevsky')
ivan.take_book('Tolstoy')
ivan.take_book('нгш')
