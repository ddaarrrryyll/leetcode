class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int cols = image[0].length;
        int rows = image.length;
        boolean[][] visited = new boolean[rows][cols];
        
        int ori = image[sr][sc];
        // start fill
        image[sr][sc] = color;
        visited[sr][sc] = true;
        fillNeighbours(image, visited, sr+1, sc, ori, color);
        fillNeighbours(image, visited, sr-1, sc, ori, color);
        fillNeighbours(image, visited, sr, sc+1, ori, color);
        fillNeighbours(image, visited, sr, sc-1, ori, color);
        
        return image;
    }
    
    public void fillNeighbours(int[][] image, boolean[][] visited, int x, int y, int ori, int color) {
        
        if (x < 0 || x >= image.length) return;
        if (y < 0 || y >= image[0].length) return;
        
        if (visited[x][y] || image[x][y] != ori) return;
        
        image[x][y] = color;
        visited[x][y] = true;
        fillNeighbours(image, visited, x+1, y, ori, color);
        fillNeighbours(image, visited, x-1, y, ori, color);
        fillNeighbours(image, visited, x, y+1, ori, color);
        fillNeighbours(image, visited, x, y-1, ori, color);
    }
}