package com.java.Examples;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;
import java.util.function.BiFunction;

public class ColletionAPI {

	public enum et {
		k1, k2, k3

	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Map<String, String> map = new HashMap<String, String>();

		map.put("key1", "100");
		map.put("key2", "200");
		map.put("key3", "300");

		Iterator itr = map.entrySet().iterator();

		System.out.println("Keys from Map");
		while (itr.hasNext()) {
			Map.Entry<String, String> e = (Entry<String, String>) itr.next();
			String key = e.getKey();

			System.out.print(" "+map.get(key));

		}
		
		
		  Set<Map.Entry<String, String>> entrySet  =map.entrySet();
		  Set<Map.Entry<String, String>> entrySet1  =map.entrySet();

		  
		  for (Entry entry : entrySet) {
			   System.out.println("------------------------------------------------");
			   System.out.println("looping HashMap in Java using EntrySet and java5 for loop");
			   System.out.println("key: " + entry.getKey() + " value: " + entry.getValue());
			}
		  
		 Iterator  setItr = entrySet1.iterator();
		 

		 System.out.println("Using iterator method");
		 while(setItr.hasNext()){
			 
		   Map.Entry<String, String>  item=(Entry<String, String>) setItr.next();	 
		   System.out.println(item.getKey()+ "" +item.getValue()); 
	 
		 }
	
		  map.merge("4", "33",new BiFunction<String, String, String>() {
			public String apply(String k, String v) {
				return v + 1;
			}
		});
		  
		  
		 System.out.println(map.toString());
		 
		 
		 Map<String, Integer> fruitCounts = new HashMap<String, Integer>();
		    List<String> fruitBasket = Arrays.asList("Apple", "Banana", "Apple", "Orange", "Mango", "Orange", "Mango", "Mango");
		    for (String fruit : fruitBasket) {
		        fruitCounts.merge(fruit, 1, (k, v) -> k + v);
		    }
		    System.out.println(fruitCounts);
		
	}

}
