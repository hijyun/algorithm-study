import java.util.Arrays;
import java.util.Scanner;

public class Mikaniz {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		
		int[][] coord = new int[n][2];
		for (int i = 0; i < n; i++) {
			coord[i][0] = scan.nextInt();
			coord[i][1] = scan.nextInt();
		}
		
		scan.close();
		
		Arrays.sort(coord, (o1, o2) -> {
			if (o1[0] == o2[0]) {
				return Integer.compare(o1[1], o2[1]);
			} else {
				return Integer.compare(o1[0], o2[0]);
			}
		});
		
		for (int i = 0; i < n; i++) {
			System.out.println(coord[i][0] + " " + coord[i][1]);
		}
	}

}
