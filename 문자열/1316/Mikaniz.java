import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		int count = 0;
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			
			boolean[] in = new boolean[26];
			boolean group = true;
			
			int len = str.length();
			char pre = str.charAt(0);
			for (int j = 0; j < len; j++) {
				char now = str.charAt(j);
				
				if (in[now - 'a'] && pre != now) {
					group = false;
					break;
				}
				
				in[now - 'a'] = true;
				pre = now;
			}
			
			if (group) {
				count++;
			}
		}
		
		System.out.println(count);
	}

}
