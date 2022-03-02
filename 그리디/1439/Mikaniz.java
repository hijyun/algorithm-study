import java.util.Scanner;

public class Mikaniz {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		sc.close();
		
		char pre = S.charAt(0);
		int[] count = new int[2];
		int len = S.length();
		for (int i = 1; i < len; i++) {
			char now = S.charAt(i);
			if (now != pre) {
				count[pre - '0']++;
				pre = now;
			}
		}
		count[pre - '0']++;
		System.out.println(count[0] < count[1] ? count[0] : count[1]);
	}

}
