import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Queue;
import java.util.LinkedList;

public class Mikaniz {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());

		HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());

			ArrayList<Integer> n1_edges = graph.get(n1);
			if (n1_edges == null) {
				n1_edges = new ArrayList<Integer>();
			}
			n1_edges.add(n2);
			graph.put(n1, n1_edges);

			ArrayList<Integer> n2_edges = graph.get(n2);
			if (n2_edges == null) {
				n2_edges = new ArrayList<Integer>();
			}
			n2_edges.add(n1);
			graph.put(n2, n2_edges);
		}

		printDFS(V, graph, new boolean[N + 1]);
		System.out.println();
		printBFS(V, graph, new boolean[N + 1]);
		System.out.println();
	}

	public static void printDFS(int V, HashMap<Integer, ArrayList<Integer>> graph, boolean[] visited) {
		visited[V] = true;
		System.out.print(V + " ");

		ArrayList<Integer> edges = graph.get(V);
		if (edges != null) {
			Collections.sort(edges);
			for (int node : edges) {
				if (!visited[node]) {
					printDFS(node, graph, visited);
				}
			}
		}
	}

	public static void printBFS(int V, HashMap<Integer, ArrayList<Integer>> graph, boolean[] visited) {
		Queue<Integer> q = new LinkedList<>();

		q.add(V);
		visited[V] = true;
		while(!q.isEmpty()) {
			int n = q.poll();
			System.out.print(n + " ");

			ArrayList<Integer> edges = graph.get(n);
			if (edges != null) {
				Collections.sort(edges);
				for (int node : edges) {
					if (!visited[node]) {
						q.add(node);
						visited[node] = true;
					}
				}
			}
		}
	}

}
