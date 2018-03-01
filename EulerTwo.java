public class EulerTwo {
   public static void main(String[] args) {
      long sigma = 0;
      long first = 1;
      long second = 2;
      long third = 3;

      while (third < 4000000) {
         if (second%2 == 0) {
            sigma+=second;
         }
         third = first + second;
         first = second;
         second = third;
      }
      System.out.println(sigma);
   }
}