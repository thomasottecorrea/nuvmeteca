import boto3
from app.models import Book, BookCreate
import uuid

class BookService:
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('Books')

    def create_book(self, book: BookCreate) -> Book:
        book_id = str(uuid.uuid4())
        item = Book(id=book_id, **book.dict()).dict()
        self.table.put_item(Item=item)
        return Book(**item)

    def get_book(self, book_id: str) -> Book:
        response = self.table.get_item(Key={'id': book_id})
        item = response.get('Item')
        if item:
            return Book(**item)
        return None

    def update_book(self, book_id: str, book: Book) -> Book:
        self.table.update_item(
            Key={'id': book_id},
            UpdateExpression="set title=:t, author=:a, category=:c, is_available=:i, borrower=:b, loan_date=:l, return_date=:r, wait_list=:w",
            ExpressionAttributeValues={
                ':t': book.title,
                ':a': book.author,
                ':c': book.category,
                ':i': book.is_available,
                ':b': book.borrower,
                ':l': book.loan_date,
                ':r': book.return_date,
                ':w': book.wait_list
            },
            ReturnValues="UPDATED_NEW"
        )
        return self.get_book(book_id)

    def list_books(self) -> list[Book]:
        response = self.table.scan()
        items = response.get('Items', [])
        return [Book(**item) for item in items]
