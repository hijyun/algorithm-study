import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int len = Integer.parseInt(br.readLine());
		
		String str = br.readLine();
		char[] arr = new char[len];
		for (int i = 0; i < len; i++) {
			arr[i] = str.charAt(i);
		}
		
		long hash = 0;
		long r = 1;
		for (int i = 0; i < len; i++) {
			hash += ((long) (arr[i] - 'a' + 1) * r) % 1234567891;
			r *= 31;
			r %= 1234567891;
		}
		hash %= 1234567891;
		
		System.out.println(hash);
	}

}
