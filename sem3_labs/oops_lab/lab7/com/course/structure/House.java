package com.course.structure;
import java.util.*;
public class House extends Building
{
    int beds,baths;
    public House()
    {
        super();
        beds=0;
        baths=0;
    }
    public void assign()
    {
        super.assign();
        System.out.println("enter baths:");
        baths=Sc.nextInt();
        System.out.println("enter beds:");
        beds=Sc.nextInt();
    }
    public void display()
    {
        super.display();
        System.out.println("baths:"+baths);
        System.out.println("beds:"+beds);
    }
}