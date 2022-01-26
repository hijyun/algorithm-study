import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int k = Integer.parseInt(br.readLine());
		
		int num = (int) Math.pow(2, k) - 1;
		int[] tree = new int[num];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < num; i++) {
			tree[i] = Integer.parseInt(st.nextToken());
		}
		
		int start = num / 2;
		int gap = num + 1;
		for (int i = 0; i < k; i++) {
			for (int j = 0; j < Math.pow(2, i); j++) {
				System.out.print(tree[start + gap * j] + " ");
			}
			gap /= 2;
			start -= gap / 2;
			System.out.println();
		}
	}

}
