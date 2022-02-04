import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Mikaniz {

	static int[] mx = { -1, -2, -2, -1, 1, 2, 2, 1 };
	static int[] my = { -2, -1, 1, 2, -2, -1, 1, 2 };
	
	static class Point {
		int x;
		int y;
		int count;
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
			this.count = 0;
		}
		
		public Point(int x, int y, int count) {
			this.x = x;
			this.y = y;
			this.count = count;
		}
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		for (int i = 0; i < n; i++) {
			int m = Integer.parseInt(br.readLine());
			
			StringTokenizer st;
			
			st = new StringTokenizer(br.readLine(), " ");
			int sx = Integer.parseInt(st.nextToken());
			int sy = Integer.parseInt(st.nextToken());
			Point start = new Point(sx, sy);
			
			st = new StringTokenizer(br.readLine(), " ");
			int gx = Integer.parseInt(st.nextToken());
			int gy = Integer.parseInt(st.nextToken());
			Point goal = new Point(gx, gy);
			
			System.out.println(findMinMove(m, start, goal));
		}
	}
	
	public static int findMinMove(int m, Point start, Point goal) {
		boolean[][] visited = new boolean[m][m];
		Queue<Point> q = new LinkedList<>();
		
		q.add(start);
		visited[start.x][start.y] = true;
		while (!q.isEmpty()) {
			Point now = q.poll();
			
			if (now.x == goal.x && now.y == goal.y) {
				return now.count;
			}
			
			for (int i = 0; i < 8; i++) {
				int x = now.x + mx[i];
				int y = now.y + my[i];
				
				if (x < 0 || y < 0 || x >= m || y >= m) {
					continue;
				}
				if (visited[x][y]) {
					continue;
				}
				
				visited[x][y] = true;
				q.add(new Point(x, y, now.count + 1));
			}
		}
		
		return -1;
	}

}
