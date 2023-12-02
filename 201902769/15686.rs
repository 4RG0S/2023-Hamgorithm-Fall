use std::collections::VecDeque;
use std::io;

fn inRange(x: i32, y: i32, n: i32) -> bool {
    return x >= 0 && x < n && y >= 0 && y < n;
}

fn combinations<T: Clone>(data: &[T], len: usize) -> Vec<Vec<T>> {
    if len == 0 {
        return vec![Vec::new()];
    }

    let mut result = Vec::new();
    let mut stack = Vec::new();
    let mut index = 0;

    while index < data.len() {
        stack.push((index, vec![data[index].clone()]));

        while !stack.is_empty() {
            let (i, mut combination) = stack.pop().unwrap();
            if combination.len() == len {
                result.push(combination.clone());
            } else {
                for j in i + 1..data.len() {
                    let mut new_combination = combination.clone();
                    new_combination.push(data[j].clone());
                    stack.push((j, new_combination));
                }
            }
        }

        index += 1;
    }

    result
}

fn bfs(mut queue: VecDeque<(i32, i32, i32)>, mut array: Vec<Vec<i32>>, n: i32, m: i32) -> i32 {
    let mut visited: [[bool; 100]; 100] = [[false; 100]; 100];
    let mut dx: Vec<i32> = vec![0, 0, 1, -1];
    let mut dy: Vec<i32> = vec![1, -1, 0, 0];
    let mut answer = 0;

    while !queue.is_empty() {
        let (count, x, y) = queue.pop_front().unwrap();
        visited[x as usize][y as usize] = true;

        for i in 0..4 {
            let nx = x + dx[i];
            let ny = y + dy[i];

            if !inRange(nx, ny, n) {
                continue;
            }

            if visited[nx as usize][ny as usize] {
                continue;
            }

            if array[nx as usize][ny as usize] == 1 {
                answer += count + 1;
            }
            visited[nx as usize][ny as usize] = true;
            array[nx as usize][ny as usize] = 2;
            queue.push_back((count + 1, nx, ny));
        }
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.split_whitespace();

    let n = iter.next().unwrap().parse::<i32>().unwrap();
    let m = iter.next().unwrap().parse::<i32>().unwrap();

    let mut array: Vec<Vec<i32>> = Vec::new();
    let mut queue: VecDeque<(i32, i32, i32)> = VecDeque::new();

    for i in 0..n {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();

        let row: Vec<i32> = input
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        for (j, &val) in row.iter().enumerate() {
            if val == 2 {
                queue.push_back((0, i.try_into().unwrap(), j.try_into().unwrap()));
            }
        }
        array.push(row);
    }

    let mut answer = i32::MAX;
    let queue_slice: &[(_, _, _)] = &queue.iter().cloned().collect::<Vec<_>>();
    for combination in combinations(queue_slice, m as usize) {
        let cloned_combination: VecDeque<(i32, i32, i32)> =
            combination.iter().cloned().collect();
        let cur = bfs(cloned_combination, array.clone(), n, m);
        // println!("{} ", cur);
        if answer > cur {
            answer = cur;
        }
    }

    print!("{}", answer);
}
