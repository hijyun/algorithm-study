import java.util.Arrays;
import java.util.Scanner;

public class Mikaniz {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		
		int[] a = new int[n];
		for (int i = 0; i < n; i++) {
			a[i] = scan.nextInt();
		}
		
		int x = scan.nextInt();
		
		scan.close();
		
		Arrays.sort(a);
		
		int count = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] >= x) {
				break;
			}
			
			for (int j = i + 1; j < n; j++) {
				if (a[i] + a[j] == x) {
					count++;
					break;
				} else if (a[i] + a[j] > x) {
					break;
				}
			}
		}
		
		System.out.println(count);
	}

}
