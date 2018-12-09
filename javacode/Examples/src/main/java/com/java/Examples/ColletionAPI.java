package com.java.Examples;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;

public class ColletionAPI {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	
	Map<String,String> map =new HashMap<String,String>();	
		
	map.put("key1", "100");
	map.put("key2", "200");
	map.put("key3", "300");
	
	
	Iterator itr = map.entrySet().iterator();
	
    while(itr.hasNext()){
    Map.Entry<String, String>  e=(Entry<String, String>) itr.next();
    String key= e.getKey();
    
     System.out.println("Value from the Map"+map.get(key));
    	
    	
    }
	
	
		
		
		
	}

}
