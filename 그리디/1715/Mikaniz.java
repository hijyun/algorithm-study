import java.util.Scanner;
import java.util.PriorityQueue;

public class Mikaniz {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();

		PriorityQueue<Integer> cards = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			cards.offer(sc.nextInt());
		}

		sc.close();
		
		int count = 0;
		while (cards.size() > 1) {
			int merge = cards.poll() + cards.poll();
			cards.offer(merge);
			count += merge;
		}
		System.out.println(count);
	}

}
