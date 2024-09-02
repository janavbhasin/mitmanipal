package com.course.structure;
import java.util.*;
public class School extends Building
{
    int clr,grade;
    public School()
    {
        super();
        clr=0;
        grade=0;
    }
    public void assign()
    {
        super.assign();
        System.out.println("enter grade:");
        grade=Sc.nextInt();
        System.out.println("enter classrooms:");
        clr=Sc.nextInt();
    }
    public void display()
    {
        super.display();
        System.out.println("grade:"+grade);
        System.out.println("classrooms:"+clr);
    }
}