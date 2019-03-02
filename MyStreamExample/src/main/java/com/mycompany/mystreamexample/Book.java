/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mystreamexample;

/**
 *
 * @author Admin
 */
public class Book {
    
   private  String bookNo;
   
   private String BookName;

    public String getBookNo() {
        return bookNo;
    }

    public String getBookName() {
        return BookName;
    }

    public void setBookNo(String bookNo) {
        this.bookNo = bookNo;
    }

    public void setBookName(String BookName) {
        this.BookName = BookName;
    }

    @Override
    public String toString() {
        return "Book{" + "bookNo=" + bookNo + ", BookName=" + BookName + '}';
    }
   
   
   
   
   
    
    
}
