import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		String[] input_nums = input.split("-|\\+");
		input = input.replaceAll("[0-9]", "");
		
		int min = Integer.parseInt(input_nums[0]);
		int len = input.length();
		boolean minus = false;
		for (int i = 0; i < len; i++) {
			if (input.charAt(i) == '-') {
				minus = true;
			}
			
			if (minus) {
				min -= Integer.parseInt(input_nums[i + 1]);
			} else {
				min += Integer.parseInt(input_nums[i + 1]);
			}
		}
		
		System.out.println(min);
	}

}
