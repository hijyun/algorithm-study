import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class mikaniz {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		scan.close();
		
		int length = 0;
		int n = num;
		while (n > 0) {
			length++;
			n /= 10;
		}
		
		Integer[] arr = new Integer[length];
		for (int i = 0; i < length; i++) {
			arr[i] = num % 10;
			num /= 10;
		}
		
		Arrays.sort(arr, Collections.reverseOrder());
		for(int i = 0; i < length; i++) {
			System.out.print(arr[i]);
		}
	}

}
