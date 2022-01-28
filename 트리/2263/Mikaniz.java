import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());

		int[] in = new int[n];
		int[] in_index = new int[n + 1];
		int[] post = new int[n];

		StringTokenizer st;

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < n; i++) {
			in[i] = Integer.parseInt(st.nextToken());
			in_index[in[i]] = i;
		}

		st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < n; i++) {
			post[i] = Integer.parseInt(st.nextToken());
		}

		printPre(n, 0, n - 1, 0, n - 1, in, post, in_index);
	}

	public static void printPre(int n, int in_p, int in_r, int post_p, int post_r, int[] in, int[] post, int[] in_index) {
		if (in_p <= in_r && post_p <= post_r) {
			int c = post[post_r];
			int c_in = in_index[c];

			System.out.print(c + " ");
			
			if (in_p != in_r && post_p != post_r) {
				printPre(n, in_p, c_in - 1, post_p, post_p + c_in - 1 - in_p, in, post, in_index);
				printPre(n, c_in + 1, in_r, post_r - in_r + c_in, post_r - 1, in, post, in_index);
			}
		}
	}

}
