public class AccountData {
    private StringBuilder name = new StringBuilder();
    private int balance;
    private int accNum;
   

    public boolean Verify(StringBuilder Input_Account){


        //NOT YET MADE, TO BE FOLLOWED.


        return false;
    }
    //constructor
    public AccountData(){
        this.balance = 5000;
        this.accNum = 0;
    }

    public AccountData(StringBuilder name, int balance, int accNum){
        this.name = name;
        this.balance = balance;
        this.accNum = accNum;
    }
    
    //check balance
    public void checkBalance(){
        System.out.println("Name: " + name + "\nAccount Number: " + accNum + "\nBalance: " + balance);
    }
    //deposit
    public void deposit(int value){
        this.balance += value;
        System.out.println("New Balance: " + this.balance);
    }
    //withdraw
    public void withdraw(int value){
        this.balance -= value;
        System.out.println("New Balance: " + this.balance);
    }
}
