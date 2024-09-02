package com.course.structure;
import java.util.*;
public class Building
{
    int sqf,stories;
    Scanner Sc = new Scanner(System.in);
    public Building()
    {
        sqf=0;
        stories=0;
    }
    public void assign()
    {
        System.out.println("enter sqf:");
        sqf=Sc.nextInt();
        System.out.println("enter stories:");
        stories=Sc.nextInt();
    }
    public void display()
    {
        System.out.println("sqf:"+sqf);
        System.out.println("stories:"+stories);
    }
}