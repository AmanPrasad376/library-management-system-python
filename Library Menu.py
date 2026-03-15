book_records = []
member_records = []


def add_books():
    book_name = input('Enter the name of the book you want to add: ')
    book_price = eval(input('Enter the price of the book: '))
    book_name.strip()

    if book_name not in book_records:
        book_records.append(book_name)
        book_records.append(book_price)
        print('{} Successfully Added!!!'.format(book_name))
        with open('books.txt', 'a') as f:
            f.write(book_name + '\t' + str(book_price) + '\n')
    else:
        print('{} is already present!!!'.format(book_name))
    print('List of books are {}'.format(book_records))


def add_member():
    while True:
        individual_records = []
        member_name = input('Enter your name: ')
        member_age = int(input('Enter age: '))
        while True:
            member_gender = input('Enter "M" for Male or "F" for female or "O" for other: ')
            if member_gender == 'M' or member_gender == 'F' or member_gender == 'O':
                break
            else:
                print('Invalid Input!!!')
                continue
        while True:
            member_mobile_number = int(input('Enter your phone number: '))
            if len(str(member_mobile_number)) != 10:
                print('Invalid Mobile Number!!')
                print('Enter again!!')
                continue
            else:
                break
        member_address = input('Enter your complete and permanent address: ')
        while True:
            member_marriage_status = input('Enter "M" for "Married" or "S" for "Single": ')
            if member_marriage_status == 'M' or member_marriage_status == 'S':
                break
            else:
                print('Invalid Input!!!')
                continue
        member_spouse_name = input('Enter the name of your partner: ')
        member_identification_mark1 = input('Enter 1st Identification mark: ')
        member_identification_mark2 = input('Enter 2nd Identification mark: ')
        while True:
            member_aadhar_number = int(input('Enter a valid 12 digit aadhar number: '))
            if len(str(member_aadhar_number)) != 12:
                print('Invalid Aadhar Number!!!')
                print('Enter again!!')
                continue
            else:
                break
        member_name.strip()

        member_address.strip()
        member_spouse_name.strip()
        member_identification_mark1.strip()
        member_identification_mark2.strip()
        individual_records.append(member_name)
        individual_records.append(member_age)
        individual_records.append(member_gender)
        individual_records.append(member_mobile_number)
        individual_records.append(member_address)
        individual_records.append(member_marriage_status)
        individual_records.append(member_spouse_name)
        individual_records.append(member_identification_mark1)
        individual_records.append(member_identification_mark2)
        individual_records.append(member_aadhar_number)
        count = False
        for i in range(len(individual_records)):
            if len(member_records) != 0:
                if individual_records[i] != member_records[i][0]:
                    member_records.append(individual_records)
                    print('{} Successfully Added!!!'.format(member_name))
                    with open('members.txt', 'a') as f:
                        f.write(str(individual_records) + '\n')
                    break
            elif len(member_records) == 0:
                member_records.append(individual_records)
                print('{} Successfully Added!!!'.format(member_name))
                with open('members.txt', 'a') as f:
                    f.write(str(individual_records) + '\n')
                break
            else:
                count = True
                break
        if count:
            print('{} is already a member'.format(member_name))
            print('Please Enter again')
            individual_records.clear()
            continue
        else:
            break
    print('List and details of Member are: {}'.format(member_records))


def modify_book_information():
    book_name1 = input('Enter the name of the book to be modified: ')
    book_name2 = input('Enter the updated name of the book: ')
    book_name1.strip()
    book_name2.strip()
    if book_name1 in book_records or book_records == []:
        index = 0
        for i in range(len(book_records)):
            if book_records[i] == book_name1:
                index = i
                break
        book_records[index] = book_name2
        print('This book {} is successfully updated to {}'.format(book_name1, book_name2))
        print('The List of books after modification {}'.format(book_records))
    else:
        print('This {} book is not in the records!!!')


def modify_student_information():
    member_name1 = input('Enter the name of the member to be modified: ')
    member_name1.strip()
    for i in range(len(member_records)):
        for j in range(len(member_records[i])):
            if member_name1 == member_records[i][j]:
                member_records.remove(member_records[i])
                add_member()
                break
            else:
                print('Not in records!!!')
                break


def issue_book():
    number_of_books_to_be_issued = int(input('Enter the number of books you want to issue: '))
    if number_of_books_to_be_issued == 1:
        book_name1 = input('Enter the name of the book to be issued: ')
        if book_name1 in book_records:
            print(
                'Please fill up the details and then you will be granted for the following book {}'.format(book_name1))
            add_member()
            index_of_price_of_book = book_records.index(book_name1) + 1
            print('The price which you have to pay for the book is: {} inclusive of tax'.format(
                book_records[index_of_price_of_book] + 0.10))
            print('The book is successfully issued!!!')
        else:
            print('The Book is not in the records!!!')
    elif number_of_books_to_be_issued == 3:
        book_name1 = input('Enter the name of the book to be issued: ')
        book_name2 = input('Enter the name of the book to be issued: ')
        book_name3 = input('Enter the name of the book to be issued: ')
        if book_name1 in book_records and book_name2 in book_records and book_name3 in book_records:
            print('Please fill up the details and then you will be granted for the following books {} {} {}'.format(
                book_name1, book_name2, book_name3))
            add_member()
            print('The price which you have to pay for these books {} {} {} is: inclusive of tax'.format(book_name1,
                                                                                                         book_name2,
                                                                                                         book_name3,
                                                                                                         book_records.pop(
                                                                                                             book_records.index(
                                                                                                                 book_name1) + 1) + book_records.pop(
                                                                                                             book_records.index(
                                                                                                                 book_name2) + 1) + book_records.pop(
                                                                                                             book_records.index(
                                                                                                                 book_name3) + 1) + 0.10))
            print('The book is successfully issued!!!')
    elif number_of_books_to_be_issued == 5:
        book_name1 = input('Enter the name of the book to be issued: ')
        book_name2 = input('Enter the name of the book to be issued: ')
        book_name3 = input('Enter the name of the book to be issued: ')
        book_name4 = input('Enter the name of the book to be issued: ')
        book_name5 = input('Enter the name of the book to be issued: ')
        if book_name1 in book_records and book_name2 in book_records and book_name3 in book_records and book_name4 in book_records and book_name5 in book_records:
            print(
                'Please fill up the details and then you will be granted for the following books {} {} {} {} {}'.format(
                    book_name1, book_name2, book_name3, book_name4, book_name5))
            add_member()
            print(
                'The price which you have to pay for these books {} {} {} {} {} is: inclusive of tax'.format(book_name1,
                                                                                                             book_name2,
                                                                                                             book_name3,
                                                                                                             book_name4,
                                                                                                             book_name5,
                                                                                                             (
                                                                                                                     book_records.pop(
                                                                                                                         book_records.index(
                                                                                                                             book_name1) + 1) + book_records.pop(
                                                                                                                 book_records.index(
                                                                                                                     book_name2) + 1) + book_records.pop(
                                                                                                                 book_records.index(
                                                                                                                     book_name3) + 1) + book_records.pop(
                                                                                                                 book_records.index(
                                                                                                                     book_name4) + 1) + book_records.pop(
                                                                                                                 book_records.index(
                                                                                                                     book_name5) + 1) + 0.30) - 0.20))
            print('The book is successfully issued!!!')


def return_book():
    book_name1 = input('Enter the name of the book to be returned: ')
    member_name1 = input('Enter your name: ')
    if book_name1 not in book_records:
        book_records.append(book_name1)
        print('Thank you {} sir/mam for returning this {} book!!!'.format(member_name1, book_name1))
    else:
        print('The book is already in the records please enter a valid book name!!!')


def search_menu():
    print('{}. for Book'.format(1))
    print('{}. for Member'.format(2))
    option1 = int(input('Enter your choice: '))
    if option1 == 1:
        book_name1 = input('Enter the name of the book to be searched!!')
        for i in range(len(book_records)):
            if book_records[i] == book_name1:
                print('Book Found at positive index {} and at negative index {}'.format(i, i - len(book_records)))
                break
        else:
            print('No results found!!!')
    elif option1 == 2:
        member_name1 = input('Enter the name of the member to be searched: ')
        for i in range(len(member_records)):
            if member_records[i] == member_name1:
                print('Member Found at positive index {} and at negative index {}'.format(i, i - len(member_records)))
                break
        else:
            print('No results found!!!')
    else:
        print('Invalid choice!!!')


def report_menu():
    complain = input('Please enter your query: ')
    print('Sorry for the inconvenience!!!')
    option2 = int(input('Press {} to talk to our support team or press {} to issue a refund request!!'.format(1, 2)))
    if option2 == 1:
        print('This is the number of our executive available 24*7 {}'.format(9608500101))
    elif option2 == 2:
        book_name1 = input('Enter the name of the book')
        if book_name1 in book_records:
            print('Refund request successfully granted!!')
        else:
            print('No match found sorry cannot initiate refund!!')
    print('Thank you for your precious time hope you liked our services!!!')
    print("You'll receive a rating request post this conversation please do rate us!!!")


def special_menu():
    print('We have listed some offers for you!!')
    print("If you issue three books then you'll have to pay the tax of one only!!")
    print("If you issue five books then you'll get an instant discount of 20%!!")


def backup():
    while True:
        option1 = int(input('Enter 1 for book records and 2 for member records: '))
        if option1 == 1:
            try:
                with open('books.txt', 'r') as f:
                    print(f.read())
                    break
            except FileNotFoundError:
                print('First add some books!!')
                break
        elif option1 == 2:
            try:
                with open('members.txt', 'r') as f:
                    list = f.readlines()
                    for lines in list:
                        print(lines, end='')
                    break
            except FileNotFoundError:
                print('First add some members!!')
                break
        else:
            print('Invalid Re-enter!!')


print('LIBRARY MENU')
while True:
    print('{}.  Add Books'.format(1))
    print('{}.  Add Member'.format(2))
    print('{}.  Modify Book Information'.format(3))
    print('{}.  Modify Student Information'.format(4))
    print('{}.  Issue Book'.format(5))
    print('{}.  Return Book'.format(6))
    print('{}.  Search Menu'.format(7))
    print('{}.  Report Menu'.format(8))
    print('{}.  Special Menu'.format(9))
    print('{}. Close Application'.format(10))
    print('{}. To go to the Main Menu'.format(11))
    print('{}. To see the past records'.format(12))
    option = int(input('Enter your choice...: '))
    if option == 1:
        add_books()
    if option == 2:
        add_member()
    if option == 3:
        modify_book_information()
    if option == 4:
        modify_student_information()
    if option == 5:
        issue_book()
    if option == 6:
        return_book()
    if option == 7:
        search_menu()
    if option == 8:
        report_menu()
    if option == 9:
        special_menu()
    if option == 10:
        break
    if option == 11:
        continue
    if option == 12:
        backup()
