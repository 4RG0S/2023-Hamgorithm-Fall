use std::io;

fn recursion(m: usize, v: &Vec<usize>, current: &mut Vec<usize>, visited: &mut Vec<bool>) {
    if current.len() == m {
        println!("{}", current.iter().map(|&x| x.to_string()).collect::<Vec<String>>().join(" "));
        return;
    }

    let mut temp = 0;
    for i in 0..v.len() {
        if !visited[i] && temp != v[i] {
            visited[i] = true;
            current.push(v[i]);
            temp = v[i];
            recursion(m, v, current, visited);
            visited[i] = false;
            current.pop();
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut iter = input.trim().split_whitespace();

    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut v = vec![];
    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    iter = input.trim().split_whitespace();
    for _ in 0..n {
        let cur: usize = iter.next().unwrap().parse().unwrap();
        v.push(cur);
    }

    v.sort();

    let mut current = vec![];
    let mut visited = vec![false; n];

    recursion(m, &v, &mut current, &mut visited);
}
