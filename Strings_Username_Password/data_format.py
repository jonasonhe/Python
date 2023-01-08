#Jonason He 

def get_book_info (title = None, isbn = None, last_name = None, publisher = None, year_published = None, price = None):
    '''
    If the optional parameters are None, the function asks the user to enter the following information:
    
    params: book title, book isbn, authuor's last name, publisher's name, year published, and price
    returns: a string of all the inputs seperated by a "/"
    '''
    if title == None or isbn == None or last_name == None or publisher == None or year_published == None or price == None:
        #check title strip
        while True:
            title = input("Please enter your book's title: ")
            if title.find("/") != -1:
                title_error = '''Error - title cannot contain the character "/"'''
                print(title_error)
                continue
            else:
                break
        
        #check ISBN strip
        while True: 
            isbn = input("Please enter an ISBN: ")
            if isbn.isdigit() == False:
                isbn_error = "Error - ISBN can only contain numbers"
                print(isbn_error)
                continue
            else:
                break
          
        #check last name strip
        while True: 
            last_name = input("Please enter the author's last name: ")
            if last_name.find("/") != -1:
                last_name_error = '''Error - Author's name cannot contain the character "/"'''
                print(last_name_error)
                continue
            elif last_name.isdigit() == True: 
                last_name_error = "Error - author's last name cannot contain any numbers"
                print(last_name_error)
                continue
            else:
                break
        
        # check publisher strip
        while True: 
            publisher = input("Please enter the name of the publisher: ")
            if publisher.find("/") != -1: 
                publisher_error = '''Error - Publisher's name cannot contain the character "/"'''
                print(publisher_error)
                continue
            elif publisher.isdigit() == True: 
                publisher_error = "Error - Publisher's name cannot contain any numbers"
                print(publisher_error)
                continue
            else: 
                break
        
        # check year published 
        while True: 

            year_published = input("Please enter the year published: ")
            if year_published.isdigit() == False:
                year_published_error = "Error - the year published must be a number"
                print(year_published_error)
                continue
            elif len(year_published) < 4:
                year_published_error = "Error - year must be a 4 digit number (i.e. 2022)"
                print(year_published_error)
            else: 
                year_published = int(year_published)
                break
            

        # check price
        while True: 
            try: 
                price = float(input("Enter the book price: "))
                if price <= 0:
                    price_error = "Error - price has to be greater than 0"
                    print(price_error)
                    continue
                break
            except: 
                print("Error - price has to be a number")
                continue
    

    #formatting
    title_output = title.strip()
    isbn_output = str(isbn)
    last_name_output = last_name.strip()
    publisher_output = publisher.strip()
    year_published_output = str(year_published)
    price_output = "%.2f" % price
    

    # Build output string
    output = "/".join([title_output, isbn_output, last_name_output,publisher_output, year_published_output, price_output])
    print(output)
    return output


def convert_to_csv_format(book_info = None):
    '''
    Convert Book info to CSV format
    Ask user for Book info if missing
    
    param: book_info()
    return: book_info in csv format or data error
    '''
    # Check if book_info id missing and ask user to enter
    if book_info == None:
        book_info = get_book_info()
    # Check if book_info has correct number of "/" within the string
    if book_info.count("/") != 5:
        return "Data Error - book info data NOT complete!"
    # Loop till all "/" are gone
    while book_info.find("/") != -1:
        # Get index of the first "/"
        pos = book_info.find("/")
        # Remove "/" and replace with ","
        book_info = f"{book_info[:pos]},{book_info[pos+1:]}"
        print(book_info)
    return book_info

def convert_to_json_format(csv_data = None):
    '''
    Convert CSV data to JSON format
    Ask user for book info if missing
    
    param: book_info()
    return: book_info in json format or data error
    '''
    # Check if data is missing and ask user to enter
    if csv_data == None:
        csv_data = convert_to_csv_format()
    # Check if csv data has correct number of "," within the string
    if csv_data.count(",") != 5:
        return "Data Error - csv data NOT complete!"
    # Create list, for each of the data
    json_data = []
    # Loop till all "," are removed
    while csv_data.find(",") != -1:
        # Find the index of ","
        pos = csv_data.find(",")
        # Add data to list
        json_data.append(csv_data[:pos])
        # Remove "," all before it
        csv_data = csv_data[pos+1:]
    # Add the last of data to list
    json_data.append(csv_data)
    # Create string for all json data
    json_format = f'{{"book_title":"{json_data[0]}",' \
                  f'"book_isbn":"{json_data[1]}",' \
                  f'"book_author":"{json_data[2]}",' \
                  f'"book_publisher":"{json_data[3]}",' \
                  f'"year_published":"{json_data[4]}",' \
                  f'"book_price":"{json_data[5]}"}}'
    print(json_format)
    return json_format



