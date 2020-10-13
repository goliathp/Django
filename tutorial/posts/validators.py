import json
import urllib3


def GBooks(isbn):
    arr = []
    bookTitle = ''
    bookAuthor = ''
    publishedDate = ''
    http = urllib3.PoolManager()
    googleBooks = http.request(
        'GET', 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn)

    load = json.loads(googleBooks.data.decode('utf-8'))
    if load['totalItems'] >= 1:
        for each in load['items']:
            arr.append(each['volumeInfo'])
        for e in arr:
            bookTitle = (e['title'])
            bookAuthor = (e['authors'][0])
            publishedDate = (e['publishedDate'])
            # return bookTitle
            # print(bookTitle, bookAuthor, publishedDate)
            f = open("gbooks.txt", "w")
            f.write(bookTitle)
            f.write(',')
            f.write(bookAuthor)
            f.write(',')
            f.write(publishedDate)
            f.close()

        return True
    else:
        return False


# exec(open('tutorial/posts/views.py').read())

# GBooks("9781410406200")

# f = open("gbooks.txt", "r")
# details = (f.read()).split(",")
# print(details[0])
# print(bookTitle)
# print(bookAuthor)
