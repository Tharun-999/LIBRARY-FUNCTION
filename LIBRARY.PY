class library(object):

    def __init__(self, totalbooks):

        self.totalbooks = totalbooks

    def total_books(self, totalbooks):
        print(f"Total Books in the Library :- {self.totalbooks}")

        return self.totalbooks

    def search(self, totalbooks, need_book):

        if need_book in totalbooks:
            print(f"The book is presented :- {need_book}")
        else:
            print(f"the book({need_book}) which you are searching for, not in library")

    def reserve(self, totalbooks, reserve_book = None):

        reserve_ = []

        if reserve_book in totalbooks:

            reserve_.append(reserve_book)
            totalbooks.remove(reserve_book)

            print(f"The book you have reserved is *************{reserve_book}")
            print(f"The books present in the library is **********{totalbooks}")

        else:
            print(f"The book(****{reserve_book}****) which for you are trying to reserve is not in list")

        return reserve_, totalbooks


    def return_book(self, totalbooks, return_, reserve_):

        if return_ not in totalbooks:

            totalbooks.append(return_)

            if len(reserved) > 0 and return_ not in totalbooks == False:
                reserved.remove(return_)
            else:
                pass
            
            print(f"total number of books present in the is *******{totalbooks}")
            print(f"total book you have returned is *********{return_}")

        else:

            print(f"The book you are to return is already in *******{totalbooks}")

if __name__ == "__main__":

    totalbooks = ["book1", "book2", "book3", "book4"]
    print(totalbooks)

    cla = library((totalbooks))

    print("1.Total_books\n2.Search\n3.reserve and return")

    choice = int(input("What do you need from top categories :-"))
    
    if choice == 1:
        cla1 = cla.total_books(totalbooks)
        print(cla1)
        
    elif choice == 2:
        search_ = input("which book need to search :-")
        cla.search(totalbooks, str(search_))
        
    elif choice == 3:
        reserve = input("enter which book you need to reserve form top list :-")
        reserved, total_boo = cla.reserve(totalbooks, reserve_book = str(reserve))
        print(reserved, total_boo)
        
        returning = input("which you need to return to library :-")
        cla.return_book(total_boo, returning, reserved)

    else:
        print(f"sorry worng input {choice}")
        
