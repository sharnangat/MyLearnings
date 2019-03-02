/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.mystreamexample;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.stream.Collector;
import java.util.stream.Stream;

/**
 *
 * @author Admin
 */
public class MyStream {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
  
        
     List<Book> bookList = createList();
     
        
        
        Book result=    bookList.stream().filter(p -> p.getBookNo().equals("10")).findAny().orElse(null);
       
        System.out.println("Boook  "+result);
        
        
    }

    private static List<Book> createList() {
        
        List<Book> list =new ArrayList();
        
        Book book1 =new Book();
        book1.setBookNo("10");
        book1.setBookName("Java");
        
        Book book2 =new Book();
        book2.setBookNo("11");
        book2.setBookName("Java 1");
        
        Book book3 =new Book();
        book3.setBookNo("12");
        book3.setBookName("Java 2");
        
        list.add(book1);
        list.add(book2);
        list.add(book3);
        
        
        
        return list;
    }
    
}
