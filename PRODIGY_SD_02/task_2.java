/*
    Build a program that generates a random number and challenges the user to guess it. 
    The program should prompt the user to input their guess, compare it to the generated number, 
    and provide feedback if the guess is too high or too low. It should continue until the user 
    correctly guesses the number and then display the number of attempts it took to win the game.
*/


import java.util.*;

class Demo 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        int randomNumber = (int)((Math.random() * 100) + 1); 

        int guess = 0;
        int attempts = 0;


        while (guess != randomNumber) 
        {
            attempts++;
            System.out.println("\nRound No. " + attempts);
            System.out.print("Enter your guess (between 1 and 100): ");
            guess = scanner.nextInt();



            if (guess < randomNumber) 
            {
                System.out.println("The random number entered by the user is too low compared to the random number formed. Try again.");
                System.out.println("Let's move on to the next round.");
            } 
            else if (guess > randomNumber) 
            {
                System.out.println("The random number entered by the user is too high compared to the random number formed. Try again.");
                System.out.println("Let's move on to the next round.");
            } 
            else 
            {
                System.out.println("Congratulations! You've guessed the number.");
                System.out.println("It took you " + attempts + " attempts.");
            }
        }


        scanner.close();
    }
}
