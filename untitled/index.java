public class Dog extends DogShow{
    public void bark() {System.out.print("woof");}
}
class Hound extend Dog{
    public void sniff(){System.out.print("sniff");}
    public void bark(){System.out.print("howl");}

}
class DogShow{
    public static void main(String[]arg) {new DogShow().go()}
    void go(){
        new Hound().bark();
        ((Dog) new Hound().bark();)
        ((Dog) new Hound().sniff();)
    }
}
public synchronized