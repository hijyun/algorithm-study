import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int[] x1 = new int[n];
		int[] x2 = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < n; i++) {
			x1[i] = Integer.parseInt(st.nextToken());
			x2[i] = x1[i];
		}
		
		Arrays.sort(x2);
		
		HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
		int index = 0;
		for (int i = 0; i < n; i++) {
			if (!count.containsKey(x2[i])) {
				count.put(x2[i], index);
				index++;
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < n; i++) {
			sb.append(count.get(x1[i])).append(" ");
		}
		
		System.out.println(sb);
	}

}
