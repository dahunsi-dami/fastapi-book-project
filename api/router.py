from fastapi import APIRouter, HTTPException  #import HTTPException to set status codes
from api.db.schemas import Book, InMemoryDB  #gets book model & InMemoryDB from schemas.py
from typing import Dict, Any  # for the response_model specification

from api.routes import books

db = InMemoryDB()  # to initialize the inmemory database

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])

@api_router.get("/books/{book_id}", response_model=Dict[str, Any])
async def get_book(book_id: int):
    """
    This endpoint gets a book with its ID.

    Args:
        book_id (int): this is the ID of the book to be retrieved.

    Returns:
        dict: as stated in the reponse_model above, this endpoint
        returns a dictionary object containing the book details.

    Raises:
        HTTPException: 404 Not Found if book isn't found.
    """
    book = db.get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book
