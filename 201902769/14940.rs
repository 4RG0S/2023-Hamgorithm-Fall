use std::io;
use std::collections::VecDeque;

fn bfs(grid: &Vec<Vec<i32>>, target: (usize, usize)) -> Vec<Vec<i32>> {
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)];
    let mut distances = vec![vec![-1; grid[0].len()]; grid.len()];
    let mut queue = VecDeque::new();
    
    distances[target.0][target.1] = 0;
    queue.push_back(target);
    
    while let Some((x, y)) = queue.pop_front() {
        for &(dx, dy) in &directions {
            let nx = (x as i32 + dx) as usize;
            let ny = (y as i32 + dy) as usize;
            
            if nx < grid.len() && ny < grid[0].len() && grid[nx][ny] == 1 && distances[nx][ny] == -1 {
                distances[nx][ny] = distances[x][y] + 1;
                queue.push_back((nx, ny));
            }
        }
    }
    for i in 0..grid.len() {
        for j in 0..grid[0].len() {
            if grid[i][j] == 0 {
                distances[i][j] = 0;
            }
        }
    }
    distances
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let nm: Vec<usize> = input.trim().split_whitespace().map(|n| n.parse().unwrap()).collect();
    let (n, m) = (nm[0], nm[1]);

    let mut grid = Vec::new();
    let mut target = (0, 0);
    
    for i in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let row: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse().unwrap()).collect();
        if let Some(j) = row.iter().position(|&x| x == 2) {
            target = (i, j);
        }
        grid.push(row);
    }

    let distances = bfs(&grid, target);
    
    for i in 0..n {
        for j in 0..m {
            print!("{} ", distances[i][j]);
        }
        println!();
    }
}
