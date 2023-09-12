use std::io;
fn bfs(edges : Vec<(i32, i32, i32)>, n : i32) -> bool {
    let mut cost: [i32; 501] = [10001; 501];

    for count in 0..n {
        for i in 0..edges.len() {
            let (cur, next, t) = edges[i];
            if cost[next as usize] > cost[cur as usize] + t {
                cost[next as usize] = cost[cur as usize] + t;
                if count == n - 1 {
                    return true;
                }
            }
        }
    }
    false
}
fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let t : i32 = input.trim().parse().unwrap();
    for _ in 0..t {
        input.clear();
        io::stdin().read_line(&mut input).unwrap();
        let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        
        let n = iter.next().unwrap();
        let m = iter.next().unwrap();
        let w = iter.next().unwrap();
        let mut edges: Vec<(i32, i32, i32)> = Vec::new();

        for _ in 0..m {
            input.clear();
            io::stdin().read_line(&mut input).unwrap();
            let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());

            let s = iter.next().unwrap();
            let e = iter.next().unwrap();
            let t = iter.next().unwrap();

            edges.push((s, e, t));
            edges.push((e, s, t));
        }

        for _ in 0..w {
            input.clear();
            io::stdin().read_line(&mut input).unwrap();
            let mut iter = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());

            let s = iter.next().unwrap();
            let e = iter.next().unwrap();
            let t = iter.next().unwrap();

            edges.push((s, e, -t));
        }
        
        if bfs(edges, n) {
            println!("YES");
        } else {
            println!("NO");
        }
    }
}
