
/**
 * ATM Machine System
    user is perform the following operations
        check balance
        deposit
        withdraw 
        exit (end transaction)
 */
import java.util.InputMismatchException;
import java.util.Scanner;

public class Atm {

    private static void PressToContinue(Scanner scanner) {
        System.out.println("Press Enter to Continue...");
        scanner.nextLine(); // absorbs the "\n" from nextInt();
        scanner.nextLine(); // absorbs the Enter key;

    }

    public static void main(String[] args) {

        // On and Off switch of the program
        boolean program = true;

        // initialize
        AccountData User = new AccountData();
        Scanner _input = new Scanner(System.in);

        // LogIn System:

        // enter the acc num to test
        // System.out.println("Enter Account Name: ");
        // StringBuilder accountnum;
        // accountnum.append(_input.nextLine());
        // //initialize databank
        // String _filename = "names.txt";

        do {

            // User.name = accountnum;
            System.out.println(
                    "<-----JAVA ATM MACHINE----->\nSelect an Option:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\nChoice:");

            int choice = _input.nextInt();
            switch (choice) {
                case 1:
                    // check balance
                    User.checkBalance();
                    PressToContinue(_input);
                    break;
                case 2:
                    // deposit
                    System.out.println("Enter Deposit Value: ");
                    try {
                        int Depositvalue = _input.nextInt();
                        User.deposit(Depositvalue);
                    } catch (InputMismatchException e) {
                        System.out.println("Error, Please input whole numbers only,");
                        _input.next();
                    }

                    PressToContinue(_input);
                    break;
                case 3:
                    // withdraw
                    System.out.println("Enter Withdraw Value: ");

                    try {
                        int Withdrawvalue = _input.nextInt();
                        User.withdraw(Withdrawvalue);
                    } catch (InputMismatchException e) {
                        System.out.println("Error, Please input whole numbers only,");
                        _input.next();
                    }

                    PressToContinue(_input);
                    break;
                case 4:
                    // exit
                    System.out.println("Thank you! See you Again!");
                    _input.close(); // closes the scanner
                    program = false;

            }

        } while (program);
        return;
    }
}
