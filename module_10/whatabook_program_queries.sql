/*
    Title: whatabook_program_queries.sql
    Author: Camille Carter
    Date: 12 February 2023
    Description: WhatABook program queries
*/

/*
    Select query to view a user's wishlist items 
*/
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 1;

/*
    Select query to view the store's location 
*/
SELECT store_id, locale from store;

/*
    Select query to view a full listing of the books WhatABook offers
*/
SELECT book_id, book_name, author, details from book;

/*
    Select query to view a listing of books not already in your user's wishlist.
    The user_id will need to be replaced with the actual values the user selects 
    from the program.
*/
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/*
    Insert statement to add a new book to a user's wishlist. 
    The values will need to be replaced with the actual values 
    the user selects from the program.
*/
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9);

/*
    Remove a book from the user's wishlist.
    The user_id and book_id values will need to be replaced 
    with the actual values the user selects from program.
*/
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;