import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Mikaniz {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		
		int[] arr = new int[n];
		ArrayList<Integer> sortedList = new ArrayList<Integer>();
		for (int i = 0; i < n; i++) {
			arr[i] = scan.nextInt();
			sortedList.add(arr[i]);
		}
		
		scan.close();
		
		Collections.sort(sortedList);
		for (int i = 0; i < n; i++) {
			int index = sortedList.indexOf(arr[i]);
			System.out.print(index + " ");
			sortedList.set(index, -1);
		}
	}

}
