import com.course.structure.Building;
import com.course.structure.House;
import com.course.structure.School;
import java.util.*;
class q1
{
    public static void main(String args[])
    {
        Scanner Sc= new Scanner(System.in);
        System.out.print("1. Building only\n2. House\n3. School ");
        int input = Sc.nextInt();
        if (input == 1) 
        {
            Building b = new Building();
            b.assign();
            b.display();
        }
        else if (input == 2) 
        {
            House h =  new House();
            h.assign();
            h.display();
        }
        else if (input == 3) 
        {
            School s = new School();
            s.assign();
            s.display();
        }
    }
}