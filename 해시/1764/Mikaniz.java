import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;
import java.util.HashMap;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		HashMap<String, Integer> nameCount = new HashMap<String, Integer>();
		for (int i = 0; i < n; i++) {
			nameCount.put(br.readLine(), 1);
		}
		
		for (int i = 0; i < m; i++) {
			String name = br.readLine();
			if (nameCount.containsKey(name)) {
				nameCount.replace(name, 2);
			}
		}
		
		Object[] names = nameCount.keySet().toArray();
		Arrays.sort(names);
		
		StringBuilder sb = new StringBuilder();
		int count = 0;
		for (Object name : names) {
			if (nameCount.get(name) == 2) {
				count++;
				sb.append(name).append("\n");
			}
		}
		
		System.out.println(count);
		System.out.println(sb);
	}

}
