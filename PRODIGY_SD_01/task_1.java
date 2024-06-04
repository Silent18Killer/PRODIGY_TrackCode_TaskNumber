/*
    Create a program that converts temperatures between Celsius, Fahrenheit, 
    and Kelvin scales. The program should prompt the user to input a temperature 
    value and the original unit of measurement. It tre should then convert the 
    temperature to the other two units and display am the converted values to the user. 
    For example, if the user enters a temperature of 25 degrees Celsius, the program 
    should convert it to Fahrenheit and Kelvin, and present the converted values as outputs.
*/

import java.util.*;

class Demo
{
    public static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) 
    {
        System.out.println("1. Celsius to Fahrenheit\n2. Celsius to Kelvin\n" +
                "3. Fahrenheit to Celsius\n4. Fahrenheit to Kelvin\n" +
                "5. Kelvin to Celsius\n6. Kelvin to Fahrenheit\n7. Exit");

        while(true) 
        {
            System.out.print("\nEnter your Choice: ");
            int ch = sc.nextInt();
            double num;


            switch (ch) 
            {
                case 1:
                    System.out.print("Enter Celsius value: ");
                    num = sc.nextDouble();
                    System.out.printf("Fahrenheit" + " value: %.2f%n", C_F(num));
                    break;
                case 2:
                    System.out.print("Enter Celsius value: ");
                    num = sc.nextDouble();
                    System.out.printf("Kelvin" + " value: %.2f%n", C_K(num));
                    break;
                case 3:
                    System.out.print("Enter Fahrenheit value: ");
                    num = sc.nextDouble();
                    System.out.printf("Celsius" + " value: %.2f%n", F_C(num));
                    break;
                case 4:
                    System.out.print("Enter Fahrenheit value: ");
                    num = sc.nextDouble();
                    System.out.printf("Kelvin" + " value: %.2f%n", F_K(num));
                    break;
                case 5:
                    System.out.print("Enter Kelvin value: ");
                    num = sc.nextDouble();
                    System.out.printf("Celsius" + " value: %.2f%n", K_C(num));
                    break;
                case 6:
                    System.out.print("Enter Kelvin value: ");
                    num = sc.nextDouble();
                    System.out.printf("Fahrenheit" + " value: %.2f%n", K_F(num));
                    break;
                case 7:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid Input");
            }



            System.out.print("Do you want again (yes/no) ? ");
            String str = sc.next();

            if(str.equals("no"))
            {
                break;
            }
            else if(str.equals("yes"))
            {
                continue;
            }
            else
            {
                System.out.println("Invalid! Exiting..");
                break;
            }
        }
    }


    public static double C_F(double C) {
        return (C * (9/5)) + 32;
    }

    public static double C_K(double C) {
        return C + 273.15f;
    }

    public static double F_C(double F) {
        return (F - 32) * 5/9;
    }

    public static double F_K(double F) {
        return (F - 32) * 5/9 + 273.15;
    }

    public static double K_C(double K) {
        return K - 273.15;
    }

    public static double K_F(double K) {
        return (K - 273.15) * 9/5 + 32;
    }


}
